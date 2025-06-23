import os
import pandas as pd
import re
from pathlib import Path
from datetime import datetime

def extract_date_from_filename(filename):
    """
    Extract date from ERCOT filename format like:
    cdr.00012331.0000000000000000.20220406.122934.DAMSPNP4190.csv
    Returns the date as a datetime object
    """
    # Look for pattern like 20220406 in the filename
    date_pattern = r'\.(\d{8})\.'
    match = re.search(date_pattern, filename)
    if match:
        date_str = match.group(1)
        try:
            return datetime.strptime(date_str, '%Y%m%d')
        except ValueError:
            return None
    return None

def find_and_sort_csv_files(data_dir):
    """
    Find all CSV files in the data directory and sort them by date
    """
    csv_files = []
    
    for root, dirs, files in os.walk(data_dir):
        for file in files:
            if file.endswith('.csv'):
                file_path = os.path.join(root, file)
                date = extract_date_from_filename(file)
                if date:
                    csv_files.append((file_path, date))
    
    # Sort by date
    csv_files.sort(key=lambda x: x[1])
    
    print(f"Found {len(csv_files)} CSV files")

    if not csv_files:
        return []

    print(f"Date range: {csv_files[0][1].strftime('%Y-%m-%d')} to {csv_files[-1][1].strftime('%Y-%m-%d')}")
    
    return [file_path for file_path, date in csv_files]

def merge_csv_files(csv_files, output_file):
    """
    Merge all CSV files into one large CSV file, sorted chronologically.
    """
    print(f"Starting to merge {len(csv_files)} CSV files...")
    
    # Read and concatenate all CSV files
    dataframes = []
    
    for i, csv_file in enumerate(csv_files):
        try:
            print(f"Processing file {i+1}/{len(csv_files)}: {os.path.basename(csv_file)}")
            df = pd.read_csv(csv_file)
            dataframes.append(df)
        except Exception as e:
            print(f"Error reading {csv_file}: {str(e)}")
            continue
    
    if not dataframes:
        print("No valid CSV files found!")
        return
    
    # Concatenate all dataframes
    print("Concatenating all dataframes...")
    merged_df = pd.concat(dataframes, ignore_index=True)
    
    print("Sorting data chronologically...")
    try:
        # Clean column names by stripping whitespace
        merged_df.columns = merged_df.columns.str.strip()

        # Create a datetime column for sorting based on ERCOT's definition
        # HourEnding 01 is 00:00-00:59, so we subtract 1 hour.
        merged_df['HourEnding_int'] = merged_df['HourEnding'].astype(str).str.split(':').str[0].astype(int)
        merged_df['datetime'] = pd.to_datetime(merged_df['DeliveryDate'], errors='coerce') + \
                                pd.to_timedelta(merged_df['HourEnding_int'] - 1, unit='h')
        
        # Drop rows where datetime could not be parsed
        merged_df.dropna(subset=['datetime'], inplace=True)
        
        # Sort by the new datetime column
        merged_df = merged_df.sort_values(by='datetime')
        
        # Clean up helper columns
        merged_df = merged_df.drop(columns=['datetime', 'HourEnding_int'])
        print("Data sorted successfully.")
    except KeyError as e:
        print(f"A required column is missing: {e}. Please check the CSV files.")
        return
    except Exception as e:
        print(f"Could not sort the data. Please check 'DeliveryDate' and 'HourEnding' columns. Error: {e}")
        return

    # Create output directory if it doesn't exist
    output_dir = os.path.dirname(output_file)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Save to CSV
    print(f"Saving merged data to {output_file}")
    print(f"Total rows: {len(merged_df)}")
    print(f"Total columns: {len(merged_df.columns)}")
    
    merged_df.to_csv(output_file, index=False)
    print(f"Successfully saved merged CSV to {output_file}")
    
    # Display sample of the data
    print("\nFirst few rows of merged data:")
    print(merged_df.head())
    print("\nColumn names:")
    print(merged_df.columns.tolist())

def main():
    # Path to the ERCOT Data directory
    ercot_data_dir = "Data/ERCOT Data"
    output_file = "Data/MegedDAM.csv"
    
    # Check if directory exists
    if not os.path.exists(ercot_data_dir):
        print(f"Directory {ercot_data_dir} not found!")
        return
    
    print(f"Starting CSV merge from {ercot_data_dir}")
    
    # Find and sort CSV files
    csv_files = find_and_sort_csv_files(ercot_data_dir)
    
    if not csv_files:
        print("No CSV files found! Please ensure that the zip files have been extracted correctly in 'Data/ERCOT Data'.")
        return
    
    # Merge CSV files
    merge_csv_files(csv_files, output_file)

if __name__ == "__main__":
    main() 
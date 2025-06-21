import pandas as pd
from pathlib import Path

root_data_dir = Path("Data")
csv_files = list(root_data_dir.glob("*.csv"))
print(f"Found {len(csv_files)} CSV files to merge")

all_dataframes = []

for csv_file in csv_files:
    print(f"Reading: {csv_file}")
    try:
        df = pd.read_csv(csv_file)
        all_dataframes.append(df)
    except Exception as e:
        print(f"Error reading {csv_file}: {e}")

print("Merging all CSV files...")
merged_df = pd.concat(all_dataframes, ignore_index=True)
merged_df['DeliveryDate'] = pd.to_datetime(merged_df['DeliveryDate'])
merged_df['HourNum'] = merged_df['HourEnding'].str.extract(r'(\d+)').astype(int)
print("Sorting chronologically...")
merged_df = merged_df.sort_values(['DeliveryDate', 'HourNum'], ascending=[True, True])
merged_df = merged_df.drop('HourNum', axis=1)
merged_df = merged_df.reset_index(drop=True)
output_file = root_data_dir / "merged_ercot_data.csv"
merged_df.to_csv(output_file, index=False)

print(f"Merged CSV saved as: {output_file}")
print(f"Total rows: {len(merged_df)}")
print(f"Date range: {merged_df['DeliveryDate'].min()} to {merged_df['DeliveryDate'].max()}")
print(f"Unique settlement points: {merged_df['SettlementPoint'].nunique()}")

print("\nFirst 10 rows:")
print(merged_df.head(10))
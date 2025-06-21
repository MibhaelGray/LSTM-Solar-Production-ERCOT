import os
import zipfile
import glob
from pathlib import Path

def unzip_all_files(data_dir):
    """
    Recursively unzip all zip files in the given directory and its subdirectories.
    Each zip file will be extracted to a folder with the same name (minus .zip extension).
    """
    # Find all zip files recursively
    zip_files = []
    for root, dirs, files in os.walk(data_dir):
        for file in files:
            if file.endswith('.zip'):
                zip_files.append(os.path.join(root, file))
    
    print(f"Found {len(zip_files)} zip files to extract")
    
    # Extract each zip file
    for zip_path in zip_files:
        try:
            # Create destination directory (same name as zip file, minus .zip)
            dest_dir = zip_path[:-4]  # Remove .zip extension
            
            # Skip if destination already exists and has content
            if os.path.exists(dest_dir) and len(os.listdir(dest_dir)) > 0:
                print(f"Skipping {zip_path} - destination already exists with content")
                continue
            
            print(f"Extracting {zip_path} to {dest_dir}")
            
            # Create destination directory if it doesn't exist
            os.makedirs(dest_dir, exist_ok=True)
            
            # Extract the zip file
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(dest_dir)
                
            print(f"Successfully extracted {zip_path}")
            
        except Exception as e:
            print(f"Error extracting {zip_path}: {str(e)}")
    
    print("Extraction complete!")

def main():
    # Path to the ERCOT Data directory
    ercot_data_dir = "Data/ERCOT Data"
    
    # Check if directory exists
    if not os.path.exists(ercot_data_dir):
        print(f"Directory {ercot_data_dir} not found!")
        return
    
    print(f"Starting extraction from {ercot_data_dir}")
    unzip_all_files(ercot_data_dir)

if __name__ == "__main__":
    main() 
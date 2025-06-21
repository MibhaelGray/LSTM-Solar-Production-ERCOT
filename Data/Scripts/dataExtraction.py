import os
import shutil
from pathlib import Path

path_1 = Path(r"Data\ERCOT Data\2022-01-01_to_2022-04-06")
path_2 = Path(r"Data\ERCOT Data\2022-04-07_to_2023-08-18")
path_3 = Path(r"Data\ERCOT Data\2023-08-19 - 2024-12-31")

root_data_dir = Path("Data")

root_data_dir.mkdir(exist_ok=True)

paths = [path_1, path_2, path_3]

for path in paths:
    print(f"Processing: {path}")

    csv_files = list(path.rglob("*.csv"))
    
    for csv_file in csv_files:

        destination = root_data_dir / csv_file.name
        counter = 1
        original_destination = destination
        while destination.exists():
            stem = original_destination.stem
            suffix = original_destination.suffix
            destination = root_data_dir / f"{stem}_{counter}{suffix}"
            counter += 1
        
        shutil.copy2(csv_file, destination)
        print(f"Copied: {csv_file} -> {destination}")
csv_count = len(list(root_data_dir.glob("*.csv")))
print(f"Total CSV files in Data directory: {csv_count}")


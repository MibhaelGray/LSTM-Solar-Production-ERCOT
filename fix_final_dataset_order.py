import pandas as pd

# Load the dataset
input_path = "Data/ERCOT Data/final_ercot_dataset.csv"
df = pd.read_csv(input_path)

# Convert to datetime if not already
if not pd.api.types.is_datetime64_any_dtype(df['Hour Ending']):
    df['Hour Ending'] = pd.to_datetime(df['Hour Ending'])

# Sort by datetime
sorted_df = df.sort_values('Hour Ending').reset_index(drop=True)

# Save back to CSV (overwrite the original file)
sorted_df.to_csv(input_path, index=False)

print(f"Sorted and saved: {input_path}") 
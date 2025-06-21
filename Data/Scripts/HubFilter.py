import pandas as pd

try:
    merged_data = pd.read_csv(r"Data\merged_ercot_data.csv", engine='python')
    print("Successfully loaded with python engine")
    print(merged_data.head())
    
    filtered_df = merged_data[merged_data["SettlementPoint"].isin(['HB_NORTH', 'HB_WEST'])]
    print(filtered_df.head())
    
except Exception as e:
    print(f"Error: {e}")


filtered_df.to_csv(r"Data\filter_merged_ercot_data.csv")
import pandas as pd
import os
from datetime import datetime, timedelta

# Step 1: Import libraries
# (Already imported above)

# Step 2: List all .txt files in the folder with specific suffixes
folder_path = '/Users/joshuaingram/Main/Projects/SolarFlareNN/data/designaled/'  # Replace with your folder path
suffixes = ['_18_bg', '_17_bg', '_16_bg']
dfs = {}

for suffix in suffixes:
    txt_files = [f for f in os.listdir(folder_path) if f.endswith(f"{suffix}.txt")]
    
    # Step 3: Read each .txt file into a DataFrame
    temp_dfs = []
    for txt_file in txt_files:
        file_path = os.path.join(folder_path, txt_file)
        df = pd.read_csv(file_path, header=None, delim_whitespace=True, names=['seconds_since_2000', f'designaled_flux{suffix}'])
        temp_dfs.append(df)
        
    # Step 4: Concatenate DataFrames with the same suffix
    dfs[suffix] = pd.concat(temp_dfs, ignore_index=True)

# Step 5: Sort each DataFrame by the date column
for suffix, df in dfs.items():
    dfs[suffix] = df.sort_values(by='date_seconds_since_2000')

# Step 6: Merge all DataFrames on 'date_seconds'
final_df = dfs['_18']
for suffix in ['_17', '_16']:
    final_df = pd.merge(final_df, dfs[suffix], on='seconds_since_2000', how='outer')

# Step 7: Convert the date column to date-time format
epoch_start = datetime(2000, 1, 1)
final_df['date_time'] = final_df['seconds_since_2000'].apply(lambda x: epoch_start + timedelta(seconds=x))

# Show the first few rows of the final DataFrame
print(final_df.head())
import pandas as pd
import glob
import os

os.chdir('C:/Users/N/Projects/dataset/scripts/pythonProject/school')

all_files = glob.glob(f'parsed_data/*.csv')

df_list = []
for file in all_files:
    df = pd.read_csv(file)
    df_list.append(df)

merged_df = pd.concat(df_list, ignore_index=True)

output_file = f'preprocessed/school_merge.csv'

merged_df.to_csv(output_file, index=False)

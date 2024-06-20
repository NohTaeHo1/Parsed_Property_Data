import pandas as pd
import glob
import os

os.chdir('C:/Users/N/Projects/dataset/scripts/pythonProject/apt_transaction_details')

all_files = glob.glob(f'raw/*.csv')

df_list = []
for file in all_files:
    df = pd.read_csv(file)
    df_list.append(df)

merged_df = pd.concat(df_list, ignore_index=True)

output_file = f'preprocessed/apart_trade_detail_2020_202405.csv'

merged_df.to_csv(output_file, index=False)

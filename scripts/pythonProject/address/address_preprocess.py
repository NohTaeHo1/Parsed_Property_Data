import pandas as pd
import os
import geopandas as gpd
import glob


legal_info_b_seoul = pd.read_csv("C:/Users/N/Projects/dataset/data/processed/legal_info_b_seoul.csv")
legal_info_b_seoul = legal_info_b_seoul.astype({'법정동코드': 'str', '법정동시군구코드': 'str', '법정동읍면동코드': 'str'})

legal_info_b_seoul['법정동코드_2'] = legal_info_b_seoul['법정동코드'].str[:8] + '00'

print(legal_info_b_seoul.dtypes)

os.chdir("C:/Users/N/Projects/dataset/scripts/pythonProject")

geo_data = gpd.read_file('geoservice/emd.shp', dtype={'EMD_CD': object}, encodings='utf-8')

print(geo_data.dtypes)
geo_data['EMD_CD'] = geo_data['EMD_CD'] + '00'

geo_data.rename(columns={'EMD_CD': '법정동코드_2'}, inplace=True)

geo_data = geo_data.astype({'법정동코드_2': 'str'})

geo_data = geo_data[['법정동코드_2', 'geometry']]

print(geo_data.head(3))

legal_geo_info = pd.merge(legal_info_b_seoul, geo_data, on='법정동코드_2', how='left')

legal_geo_info2 = legal_geo_info[['법정동코드', '시도명', '시군구명', '읍면동명', 'geometry']].drop_duplicates()
output_file2 = f'address/preprocessed/legal_geo_info2.csv'
legal_geo_info2.to_csv(output_file2, index=False)

legal_geo_info3 = legal_geo_info[['법정동시군구코드', '시도명', '시군구명']].drop_duplicates()
output_file3 = f'address/preprocessed/legal_geo_info3.csv'
legal_geo_info3.to_csv(output_file3, index=False)

legal_geo_info4 = legal_geo_info[['주소', '법정동코드', '법정동읍면동코드', 'geometry']].drop_duplicates()
output_file4 = f'address/preprocessed/legal_geo_info4.csv'
legal_geo_info4.to_csv(output_file4, index=False)

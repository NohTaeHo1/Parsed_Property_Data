import pandas as pd
import requests
import os

os.chdir('C:/Users/N/Projects/dataset/scripts/pythonProject')

city_park = pd.read_csv('city_park/parsed_data/city_park.csv')
city_park['parkNm'] = city_park['parkNm'].str.replace('&amp;lt;', '<').str.replace('&amp;gt;', '>')


city_park['lnmadr'].fillna('', inplace=True)

city_park_seoul = city_park[city_park['lnmadr'].str.startswith('서울특별시')]

output_file = f'city_park/parsed_data/city_park_seoul.csv'

city_park_seoul.to_csv(output_file, index=False)
print(f'{output_file} 저장 완료')

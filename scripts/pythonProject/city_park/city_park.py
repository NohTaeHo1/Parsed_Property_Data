import pandas as pd
import requests
import os
from bs4 import BeautifulSoup as bs
from dotenv import load_dotenv

load_dotenv()

os.chdir('C:/Users/N/Projects/dataset')

api_key = os.getenv('API_KEY')

column_nm = ['manageNo', 'parkNm', 'parkSe', 'rdnmadr', 'lnmadr', 'latitude', 'longitude',
             'parkAr', 'appnNtfcDate', 'institutionNm', 'phoneNumber', 'referenceDate', 'insttCode']

# # 처음 파일 확인할때 쓰는거
# url = 'http://api.data.go.kr/openapi/tn_pubr_public_cty_park_info_api'
# params ={'serviceKey' : api_key, 'pageNo' : '0', 'numOfRows' : '3', 'type' : 'xml' }
#
# res = requests.get(url, params=params)
#
# soup = bs(res.text, 'xml')
#
# output_file = 'scripts/pythonProject/city_park/city_park_test.xml'
# with open(output_file, 'w', encoding='utf-8') as f:
#     f.write(soup.prettify())

# OpenAPI 요청하기
url = 'http://api.data.go.kr/openapi/tn_pubr_public_cty_park_info_api'
params ={'serviceKey' : api_key, 'pageNo' : '0', 'numOfRows' : '1000000', 'type' : 'xml'}
res = requests.get(url, params)
soup = bs(res.text, 'xml')
items = soup.find_all('item')
total = pd.DataFrame()

for k in range(len(items)):
    df_raw = []
    for j in column_nm:
        try:
            df_raw.append(items[k].find(j).text)
        except:
            df_raw.append('존재하지 않음')

    df = pd.DataFrame(df_raw).T
    df.columns = column_nm
    total = pd.concat([total, df])

total.columns = column_nm

# 데이터 파일로 저장
output_file = f'scripts/pythonProject/city_park/parsed_data/city_park.csv'

total.to_csv(output_file, index=False)
print(f'{output_file} 저장 완료')

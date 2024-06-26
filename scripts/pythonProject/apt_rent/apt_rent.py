import pandas as pd
import requests
import os
from bs4 import BeautifulSoup as bs
from dotenv import load_dotenv

load_dotenv()

os.chdir('C:/Users/N/Projects/dataset')
df = pd.read_csv('data/preprocessed/legal_info_b_seoul.csv')

LAWD_CD_list = df['법정동시군구코드'].unique()

api_key = os.getenv('API_KEY')

column_nm = ['갱신요구권사용', '건축년도', '계약구분', '계약기간', '년', '법정동', '보증금액',
             '아파트', '월', '월세금액', '일', '전용면적', '종전계약보증금', '종전계약월세',
             '지번', '지역코드', '층']


# 처음 파일 확인할때 쓰는거
# url = 'http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptRent'
# params ={'serviceKey' : api_key, 'LAWD_CD' : '11110', 'DEAL_YMD' : '201512' }
#
# res = requests.get(url, params=params)
#
# soup = bs(res.text, 'xml')
#
# output_file = 'scripts/pythonProject/apt_rent/apart_rent_test.xml'
# with open(output_file, 'w', encoding='utf-8') as f:
#     f.write(soup.prettify())


dear_ymd = 202000


for k in range(12):
    total = pd.DataFrame()
    dear_ymd += 1

    # OpenAPI 요청하기
    for i in range(len(LAWD_CD_list)):
        url = 'http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptRent'
        params = {'serviceKey' : api_key, 'LAWD_CD' : f'{LAWD_CD_list[i]}', 'DEAL_YMD' : f'{dear_ymd}' }

        res = requests.get(url, params)
        soup = bs(res.text, 'xml')
        items = soup.find_all('item')

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
    output_file = f'scripts/pythonProject/apt_rent/parsed_data/apart_rent_{dear_ymd}.csv'

    total.to_csv(output_file, index=False)
    print(f'{output_file} 저장 완료')

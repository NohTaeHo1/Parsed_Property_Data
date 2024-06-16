import pandas as pd
import requests
import os
from bs4 import BeautifulSoup as bs
from dotenv import load_dotenv

load_dotenv()

os.chdir('C:/Users/N/Projects/dataset')

df = pd.read_csv('data/processed/legal_info_b.csv')

# 생성한 법정동코드 고유값 지정
LAWD_CD_list = df['법정동시군구코드'].unique()

api_key = os.getenv('API_KEY')

# OpenAPI 요청을 위한 기본 정보 설정
url = 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev'
params = {
    'serviceKey': api_key,
    'pageNo': '1',
    'numOfRows': '5',
    'LAWD_CD': '11110',
    'DEAL_YMD': '202406'
}

column_nm = ['거래금액', '거래유형', '건축년도', '년', '도로명', '도로명건물본번호코드', '도로명건물부번호코드',
             '도로명시군구코드', '도로명일련번호코드', '도로명지상지하코드', '도로명코드', '동', '등기일자', '매도자', '매수자', '법정동', '법정동본번코드',
             '법정동부번코드', '법정동시군구코드', '법정동읍면동코드', '법정동지번코드', '아파트', '월', '일', '일련번호', '전용면적',
             '중개사소재지', '지번', '지역코드', '층']

# API 요청 보내기
res = requests.get(url, params)

# BeautifulSoup을 사용하여 XML 파싱
soup = bs(res.text, 'xml')

# XML 데이터 예쁘게 출력하여 파일로 저장
output_file = 'scripts/pythonProject/parsed_test.xml'

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(soup.prettify())

# XML 데이터를 데이터프레임 형태로 받기
# items는 item 태그를 찾아 리스트 형태로 저장 // [<item> <거래금액> 82,500 </거래금액> </item>] 이런 형태 // item태그마다 하나의 요소

# items = soup.find_all('item')
# total = pd.DataFrame()
#
# for k in range(len(items)):
#     df_raw = []
#     for j in column_nm:
#         df_raw.append(items[k].find(j).text)
#     df = pd.DataFrame(df_raw).T
#     total = pd.concat([total, df])
#
# total.columns = column_nm
#
# print(total.head(3).T)


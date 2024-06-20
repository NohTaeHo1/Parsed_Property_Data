import pandas as pd
import requests
import os
from bs4 import BeautifulSoup as bs
from dotenv import load_dotenv

load_dotenv()


# 서울로 한정된
os.chdir('C:/Users/N/Projects/dataset')
df = pd.read_csv('data/preprocessed/legal_info_b_seoul.csv')

# 생성한 법정동코드 중복제거
LAWD_CD_list = df['법정동시군구코드'].unique()

api_key = os.getenv('API_KEY')

column_nm = ['거래금액', '거래유형', '건축년도', '년', '도로명', '도로명건물본번호코드', '도로명건물부번호코드',
             '도로명시군구코드', '도로명일련번호코드', '도로명지상지하코드', '도로명코드', '동', '등기일자', '매도자', '매수자', '법정동', '법정동본번코드',
             '법정동부번코드', '법정동시군구코드', '법정동읍면동코드', '법정동지번코드', '아파트', '월', '일', '일련번호', '전용면적',
             '중개사소재지', '지번', '지역코드', '층']


dear_ymd = 202000

for k in range(12):
    total = pd.DataFrame()

    dear_ymd += 1
    # OpenAPI 요청하기
    for i in range(len(LAWD_CD_list)):
        url = 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev'
        params = {
            'serviceKey': api_key,
            'pageNo': '1',
            'numOfRows': '1000000',
            'LAWD_CD': '11110',
            'DEAL_YMD': str(dear_ymd)
        }
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
    output_file = 'scripts/pythonProject/raw/apart_trade_detail_' + str(dear_ymd) + '.csv'

    total.to_csv(output_file, index=False)
    print(f'{output_file} 저장 완료')

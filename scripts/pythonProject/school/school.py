import pandas as pd
import requests
import os
from bs4 import BeautifulSoup as bs
from dotenv import load_dotenv

load_dotenv()

os.chdir('C:/Users/N/Projects/dataset')

api_key = os.getenv('NEIS_API_KEY')

column_nm = ['시도교육청코드', '시도교육청명', '행정표준코드', '학교명', '영문학교명', '학교종류명', '시도명',
             '관할조직명', '설립명', '도로명우편번호', '도로명주소', '도로명상세주소', '전화번호', '홈페이지주소',
             '남녀공학구분명', '팩스번호', '고등학교구분명', '산업체특별학급존재여부', '고등학교일반전문구분명', '특수목적고등학교계열명', '입시전후기구분명',
             '주야구분명', '설립일자', '개교기념일', '수정일자']
schools = ["초등학교", "중학교", "고등학교"]
en_schools = ['elementary_school', 'middle_school', 'high_school']

for i in range(3):
    total = pd.DataFrame()

    url = 'https://open.neis.go.kr/hub/schoolInfo'
    pIndex = 1

    while True:
        params = {'KEY': api_key, 'Type': 'xml', 'pIndex': f'{pIndex}', 'pSize': '1000', 'SCHUL_KND_SC_NM': schools[i], 'LCTN_SC_NM': '서울특별시'}

        res = requests.get(url, params)
        print(f"Response Text (first 1000 chars): {res.text[:1000]}")

        soup = bs(res.text, 'xml')
        items = soup.find_all('row')

        if not items:
            break

        for k in range(len(items)):
            df_list = items[k].find_all()
            df_raw = []

            for l in range(len(df_list)):
                df_raw.append(df_list[l].text)
            df = pd.DataFrame(df_raw).T

            df.columns = column_nm
            total = pd.concat([total, df])
        pIndex += 1

    # total.columns = column_nm

    output_file = f'scripts/pythonProject/school/parsed_data/{en_schools[i]}.csv'

    total.to_csv(output_file, index=False)
    print(f'{output_file} 저장 완료')

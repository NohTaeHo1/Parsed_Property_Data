import json
import urllib.request
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

os.chdir('C:/Users/N/Projects/dataset')

# 최근으로부터 12개월치
url = 'https://kosis.kr/openapi/Param/statisticsParameterData.do?method=getList&apiKey=NDU5YzdmZjM4YzBlNDU0ODExY2I1MWZlN2M5NWU5MmU=&itmId=T20+T21+T22+&objL1=11110+11140+11170+11200+11215+11230+11260+11290+11305+11320+11350+11380+11410+11440+11470+11500+11530+11545+11560+11590+11620+11650+11680+11710+11740+&objL2=&objL3=&objL4=&objL5=&objL6=&objL7=&objL8=&format=json&jsonVD=Y&prdSe=M&newEstPrdCnt=12&orgId=101&tblId=DT_1B040A3'

res = urllib.request.urlopen(url)
res_message = res.read().decode('utf-8')

data = json.loads(res_message)

df = pd.DataFrame(data)

output_file = f'scripts/pythonProject/population/parsed_data/population.csv'

df.to_csv(output_file, index=False)
print(f'{output_file} 저장 완료')

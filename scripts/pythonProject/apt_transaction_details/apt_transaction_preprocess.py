import pandas as pd
import os
import geopandas as gpd
from shapely.geometry import Polygon


os.chdir('C:/Users/N/Projects/dataset/scripts/pythonProject')

apt_trade = pd.read_csv("apt_transaction_details/preprocessed/apart_trade_detail_2020_202405.csv", thousands=',')
apt_rent = pd.read_csv("apt_rent/preprocessed/apart_rent_2020_202405.csv", thousands=',')
off_trade = pd.read_csv("officetel_transaction/preprocessed/officetel_trade_2020_202405.csv", thousands=',')
off_rent = pd.read_csv("officetel_rent/preprocessed/officetel_rent_2020_202405.csv", thousands=',')



#
#
# apt_trade['법정동코드'] = apt_trade['법정동시군구코드'].astype(str) + apt_trade['법정동읍면동코드'].astype(str)
# apt_trade = apt_trade[['거래금액', '거래유형', '건축년도', '전용면적', '법정동', '법정동코드', '아파트', '층', '년', '월', '일']]
#
# legal_geo_info2 = pd.read_csv("address/preprocessed/legal_geo_info2.csv").astype({'법정동코드': str})
#
# # print(apt_trade.dtypes)
# # print(legal_geo_info2.dtypes)
#
# apt_trade_final = pd.merge(apt_trade, legal_geo_info2, on='법정동코드', how='left')
# apt_trade_final = gpd.GeoDataFrame(apt_trade_final)
# apt_trade_final['geometry'] = apt_trade_final['geometry'].apply(lambda x: Polygon(eval(x)))
#
# # print(apt_trade_final.dtypes)
# # print(apt_trade_final.head(3).T)
#
# apt_trade_final = apt_trade_final.reset_index(drop=True)
# apt_trade_final = gpd.GeoDataFrame(apt_trade_final, geometry='geometry')

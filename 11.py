import requests
import xmltodict
import json
from pprint import pprint
import sys
from datetime import datetime, timedelta

api_key = '399a12818bb184fe2a3f0d3c393c10da8f967c234392c801455bb606d426ce6c'

# 조회 가능한 최소 최대 날짜
tday = datetime.today()-timedelta(1)
tday = int(tday.strftime("%Y%m%d")) #tday = 20230325
searchDate = int(sys.stdin.readline())
if searchDate < 20150401 or searchDate > tday:
    print('error')
    sys.exit(0)

# API 요청 보내기
url = f'http://211.237.50.150:7080/openapi/{api_key}/xml/Grid_20180118000000000580_1/1/1?DELNG_DE={searchDate}'

content = requests.get(url).content
dict = xmltodict.parse(content)

#totalCnt = int(dict['Grid_20180118000000000580_1']) #59276

minimum = 1
maximum = 1000

# print(totalCnt) 총 카운트 수 
pprint(dict['Grid_20180118000000000580_1'])
import requests
import xmltodict
import json
from pprint import pprint
import sys
from datetime import datetime, timedelta
import agri_key

api_key = agri_key.key
#pprint(dict['Grid_20141119000000000012_1']['total'])

# 조회 가능한 최소 최대 날짜
tday = datetime.today()-timedelta(1)
tday = int(tday.strftime("%Y%m%d"))
searchDate = int(sys.stdin.readline())
if searchDate < 20180118 or searchDate > tday:              #입력한 날짜에 따라 조회범위에 벗어나면 exit로 종료
    print('error')
    sys.exit(0)
else:
    tday = 20230325
    day = str(tday)[-2:]
    day = int(day)

url = f'http://211.237.50.150:7080/openapi/{api_key}/xml/Grid_20141119000000000012_1/1/1000?AUCNG_DE={searchDate}'
content = requests.get(url).content
dict = xmltodict.parse(content)


totalCnt = totalCnt = int(dict['Grid_20141119000000000012_1']['totalCnt'])  #금일 거래횟수

page_size = 1000                                                            #최대 요청가능한 데이터 1~1000
num_pages = (totalCnt + page_size - 1) // page_size
print(num_pages)
total_price = []

for i in range(num_pages):
    minimum = i * page_size + 1
    maximum = (i + 1) * page_size
    total_url = f'http://211.237.50.150:7080/openapi/{api_key}/xml/Grid_20141119000000000012_1/{minimum}/{maximum}?AUCNG_DE={searchDate}'
    total_content = requests.get(total_url).content
    total_dict = xmltodict.parse(total_content)

    for row in total_dict['Grid_20141119000000000012_1']['row']:
        total_price.append(int(row['AVRG_AMT']))
    
    print(i)

print(total_price)
avg_total_price = sum(total_price) // totalCnt                                #금일 평균 도매가 가격
print(avg_total_price)

"""
백준 4963
import sys
sys.setrecursionlimit(10000)

def dfs(x,y):
if x<0 or x>=h or y<0 or y>=w:
return False

if graph[x][y]==1:
	graph[x][y]=0
	dfs(x-1,y)
	dfs(x+1,y)
	dfs(x,y-1)
	dfs(x,y+1)
	dfs(x-1,y+1)
	dfs(x+1,y-1)
	dfs(x-1,y-1)
	dfs(x+1,y+1)
	return True
return False
while True:
w, h = map(int,input().split())
if h==0 or w==0:
break
graph = []
answer = 0
for i in range(h):
graph.append(list(map(int,input().split())))

for i in range(h):
	for j in range(w):
		if dfs(i,j)==True:
			answer+=1

print(answer)
"""
import requests
import xmltodict
import json
from pprint import pprint
import sys
from datetime import datetime, timedelta
import agri_key

api_key = agri_key.key


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

# API 요청 보내기
url = f'http://211.237.50.150:7080/openapi/{api_key}/xml/Grid_20180118000000000580_1/1/1000?DELNG_DE={searchDate}'
content = requests.get(url).content
dict = xmltodict.parse(content)


totalCnt = totalCnt = int(dict['Grid_20180118000000000580_1']['totalCnt'])  #금일 거래횟수

page_size = 1000                                                            #최대 요청가능한 데이터 1~1000
num_pages = (totalCnt + page_size - 1) // page_size
print(num_pages)
total_price = []

for i in range(num_pages):
    minimum = i * page_size + 1
    maximum = (i + 1) * page_size
    total_url = f'http://211.237.50.150:7080/openapi/{api_key}/xml/Grid_20180118000000000580_1/{minimum}/{maximum}?DELNG_DE={searchDate}'
    total_content = requests.get(total_url).content
    total_dict = xmltodict.parse(total_content)

    for row in total_dict['Grid_20180118000000000580_1']['row']:
        total_price.append(int(row['PRICE']))
    
    print(i)

avg_total_price = sum(total_price) // totalCnt                                #금일 평균 도매가 가격
print(avg_total_price)



"""
while minimum != totalCnt:
    if minimum == maximum:
        minimum = maximum
        maximum += 1000
        total_url = f'http://211.237.50.150:7080/openapi/{api_key}/xml/Grid_20180118000000000580_1/{minimum}/{maximum}?DELNG_DE={searchDate}'
        total_content = requests.get(total_url).content
        total_dict = xmltodict.parse(total_content)
    else:
        for row in total_dict['Grid_20180118000000000580_1']['row']:
            total_price.append(row['PRICE'])
"""

"""
while num!=2:
    print(dict['Grid_20180118000000000580_1']['row'][num]['PRICE'])
    total+=int(dict['Grid_20180118000000000580_1']['row'][num]['PRICE'])
    num+=1
    print(total)


while minimum != totalcnt:
    if minimum == maximum:
        maximum +=1000
    else:
        minimum+=1
    print(minimum)
"""

"""
graph = {'A':['B','C'],
         'B':['A','D','E'],
         'C':['A','G','H'],
         'D':['B'],
         'E':['B','F'],
         'F':['E'],
         'G':['C'],
         'H':['C']}

def dfs(graph ,start_node):
    need_visited, visited = list(),list()
    need_visited.append(start_node)

    while need_visited:
        node = need_visited.pop()
        print(node)
        if node not in visited:
            visited.append(node)
            print(visited)
            need_visited.extend(graph[node])
    
    return visited

print(dfs(graph , 'A'))
"""
import requests,openpyxl,time,json,time
from datetime import datetime, timedelta
from bs4 import BeautifulSoup


#url = 'http://localhost:8085/city/list'
#url = 'http://docker34-wuliu.qipeipu.net/city/list'
#url = 'http://docker34-wuliu.qipeipu.net/city/getById?cityId=1203'

# params = {
#     'current': 1,
#     'size': 10
# }
# headers = {
#     # Content-Type
#     'Content-Type':'application/json',
#     # Cookie
#     'Cookie':'JSESSIONID=92m21p3stn7u1qh8yde157lft'
#     }
# res = requests.post(url,data=json.dumps(params),headers=headers)
# #res = requests.get(url,headers=headers)
# print(res.status_code)
# print(res.text)


# headers = {
#     # Content-Type
#     'Content-Type':'application/json'
#     # Cookie
#     #'Cookie':'JSESSIONID=92m21p3stn7u1qh8yde157lft'
#     }

# url = 'http://localhost:8080/paramTest/format'
# params = {
#     'date': time.time(),
#     'number': '1,234,567.89'
# }
# res = requests.get(url,data=json.dumps(params))
# print(res.status_code)
# print(res.text)

aa='1--2--3'
bb=aa.split('--')
print(type(bb))

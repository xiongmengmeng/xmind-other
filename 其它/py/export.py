import requests,openpyxl,time,json
from datetime import datetime, timedelta
from bs4 import BeautifulSoup

url = 'http://docker34-wuliu.qipeipu.net/freightConfig/exportDispatchFreightConfigList?destWarehouseId=&firstWarehouseId=&provinceId=&cityId=&belongToOrderType=&type=&current=0&size=10'
#url = 'http://docker34-wuliu.qipeipu.net/city/list'
#url = 'http://docker34-wuliu.qipeipu.net/city/getById?cityId=1203'

# params = {
#     'current': 1,
#     'size': 10
# }
headers = {
    #'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Content-Type':'application/octet-stream',
    'Content-Disposition': 'form-data; name="attachment"; filename="运费规则.xls"',
    # Cookie
    'Cookie':'JSESSIONID=8FCE3F5F526CAEE2D664BED3FF97737B'
    }
res = requests.post(url,headers=headers)
#res = requests.get(url,headers=headers)
print(res.status_code)
print(res.text)
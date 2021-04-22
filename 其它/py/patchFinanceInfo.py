import requests,openpyxl,time
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
url = 'http://10.1.2.73:8080/timeCostPatch.jsp'
wb1=openpyxl.load_workbook('c:\\Users\\btr\\Desktop\\data.xlsx')
sheet=wb1['Sheet1']


for i in sheet:
    #使用i[0].value来判断是否有值
    if i[0].value:
        #第i行的第0列单元格内容：i[0].value
        list=i[0].value.split('*')
        print(list[0])
        if(list[0].startswith('BTL')):
            
            continue
        params = {
            'id': 5,
            'packageNo': list[0]
        }
        res = requests.post(url,params=params)
        print(res.status_code)
        bs=BeautifulSoup(res.text,'html.parser')
        info=bs.find('p') 
        print(info.text)
        time.sleep(10)
wb1.close()
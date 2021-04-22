import requests,json,openpyxl,csv
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
HEADERS = {
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
}





#统计下市盈率为正且小于80的公司个数
num=0 
#统计下销售毛利率>30%的公司个数
count=0
#关注名单
attr=[]
#筛选股票所在行业
industry_info={}
#一共196页数据，每页20个,range(1,197)
for i in range(1,197):
    url = 'http://q.10jqka.com.cn/index/index/board/all/field/zdf/order/desc/page/'+str(i)+'/ajax/1/'
    response = requests.get(url,headers=HEADERS)
    soup=BeautifulSoup(response.text,'html.parser')
    temp=soup.find('table',class_='m-table m-pager-table')
    if(temp!=None):
        basees=temp.find_all('tr')
        for j in basees:
            lines=j.find_all('td')
            if(lines!=[]):
                #获得股票编码
                #print(lines[1].text)
                #获得股票名称
                #print(lines[2].text)
                #去掉科创版和ST的股票
                if(lines[1].text.startswith('688') or lines[1].text.startswith('*ST')):
                    break
                #去掉市盈率为亏损的股票
                if(lines[13].text!='亏损' and  lines[13].text!='--' and float(lines[13].text)<80):
                    #打印【公司编码--公司名称--公司市盈率】
                    #print(str(i)+'页的--'+lines[2].text+'--市盈率：'+lines[13].text)
                    num=num+1
                    #用于控制流程
                    flag=False
                    #打印【公司基本信息，如当前股价之类的】
                    # for h in lines:
                    #     print(h.text,end='\t')


                    #查询股票的基本财务数据
                    url_finance='http://basic.10jqka.com.cn/'+lines[1].text+'/finance.html'
                    response = requests.get(url_finance,headers=HEADERS)
                    soup=BeautifulSoup(response.text,'html.parser')
                    item=soup.find('p',id='main')
                    titile=json.loads(item.text)['title']
                    report=json.loads(item.text)['report']
                    #打印出来【比较的数据的日期】，此处是比较2020-06-30的数据
                    #print('\t'+'\t'.join('%s' %id for id in report[0][0:1]))
                    temp=[lines[1].text,lines[2].text,lines[13].text]
                    for m in range(1,16):
                        temp.append(report[m][0])
                        #打印【公司基本财务数据】
                        #对比多数据时：'\t'.join('%s' %id for id in report[m][0:1])
                        #print(titile[m][0]+":\t"+'\t'.join('%s' %id for id in report[m][0:1]))
                        #每股经营现金流>0
                        if(m==11 and type(report[m][0])!=type(True) and float(report[m][0])<0):
                            break
                        #销售净利率>0%
                        if(m==12 and type(report[m][0])!=type(True) and float(report[m][0].strip('%'))<0):
                             break
                        #销售毛利率>30%
                        if(m==13 and type(report[m][0])!=type(True) and float(report[m][0].strip('%'))<40):
                            break
                        #净资产收益率>5%
                        if(m==14 and type(report[m][0])!=type(True) and float(report[m][0].strip('%'))<5):
                            break
                        #净资产收益率-摊薄>5%
                        if(m==15 and type(report[m][0])!=type(True) and float(report[m][0].strip('%'))>5):
                            flag=True
                            count=count+1
                            print(str(i)+'页的--'+lines[2].text+'--市盈率：'+lines[13].text)
                            
                    if flag:
                        #查询股票的财务信息
                        headers_industry = {
                            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                            'Accept-Encoding':'zip, deflate',
                            'Accept-Language':'zh-CN,zh;q=0.9',
                            'Cache-Control':'no-cache',
                            'Connection':'keep-alive',
                            'Cookie':'Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1599306108; reviewJump=nojump; searchGuide=sg; usersurvey=1; spversion=20130314; historystock=002677%7C*%7C000930; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1599379067; v=AuieRsuyI99KLw9bxLKbI05nud35EUwbLnUgn6IZNGNW_YbLSiEcq36F8C3x',
                            'Host':'basic.10jqka.com.cn',
                            'Pragma':'no-cache',
                            'Referer':'http://stockpage.10jqka.com.cn/'+lines[1].text+'/field/',
                            'Upgrade-Insecure-Requests':'1',
                            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
                        }
                        url_field='http://basic.10jqka.com.cn/'+lines[1].text+'/field.html'
                        response = requests.get(url_field,headers=headers_industry)
                        response.encoding = 'gbk' 
                        soup=BeautifulSoup(response.text,'html.parser')
                        p=soup.find('p',class_='threecate fl')
                        industry=p.text.split("：")[1]
                        temp.append(industry)
                        attr.append(temp)
                        print('公司所属行业三级行业分类:'+industry)
                        #industry.split(" -- ")[]
                        
                        if(industry_info !={} and industry in industry_info.keys()):
                            industry_info[industry]=industry_info[industry]+1
                        industry_info[industry]=1
                            




print('市盈率为正且小于80的公司有'+str(num)+'家')
print('销售毛利率>40%的公司有'+str(count)+'家')
#print(attr)
for key,value in industry_info.items():
    print('行业：'+key+'----'+str(value))






wb=openpyxl.Workbook()
sheet=wb.active
sheet.title='new title'
sheet.append(['股票编码',
'股票名称',
'市盈率',
'净利润',
'净利润同比增长率',
'扣非净利润',
'扣非净利润同比增长率',
'营业总收入',
'营业总收入同比增长率',
'基本每股收益',
'每股净资产',
'每股资本公积金',
'每股未分配利润',
'每股经营现金流',
'销售净利率',
'销售毛利率',
'净资产收益率',
'净资产收益率-摊薄',
'行业'])
for i in attr:
    print(i)
    sheet.append(i)
wb.save('c:\\Users\\69505\Desktop\\base.xlsx')
print("数据处理完成 ")





import requests,json,openpyxl,csv,time
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import time
def compare_time(time1,time2):
    s_time = time.mktime(time.strptime(time1,'%Y-%m-%d'))
    e_time = time.mktime(time.strptime(time2,'%Y-%m-%d'))
    return int(s_time) - int(e_time)


HEADERS = {
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
}

def showBasicInfo(lines,num):
    flag=True
    if(lines==[]):
        flag=False
        return flag,num
    #获得股票编码
    #print(lines[1].text)
    #获得股票名称
    #print(lines[2].text)
    #去掉科创版和ST的股票
    if(lines[1].text.startswith('688') or lines[1].text.startswith('*ST')):
        flag=False
        return flag,num
    #去掉市盈率亏损的股票
    if(lines[13].text=='亏损' or  lines[13].text=='--' ):
        flag=False
        return flag,num
    #去掉市盈率大于60的股票
    if(float(lines[13].text)>60):
        flag=False
        return flag,num
    #打印【公司编码--公司名称--公司市盈率】
    #print(str(i)+'页的--'+lines[2].text+'--市盈率：'+lines[13].text)
    num=num+1
    #打印【公司基本信息，如当前股价之类的】
    # for h in lines:
    #     print(h.text,end='\t')
    return flag,num


def showCompanyBasicInfo(lines,flag,temp,statistical_num):
    if(lines==[] or flag==False):
        return flag,statistical_num,temp
    #查询股票的基本数据
    url_base='http://stockpage.10jqka.com.cn/'+lines[1].text+'/'
    response = requests.get(url_base,headers=HEADERS)
    soup=BeautifulSoup(response.text,'html.parser')
    dl=soup.find('dl',class_='company_details')
    dts=dl.find_all('dt')
    dds=dl.find_all('dd')
    #打印【公司基本信息】
    #print('\n打印【公司基本信息】')
    for m in range(0,10):
        #print(str(m)+'--'+dts[m].text+":\t"+dds[m].text)
        if(m==0 ):
            print(dts[m].text+":\t"+dds[m].text)
        # elif(m==1 ):
        #     #print(dts[m].text+":\t"+dds[m]['title'])
        # elif(m==2):
        #     #print(dts[m].text+":\t"+dds[3]['title'])
        elif(m==3):
            datetime.strptime(dds[m+1].text, "%Y-%m-%d")
            print(dts[m].text+":\t"+dds[m+1].text)
            temp.append(str(dds[m+1].text))
            #上市两年内的过滤
            if(int(dds[m+1].text.split("-")[0])>2017):
                flag=False
            else:
                statistical_num=statistical_num+1
    return flag,statistical_num   ,temp  


def showBasicFinanceInfo(lines,flag,count,temp):
    #查询股票的基本财务数据
    if(lines==[] or flag==False):
        return flag,count,temp
    url_finance='http://basic.10jqka.com.cn/'+lines[1].text+'/finance.html'
    response = requests.get(url_finance,headers=HEADERS)
    soup=BeautifulSoup(response.text,'html.parser')
    item=soup.find('p',id='main')
    title=json.loads(item.text)['title']
    report=json.loads(item.text)['report']
    #打印出来【比较的数据的日期】，此处是比较2020-06-30的数据
    #print('\t'+'\t'.join('%s' %id for id in report[0][0:1]))
    for m in range(1,16):
        #兼容新股没有那么多财务数据的情况
        #print(report[m])
        middle=6
        last=10
        if(len(report[m])<6):
            middle=2
            last=2
        elif(len(report[m])<10):
            middle=6
            last=6
        temp.append(report[m][2])
        #打印【公司基本财务数据】
        #对比多数据时：'\t'.join('%s' %id for id in report[m][0:1])
        #print(title[m][0]+":\t"+'\t'.join('%s' %id for id in report[m][0:1]))
        #每股经营现金流>0，时间今年半年报，去年年报
        if(m==11 and type(report[m][0])!=type(True) and float(report[m][0])<0 and type(report[m][2])!=type(True) and float(report[m][2])<0):
            flag=False
            break
        #销售净利率>0%，时间今年半年报，近三年年报
        if(m==12 and type(report[m][0])!=type(True) and float(report[m][0].strip('%'))<0 
        and type(report[m][2])!=type(True) and float(report[m][2].strip('%'))<0
        and type(report[m][middle])!=type(True) and float(report[m][middle].strip('%'))<0
        and type(report[m][last])!=type(True) and float(report[m][last].strip('%'))<0):
            flag=False
            break
        #销售毛利率>30%，时间今年半年报，近三年年报
        if(m==13 and type(report[m][0])!=type(True) and float(report[m][0].strip('%'))<40 
        and type(report[m][2])!=type(True) and float(report[m][2].strip('%'))<40
        and type(report[m][middle])!=type(True) and float(report[m][middle].strip('%'))<40
        and  type(report[m][last])!=type(True) and float(report[m][last].strip('%'))<40):
            flag=False
            break
        #净资产收益率>5%，时间今年半年报，近三年年报
        if(m==14 and type(report[m][0])!=type(True) and float(report[m][0].strip('%'))<10
        and type(report[m][2])!=type(True) and float(report[m][2].strip('%'))<10
        and type(report[m][middle])!=type(True) and float(report[m][middle].strip('%'))<10  
        and type(report[m][last])!=type(True) and float(report[m][last].strip('%'))<10 ):
            flag=False
            break
        #净资产收益率-摊薄>5%，时间今年半年报，近三年年报
        if(m==15 and type(report[m][0])!=type(True) and float(report[m][0].strip('%'))<10
        and type(report[m][2])!=type(True) and float(report[m][2].strip('%'))<10
        and type(report[m][middle])!=type(True) and float(report[m][middle].strip('%'))<10 
        and type(report[m][last])!=type(True) and float(report[m][last].strip('%'))<10):
            flag=False
            break
    if(flag):
        count=count+1
        print(str(i)+'页的--'+lines[1].text+'--'+lines[2].text+'--市盈率：'+lines[13].text)
    return flag,count,temp

def showIndustryInfo(lines,flag,industry_info,temp):
    if(lines==[] or flag==False):
        return attr,industry_info
    #查询股票的财务信息
    headers_industry = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding':'zip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Cache-Control':'no-cache',
        'Connection':'keep-alive',
        'Cookie':'Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1599306108; reviewJump=nojump; searchGuide=sg; usersurvey=1; spversion=20130314; historystock='+lines[1].text+'%7C*%7C000930; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1599379067; v=AuieRsuyI99KLw9bxLKbI05nud35EUwbLnUgn6IZNGNW_YbLSiEcq36F8C3x',
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
    print(str(i)+'页的--'+lines[2].text+'----所属行业三级行业分类:'+industry)
    temp.extend(industry.split(" -- "))
    if(industry_info !={} and industry in industry_info.keys()):
        industry_info[industry]=int(industry_info[industry])+1
    else:
        industry_info[industry]=1
    return attr,industry_info

def showMainBusiness(lines,attr,temp,flag):
    if(lines==[] or flag==False):
        return 
    #公司主营
    headers_main_business = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding':'zip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Cache-Control':'no-cache',
        'Connection':'keep-alive',
        'Cookie':'Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1599306108; reviewJump=nojump; searchGuide=sg; spversion=20130314; historystock='+lines[1].text+'%7C*%7C000930; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1599399866; usersurvey=1; v=AgB2_uPKS5fQIjeTw3ID-xZv0YXRieRThm04V3qRzJuu9a6zIpm049Z9COXJ',
        'Host':'basic.10jqka.com.cn',
        'Pragma':'no-cache',
        'Referer':'http://stockpage.10jqka.com.cn/'+lines[1].text+'/operate/',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
    }
    url_main_business='http://basic.10jqka.com.cn/'+lines[1].text+'/operate.html'
    response = requests.get(url_main_business,headers=headers_main_business)
    response.encoding = 'gbk' 
    soup=BeautifulSoup(response.text,'html.parser')
    business_info=soup.find('ul',class_='main_intro_list')
    if(business_info!=None):
        businesses=business_info.find_all('li')
        temp.append(businesses[0].text)
        print('\n打印【公司主营】')
        for i in range(0,3):
            print(businesses[i].text)
    else:
        temp.append('')
    attr.append(temp)

#统计下市盈率为正且小于60的公司个数
num=0 
#统计下销售毛利率>40%,净资产收益率>10%等的公司个数ip
count=0
#统计三年前上市的公司个数ip
statistical_num=0
#关注名单
attr=[]
#筛选股票所在行业
industry_info={}


#一共196页数据，每页20个,range(1,197)
for i in range(1,197):
    time.sleep(1)
    url = 'http://q.10jqka.com.cn/index/index/board/all/field/zdf/order/desc/page/'+str(i)+'/ajax/1/'
    response = requests.get(url,headers=HEADERS)
    soup=BeautifulSoup(response.text,'html.parser')
    temp=soup.find('table',class_='m-table m-pager-table')
    if(temp!=None):
        basees=temp.find_all('tr')
        for j in basees:
            lines=j.find_all('td')
            baiscInfo=showBasicInfo(lines,num)
            flag=baiscInfo[0]
            num=baiscInfo[1]
            if(lines!=[]):
                #print(str(i)+'页的--'+lines[2].text+'--flag：'+str(flag))
                temp=[lines[1].text,lines[2].text,lines[13].text]
                #查询公司的基本信息
                companyBasicInfo=showCompanyBasicInfo(lines,flag,temp,statistical_num)
                flag=companyBasicInfo[0]
                statistical_num=companyBasicInfo[1]
                #查询股票的基本财务数据
                basicFinanceInfo=showBasicFinanceInfo(lines,flag,count,temp)
                flag=basicFinanceInfo[0]
                count=basicFinanceInfo[1]
                temp=basicFinanceInfo[2]
                #查询股票的财务信息            
                industryInfo=showIndustryInfo(lines,flag,industry_info,temp)
                attr=industryInfo[0]
                industry_info=industryInfo[1]
                #公司主营
                showMainBusiness(lines,attr,temp,flag)
                            




print('市盈率为正且小于60的公司有'+str(num)+'家')
print('销售毛利率>40%的公司有'+str(count)+'家')
print('三年前上市的公司有'+str(statistical_num)+'家')
#print(attr)
for key,value in industry_info.items():
    print('行业：'+key+'----'+str(value))






wb=openpyxl.Workbook()
sheet=wb.active
sheet.title='new title'
sheet.append(['股票编码',
'股票名称',
'市盈率',
'上市时间',
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

'行业一级',
'行业二级',
'行业三级',
'主营'
])
for i in attr:
    # print(i)
    sheet.append(i)
wb.save('c:\\Users\\btr\Desktop\\screeSharesInfo1.xlsx')
print("数据处理完成 ")







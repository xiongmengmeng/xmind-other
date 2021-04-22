import requests,json
from bs4 import BeautifulSoup
HEADERS = {
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
}
#用来查想买的股票信息
infos={'浙江美大':'002677','开能健康':'300272','海大集团':'002311',
'海尔智家':'600690','燕塘乳业':'002732',
'华胜天成':'600410','招商证券':'600999',
'科大讯飞':'002230','三只松鼠':'300783'}
code=infos['浙江美大']






def showBasicInfo(code):
    #查询股票的基本数据
    url_base='http://stockpage.10jqka.com.cn/'+code+'/'
    response = requests.get(url_base,headers=HEADERS)
    soup=BeautifulSoup(response.text,'html.parser')
    dl=soup.find('dl',class_='company_details')
    dts=dl.find_all('dt')
    dds=dl.find_all('dd')
    #打印【公司基本信息】
    print('\n打印【公司基本信息】')
    for m in range(0,10):
        #print(str(m)+'--'+dts[m].text+":\t"+dds[m].text)
        if(m==0 ):
            print(dts[m].text+":\t"+dds[m].text)
        # elif(m==1 ):
        #     #print(dts[m].text+":\t"+dds[m]['title'])
        # elif(m==2):
        #     #print(dts[m].text+":\t"+dds[3]['title'])
        elif(m==3):
            print(dts[m].text+":\t"+dds[m+1].text)
    

        
    span=soup.find('div',class_='analyze-img fl').find_all('span')
    print('\n打印【公司评估】')
    print(span[1].text+"--------------"+span[2].text)
    intro=soup.find('div',class_='analyze-txt f')
    print(intro)
    # for k in intro:
    #     print(k.text)


def showBasicFinanceInfo(code):
    #查询股票的基本财务数据
    print('\n打印【公司基本财务数据】')
    url_finance='http://basic.10jqka.com.cn/'+code+'/finance.html'
    response = requests.get(url_finance,headers=HEADERS)
    soup=BeautifulSoup(response.text,'html.parser')
    item=soup.find('p',id='main')
    titile=json.loads(item.text)['title']
    report=json.loads(item.text)['report']

    for m in range(0,16):
        annualReport=[report[m][0],report[m][2],report[m][6],report[m][10]]
        #打印出来【比较的数据的日期】，此处是比较2020-06-30的数据 '\t'.join('%s' %id for id in report[0][0:1]
        if(m==0):
            print('\t'+'\t'.join('%s' %id for id in annualReport))
        else:
            #打印【公司基本财务数据】
            #对比多数据时：'\t'.join('%s' %id for id in report[m][0:1])
            print(titile[m][0]+":\t"+'\t'.join('%s' %id for id in annualReport))




def showIndustryInfo(code):
    #查询股票的行业数据
    headers_industry = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding':'zip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Cache-Control':'no-cache',
        'Connection':'keep-alive',
        'Cookie':'Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1599306108; reviewJump=nojump; searchGuide=sg; usersurvey=1; spversion=20130314; historystock=002677%7C*%7C000930; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1599379067; v=AuieRsuyI99KLw9bxLKbI05nud35EUwbLnUgn6IZNGNW_YbLSiEcq36F8C3x',
        'Host':'basic.10jqka.com.cn',
        'Pragma':'no-cache',
        'Referer':'http://stockpage.10jqka.com.cn/'+code+'/field/',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
    }
    url_field='http://basic.10jqka.com.cn/'+code+'/field.html'
    response = requests.get(url_field,headers=headers_industry)
    response.encoding = 'gbk' 
    soup=BeautifulSoup(response.text,'html.parser')
    #print(soup.text)
    p=soup.find('p',class_='threecate fl')
    print('\n打印【公司行业】')
    print('公司所属行业三级行业分类:'+p.text.split("：")[1])


def showMainBusiness(code):
    #公司主营
    headers_main_business = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding':'zip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Cache-Control':'no-cache',
        'Connection':'keep-alive',
        'Cookie':'Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1599306108; reviewJump=nojump; searchGuide=sg; spversion=20130314; historystock=002677%7C*%7C000930; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1599399866; usersurvey=1; v=AgB2_uPKS5fQIjeTw3ID-xZv0YXRieRThm04V3qRzJuu9a6zIpm049Z9COXJ',
        'Host':'basic.10jqka.com.cn',
        'Pragma':'no-cache',
        'Referer':'http://stockpage.10jqka.com.cn/'+code+'/operate/',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
    }
    url_main_business='http://basic.10jqka.com.cn/'+code+'/operate.html'
    response = requests.get(url_main_business,headers=headers_main_business)
    print(response.status_code)
    response.encoding = 'gbk' 
    soup=BeautifulSoup(response.text,'html.parser')
    business_info=soup.find('ul',class_='main_intro_list')
    if(business_info!=None):
        businesses=business_info.find_all('li')
        print('\n打印【公司主营】')
        for i in range(0,3):
            print(businesses[i].text)

                    



showBasicInfo(code)
showBasicFinanceInfo(code)
showIndustryInfo(code)
showMainBusiness(code)






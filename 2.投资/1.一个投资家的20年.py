import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="一个投资家的20年"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("一个投资家的20年")
r2=s2.getRootTopic()
r2.setTitle("一个投资家的20年")


content={
'衡量投资成功的三个标准':[
    '跑赢大市',
    '绝对盈利',
    '解决问题'
],
'市场':[
    '不要去预测市场',
    '不要太关注宏观经济：例2020',
    '二八法则：八成的时间不赚钱，二成时间在营利',
    '仓位'
],
'信息':[
    '信息并不重要',
    '重要是的解析信息的能力'
],
'卖出的三个理由':[
    '目标公司本身运营恶化',
    '价格高估',
    '有更好的选择'
],
'心态':[
    '关注价值，而不是价格',
    '盈亏自负，愿赌服输',
    '在正确的方向上忍耐',
    '内心的淡定与从容'
],
'目标':[
    '财务健康标准：财产性收入超过日常工作所得'
    '追求长久的存在',
    '在有限的时间与精力内：',
    '学习可以学习的',
    '努力可以努力的',
    '帮助可以帮助的',
    '得到可以得到的'
],
'其它':[
    {'幸福感':[
        '降低欲望',
        '提升财富'
    ]},
    {'书籍推荐':[
        '手把手教你读财报',
        '...2:18节课看透银行业',
        '投资中最简单的事',
        '投资中最重要的事'
    ]}
]



}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
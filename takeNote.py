import os,sys 
# parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
# sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="takeNote"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("takeNote")
r2=s2.getRootTopic()
r2.setTitle("方格笔记")


content={
'目的':[
    '再现学习思考过程',
    '有框架，格式加深记忆'
],
'基本原则':[
    '大小：A4',
    '颜色: 不超过三种,记录用蓝色，结论用红色',
    '题目: 一页一主题，写重点',
    '大量书写，大量舍弃'
],
'记忆性笔记本':[
    '板书->发现->总结',
    {'上方':[
        '左：标题',
        '右：重点'
    ]},
    {'左侧':[
        '用眼方式'
    ]},
    {'中间':[
        '发现部分',
        '将发现故事化',
        '逻辑连接词',
        '注重理解力',
        '提问能力'
    ]},
    {'右侧':[
        '概括能力',
        '关注重点'
    ]}
],
'工作笔记本':[
    {'目的':[
        '面对海量信息，如何做出取舍'
    ]},
    '记笔记->舍弃->得出一个结论',
    {'措施':[
        '提高提问力,确认论点',
        '确认论点(目的与意义),例PRD'
    ]}
],
'提案笔记本':[
    ''
]
}
#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
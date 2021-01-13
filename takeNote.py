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
'记忆性笔记本：板书->逻辑->总结':[
    {'上方':[
        '左：标题',
        '右：重点'
    ]},
    {'左侧:记忆图片':[
        '用眼方式'
    ]},
    {'中间:梳理逻辑':[
        '发现部分',
        '将发现故事化',
        '逻辑连接词',
        '注重理解力',
        '提问能力'
    ]},
    {'右侧:概括，得出重点':[
        '概括能力',
        '关注重点'
    ]}
],
'工作笔记本：信息->舍弃->结论':[
    {'目的':[
        '面对海量信息，如何做出取舍'
    ]},
    {'措施':[
        '提高提问力,确认论点',
        '确认论点(目的与意义),例PRD'
    ]}
],
'提案笔记本:事实->本质->行动':[
    {'左边：准确设定论点':[
        '基于事实思考问题',
        '区分事实与意见'
    ]},
    {'中间：挖掘本质问题':[
        '逻辑连接词+三种箭头',
        '边问五个为什么'
    ]},
    {'右边：明确提出行动':[
        '将结论提炼为一个信息->少即是多',
        '基于行动的思考法->用看得见的词语来表达具体行动'  
    ]}
],
'博弈笔记本:结论先行，辅以图表':[
    '目的：记忆->思考->整理思考->向他们传达想法',
    {'重点':[
        '信息为先，先传达结论',
        {'图表(能给人心理冲击的)':[
            '对比',
            '瀑布(舍弃，集中，增加)',
            {'金字塔效果':[
                '目标->',
                '实现目标的三个重点->',
                '完成三个重点应采取的行动'
            ]},
            '高楼效果'
        ]}
    ]}
]
}
#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
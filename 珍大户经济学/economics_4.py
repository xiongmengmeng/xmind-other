
import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="economics"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("economics4")
r2=s2.getRootTopic()
r2.setTitle("第三讲：经济学的核心逻辑--番外")

#xmind内容
content={
'周期':[
    '供需变动对均衡的影响',
    {'猪周期':[
        'S1->S2,猪瘟',
        'S2->S3,扩大产能',
        '每个上升或下降周期约8-15个月',
        '同样的还有石油和新能源汽车'
    ]},
    '经济周期',
    {'三大指标':[
        'CPI:消费者价格指数',
        'PPI:生产者价格指数，与货币政策有关',
        {'PMI':[
            '采购经理人指数',
            {'注意':[
                '高于50，还是低于50',
                '连续',
                '注意夸张数值'
            ]},
            {'意义':[
                '提前发布',
                '非常详尽'
            ]},
            '缺点:不准确'
        ]}
    ]}
],
'用供需原理思考':[
    {'要不要买车位':[
        '1.是否有替代品',
        '2.车位配比<1:1,值得买',
        '车位配比>1:1.5,不值得买',
        '车位配比1:1--1:1.5,综合考虑',
        {'思考':[
            '1.一次性买入小区车位，控制小区车位配比到1:0.5',
            '2.开发商一开始就这样销售'
        ]}
    ]},
    {'商业计划书/企业线路':[
        {'三十而已':[
            '1.基层:拼业绩',
            '2.中层：员工激励',
            '3.高层：收缩与扩张',
            '总之：站在公司角度，思考外界变化原因，提出对策'
        ]},
        {'风口':[
            '需求曲线大幅右移，而市场上竞争对手很少',
            '抢占先机->市场份额'
        ]},
        {'思考':[
            '自上而下，行业->公司->个人',
            {'行业现状':[
                {'总需求现状':[
                    '消费者收入分析',
                    '用户人数，结构',
                    '消费者喜好变化',
                    '替代品和互补品分析'
                ]},
                {'总供给现状':[
                    '外界资源变化',
                    '技术分析',
                    '竞争对手数量',
                    '外部政策分析'
                ]}
            ]},
            {'公司层面':[
                'ALL IN or 活下去',
            ]},
            {'个人':[
                '投资:ALL IN or 活下去',
                '工作:继续或换行业'
            ]}
        ]}
    ]},
    {'青春期如何安稳度过':[
        '这个时期个人比较注重与群体的关系',
        '考虑打造稀缺性'
    ]},
    {'什么时候租房最划算':[
        '11月下旬-次年2月'
    ]},
    {'考什么证书':[
        '对比会计跟律师的职业',
        '汽车牌照'
    ]}
]

}

#构建xmind
xmind.build(content,r2)
topics=r2.getSubTopics()
for topic in topics:
    topic.addMarker(MarkerId.starBlue)

#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
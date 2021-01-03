
import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="economics"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("economics3")
r2=s2.getRootTopic()
r2.setTitle("第三讲：经济学的核心逻辑")

#xmind内容
content={
'需求':[
    {'需求量':[
        '在某个价格下，消费者愿意且能够购买的某种商品或服务的数量',
        {'两个条件':[
            '购买意愿',
            '购买能力'
        ]},
        '例：作者的课，整理师,人保养车券，苹果手机的价值'
    ]},
    {'需求定理':[
        '需求与价格成反向关系',
        '在保持其他因素不变的条件下：',
        '当一种商品价格升高，需求量减少',
        '当一种商品价格下降，需求量增加'
    ]},
    {'需求曲线':[
        '需求量的变化：价格'
    ]},
    {'需求曲线移动':[
        {'1.收入变化':[
            '收入增加:增加对优质品的消费',
            '减少对劣质品的消费'
        ]},
        '2.替代品:猪肉，鸡肉',
        {'3.互补品':[
            '护肤品销售',
            '衣服搭配',
            '菜单'
        ]},
        {'4.人的变化':[
            '户籍制度',
            '麦当劳',
            '高尔夫球场'
        ]},
        {'5.消费者对未来的预期':[
            '购房'
        ]},
        {'6.消费者的喜好，偏好的变化--营销':[
            '冲牙器',
            '电动牙刷'
        ]}
    ]}
],
'供给':[
    {'供给量':[
        '在某个价格下，卖家愿意且能够出售的某种商品或服务的数量',
        {'两个条件':[
            '供给意愿',
            '供给能力'
        ]},
    ]},
    {'供给定理':[
        '需求与价格成正向关系',
        '在保持其他因素不变的条件下：',
        '当一种商品价格升高，供给量增加',
        '当一种商品价格下降，供给量减少'
    ]},
    {'供给曲线':[
        '供给量的变化：价格',
        '例：原油产量，可开采数量是随价格变化的'
    ]},
    {'供给曲线移动':[
        {'1.投入资源的价格变化':[
            '资源：原材料，人力，租金'
        ]},
        {'2.技术因素':[
            '页岩气石油成本,智能指纹锁',
            '技术提升,供给曲线右移，价格下降'
        ]},
        '3.同一生产线或生产流程下的相关产品',
        {'4.厂商数目':[
            '例：手机'
        ]},
        '5.预期',
        {'6.其它因素':[
            '政策法规变化：去产能，供给曲线左移',
            '税收',
            '政治环境',
            '国际关系'
        ]}
    ]}
],
'均衡价格':[
    '看不见的手：价格对市场资源进行调节的一种机制',
    {'1.供需交汇':[
        '均衡价格'
    ]},
    {'2.价格调节':[
        '过剩或短缺'
    ]},
    {'3.形成均衡':[
        '对工业品:价格升高，吸引外界资源，价格下降',
        '对于医疗资源呢？是否应该涨价'
    ]}, 
    {'4.变动':[
        'D,S均右移，数量上升，价格不确定',
        'D,S均左移，数量下降，价格不确定',
        'D右移，S左移，价格上升，数量不确定',
        'D左移，S右移，价格下降，数量不确定'
    ]},
    {'思考':[
        '1.石油什么时候枯竭',
        '2.82年拉菲什么时候喝完',
        '3.美国感染人数上升，医疗资源什么时候被挤兑',
        '均衡价格一定好吗',
        '市场调节一定好吗'
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
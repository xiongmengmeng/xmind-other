
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
r2.setTitle("第四讲：消费者选择模型")

#xmind内容
content={
'消费者是如何选择的':[
    '把有限的钱分配到无限的欲望中'
],
'消费者做选择的三个因素':[
    {'购买意愿':[
        '消费者偏好->效用',
    ]},
    {'购买能力':[
        '商品价格',
        '消费者收入'
    ]}
],
'效用':[
    {'1.效用':[
        '消费者的满足程度',
        '个人之间无法被衡量与比较'
    ]},
    {'2.总效用':[
        '简单：数量*效用',
        '实际：积分'
    ]},
    {'3.边际效用':[
        '增加一份带来的额外效用',
        '思考边际效用是否是递减的',
        '集物品，连环杀人犯',
        {'征税':[
            {'目的':[
                '1.提供公共服务',
                '2.提供福利，缩小贫富差距',
            ]},
            {'制度':[
                '累退税率制',
                '累进税率制'
            ]}
        ]}
    ]}
],
'思考':[
    {'社会走向':[
        '边际效用递减',
        '商品社会变化不大',
        '生产力提升',
        '->综上，社会会走向产能过剩吗，会通货膨胀吗'
    ]},
    {'乌托邦是可能存在的吗':[
        '仅依靠善良来改变社会，唤起社会良知，维护社会运转',
        ''
    ]},
    {'':[
        '',
        ''
    ]},
    {'':[
        '',
        ''
    ]},
    {'':[
        '',
        ''
    ]},
    {'':[
        '',
        ''
    ]},
]


}

#构建xmind
xmind.build(content,r2)
topics=r2.getSubTopics()
for topic in topics:
    topic.addMarker(MarkerId.starBlue)

#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
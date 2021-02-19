
import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="finance"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("利润表--分析")
r2=s2.getRootTopic()
r2.setTitle("利润表--分析")

#xmind内容
content={
'营业收入':[
    '展示企业经营状况和发展趋势',
    '选择过去增长，现在增长，预计在可见未来继续保持增长的企业',
    {'收入增长的三种途径':[
        '潜在需求增长：可靠性最高',
        '市场份额扩大：评估竞争对手的反击力度及反击下增长的可持续性',
        '价格提升：评估的是消费的替代性强弱'
    ]},
    {'注意':[
        '绝对数的增长',
        '增速是否高于行业平均水平'
    ]}
],
'毛利率':[
    '=(营业收入-营业成本)/营业收入',
    '高：公司的产品具有很强的竞争优势，其替代品较少或替代的代价很大'
],
'费用率':[
    '=(销售费用+管理费用+财务费用)/营业总收入',
    '用来排除企业',
    {'销售费用高,企业扩张':[
        '扩大生产能力',
        '配套新的团队、资金和促销方案',
        '对企业的管理能力边界要求极高'
    ]},
    '管理费用:增长比例等于或小于营业收入增长',
    {'费用占毛利润的比例':[
        '<30%：优秀的企业',
        '30%～70%：有一定竞争优势的企业',
        '>70%:忽略'
    ]}
],
'营业利润率':[
    '=营业利润/营业收入',
    {'营业利润率上升':[
        '售价提升:思考提价会不会导致市场份额的下降',
        '成本下降：思考成本是全行业一起降了，还是该公司独降，原因，一次性还是持续',
        '费用控制得力：思考有没有伤及公司团队战斗力，一次性还是永久性的费用减少'
    ]}
],
'确认净利润是否变成现金回到公司账户':[
    '经营现金流净额/净利润>1,优秀企业'
]

}

#构建xmind
xmind.build(content,r2)
topics=r2.getSubTopics()
for topic in topics:
    topic.addMarker(MarkerId.starBlue)

#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
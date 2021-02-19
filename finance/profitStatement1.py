
import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="finance"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("利润表")
r2=s2.getRootTopic()
r2.setTitle("利润表")

#xmind内容
content={
'P（股价）=PE（市盈率）×E（每股收益）':[
],
'净利润的产生过程':[
    {'1.从营业收入到营业利润的过程':[
        {'营业总收入':[
            {'营业收入':[
                '满足以下条件时确认”进行搜索，能够找到该公司对收入的确认原则',
                {'三种途径':[
                    '销售商品',
                    '提供劳务',
                    '让渡资产使用权（现金、无形资产、固定资产等）'
                ]}
            ]},
            '利息收入',
            '已赚保费',
            '手续费及佣金收入'
        ]},
        {'营业总成本':[
            {'营业成本':[
                '销售产品的存货价值',
                '毛利润:主营业务收入减去营业成本',
                '毛利率:毛利润占主营业务收入的比例',
                {'提高原因':[
                    '成本下降',
                    '售价的上升'
                ]}
            ]},
            '营业税金及附加',
            '营业费用（销售费用、管理费用和财务费用）',
            '资产减值损失:一般很小'
        ]},
        {'其他收益':[
            '公允价值变动收益',
            '投资收益',
            '汇兑收益'
        ]},
        {'营业利润':[
            '=营业总收入-营业总成本-其他收益',
            '看营业利润及营业利润率的历史变化趋势，以及与同行业其他公司进行对比',
        ]}
    ]},
    {'2.从营业利润到净利润的变化':[
        {'净利润':[
            '=营业利润加上营业外收支净额，缴纳了所得税',
            '净利润≠挣到钱',
            '要和现金流量表的“经营现金流净额”对照看',
            '“经营现金流净额÷净利润”来衡量净利润的含金量'
        ]},
        {'企业最终利润的高低由三个因素决定':[
            '毛利率高低--“茅台模式”--产品竞争力强弱',
            '周转率快慢--“沃尔玛模式”--管理层运营能力的高低',
            '经营杠杆大小--“银行模式”--企业承担的风险大小',
        ]}
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
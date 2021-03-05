import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="容貌研究"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("容貌研究")
r2=s2.getRootTopic()
r2.setTitle("容貌研究")


content={
'脸':[
    '区分人的脸，是通过比较来进行学习的',
    '脸的魅力：健康且生机勃勃->年轻的肌肤',
    '改变眉毛倾斜和位置，脸的各感官配置都会看上去不同',
    '为脸部魅力做贡献的，是遍布脸部的肌肉',
    '左右对称脸被视为无重大疾病的标志'
],
'脸的社交性':[
    {'杏仁核':[
        '杏仁核对恐惧做出反应',
        '被重要对象背叛或伤害是一种巨大的恐惧->',
        '会对大脑造成损害，让杏仁核过度反应或变小',
        '青少年恐惧感淡薄，与杏仁核未发育成熟有关'
    ]},
    {'记脸诀窍':[
        '利用情感来激活大脑',
        '记忆笑脸的人名，使用眶额皮层处理正面信息',
        '记忆不可信的人，使用岛叶皮质处理负面信息'
    ]},
    {'婴儿记脸':[
        '4个月前，通过眼镜，发型来认脸',
        '7个月，可区别喜怒等基本表情',
        '8个月后，认脸能力与成人基本相同',
        '10月，婴儿可通过观察母亲神色来决定自己的行为'
    ]}

],
'眼睛':[
    {'成年人无法凝视':[
        '因为观察脸或视线时，伴随着情感',
        '情感会随着成长变得越来越复杂'
    ]}
],
'表情':[
    '交流的原点',
    '与情感紧密相连',
    '表情魅力：微笑'

]

}
#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
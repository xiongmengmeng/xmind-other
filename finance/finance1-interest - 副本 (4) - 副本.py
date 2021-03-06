
import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="finance"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("财务是个真实的谎言")
r2=s2.getRootTopic()
r2.setTitle("财务是个真实的谎言")

#xmind内容
content={
'':[
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
],
'':[
    '',
    '',
    '',
    '',
    ''
],
'':[
    '',
    '',
    '',
    '',
    ''
],
'':[
    '',
    '',
    '',
    '',
    ''
],
'':[
    '',
    '',
    '',
    '',
    ''
]
}

#构建xmind
xmind.build(content,r2)
topics=r2.getSubTopics()
for topic in topics:
    topic.addMarker(MarkerId.starBlue)

#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
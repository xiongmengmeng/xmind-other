import xmind
from xmind.core.const import TOPIC_DETACHED
from xmind.core.markerref import MarkerId

# load an existing file or create a new workbook if nothing is found
w = xmind.load("c:\\Users\\btr\\Desktop\\test.xmind") 


# create a new sheet 创建新工作表
# s2=w.createSheet()
s1=w.getPrimarySheet() 
s2.setTitle("redis")
r2=s2.getRootTopic()
r2.setTitle("redis")

# Create a topic with a link to the first sheet given by s2.getID()
t1 = r2.addSubTopic()
t1.setTopicHyperlink(s2.getID()) 
t1.setTitle("数据结构") # set its title

# Create a topic with a hyperlink 使用超链接创建主题
t2 = r2.addSubTopic()
t2.setTitle("事务")
#t2.setURLHyperlink("https://xmind.net") 

# Create a topic with notes 用笔记创建主题
t3 = r2.addSubTopic()
t3.setTitle("管道")
# t3.setPlainNotes("notes for this topic") 
# t3.setTitle("topic with \n notes")

# Create a topic with a file hyperlink
t4 = r2.addSubTopic()
#t4.setFileHyperlink("logo.jpeg") 
t4.setTitle("lua表达式")

# Create topic that is a subtopic of another topic
t41 = t1.addSubTopic()
t41.setTitle("string")

# create a detached topic whose (invisible) parent is the root 创建一个分离的主题，其（不可见的）父级是根
# d1 = r2.addSubTopic(topics_type = TOPIC_DETACHED)
# d1.setTitle("detached topic")
# d1.setPosition(0,20)

# loop on the (attached) subTopics
topics=r2.getSubTopics()
# Demonstrate creating a marker 给节点增加图像
for topic in topics:
    topic.addMarker(MarkerId.starBlue)
    


# and we save
xmind.save(w,"c:\\Users\\btr\\Desktop\\test2.xmind") 

import xmind
from xmind.core.markerref import MarkerId
w = xmind.load("c:\\Users\\btr\\Desktop\\englishPrefix.xmind") 
s2=w.createSheet()
s2.setTitle("前缀")
r2=s2.getRootTopic()
r2.setTitle("前缀")


content={
'1. a-':[
    '1.在…，…的:akin[əˈkɪn]a. 同族的（a+kin亲属）',
    '2.表加强:afresh[əˈfreʃ]ad. 再；重新（a+fresh新鲜的）',
    '3.不，无，非:apathy[ˈæpəθi]n. 冷漠（a+pathy感情）'
],
'2. ab-, abs-':[
    '1.相反：absent[ˈæbsənt]a. 缺席的（abs+ent存在→不在→缺席的）',
    '2.去掉，离去：abject[ˈæbdʒekt]a. 可怜的（ab+ject扔→被人扔掉→可怜的）'
],
'3. ab-, ac-, af-, ag-, ap-, ar-, as-, at-':[
    '加在同辅音字母的词根前，表加强',
    'affiliation[əˌfɪliˈeɪʃn]n. 入会，加入（af+fili子女+ation表结果→成为子女→入会）',
    'accentuate[əkˈsentʃueɪt]v. 强调（ac+cent唱歌+uate使…→不停地唱→强调）'
],
'4. ad-':[
    '表示“做…”或加强',
    'adapt[əˈdæpt]v. 适应（ad+apt适应）',
    'admonish[ədˈmɒnɪʃ]v. 告诫，警告（ad+mon警告+ish使…→一再警告→告诫）'
],
'5. an-':[
    '1.在…，…的',
    '2.表加强'
],
'6. ant-, anti-':[
    '相反；反对；抗'
],
'7. be-':[
    '1.构成动词，使…',
    '2.构成介词',
    '3.加以…，饰以…'
],
'8. bi-, bin-':[
    '二，两'
],
'9. by-':[
    '在旁边；副的'
],
'10. circum-':[
    '环绕，周围'
],
'11. co-, col-':[
    '共同'
],
'12. com-, con-, cor-':[
    '共同',
    '表加强'

],
'13. contra-':[
    '反对；相反；对比',
    'contradict[ˌkɒntrəˈdɪkt]v. 同…矛盾（contra+dict说→反着说→同…矛盾）'
],
'14. counter-':[
    '反对，相反',
    'counteract[ˌkaʊntərˈækt]v. 对抗；抵消（counter+act行动→反对的行动→对抗）'
],
'15. de':[
    '去掉；取消；毁',
    '否定，非；相反',
    '向下；降低，减少',
    '离开',
    '使…加强'
],
'16. di-':[
    '二，两',
    '使…分开，离开'
],
'17. dif-（在同辅音词根前）':[
    '不，否定',
    '分开'
],
'18. dis-':[
    '不，没有',
    '除去；剥夺',
    '分开，分离（有时也作di-）',
    '表示“完全地；加强”，用在含有',
    '“分开；否定”等意义的单词前'
],
'19. e-':[
    '出，外',
    '无；除去',
    '表加强或引申'
],
'20. eco-':[
    '生态；经济',
    'ecosystem[ˈiːkəʊsɪstəm]n. 生态系统（eco+system系统）',
    'ecotourism[ˈiːkəʊtʊərɪzəm]n. 生态旅游（eco+tourism旅游）'
],
'21. em-, en-':[
    '进入…之中；包围',
    '使…',
    '用…做某事；加以…，饰以…'
],
'22. ex-':[
    '出，出去',
    '前面的，前任的',
    '使…；做…；加强'
],
'23. extra-, extro-':[
    '超过；以外'
],
'24. fore-':[
    '前面；预先'
],
'25. il-':[
    '（放在同辅音词根前）不，无',
    '向内；进入',
    '表加强或引申'
],
'26. im-, in-':[
    '不，无，非',
    '向内；进入',
    '使…；加以…；饰以…'
],
'27. inter-':[
    '在…之间',
    'intercede[ˌɪntəˈsiːd]v. 调停（inter+ced走+e→在两者之间走〔防止发生冲突〕→调停）',
    'interrogate[ɪnˈterəɡeɪt]v. 审问；询问（inter+rog问+ate→一问一答→询问）'
    '相互',
    'interrelate[ˌɪntərɪˈleɪt]v. 相互关联（inter+relate关联）',
    'interact[ˌɪntərˈækt]v. 相互作用（inter+act行动→互动→相互作用）'
],
'28. intro-':[
    '向内，入内'
],
'29. ir-':[
    '（放在同辅音词根前）不，无',
    '向内，进入',
    '表加强'
],
'30. kilo-':[
    '千',
    'kilogram[ˈkɪləɡræm]n. 千克（kilo+gram克）',
    'kilometer[ˈkɪləmiːtə(r)]n. 千米（kilo+meter米）'
],
'31. magn(i)-':[
    '大',
    'magnate[ˈmæɡneɪt]n. 巨头，权贵（magn+ate表人）',
    'magnify[ˈmæɡnɪfaɪ]v. 放大（magni+fy使…→使…大→放大）'
],
'32. mis-':[
    '错误；坏',
    'misuse v.[ˌmɪsˈjuːz] n. [ˌmɪsˈjuːs]误用；虐待（mis+use用',
    'misapprehend[ˌmɪsæprɪˈhend]v. 误解（mis+apprehend理解）'
],
'33. non':[
    '-不，非'
],
'34. ob-, op-':[
    '逆，倒；反对，否定',
    '表加强'
],
'35. out-':[
    '太，过分',
    '出，外',
    '超过，胜过'
],
'36. over-':[
    '过度，过分',
    '在…之上，凌驾',
    '翻转'
],
'37. per-':[
    '贯穿，自始至终',
    'permanent[ˈpɜːmənənt]a. 永久的（per+man逗留+ent具有…性质的→始终留在那里→永久的）',
    'persist[pəˈsɪst]v. 坚持（per+sist站→一直站着→坚持）',
    'perspire[pəˈspaɪə(r)]v. 出汗（per+spir呼吸+e→全身呼吸→出汗）',
    '表加强',
    'perplexed[pəˈplekst]a. 困惑的（per+plex重叠+ed→全部重叠在一起、让人感觉混乱的→困惑的）',
    'peremptory[pəˈremptəri]a. 不容反抗的；专横的（per+empt拿+ory…的→全部拿走的→专横的）',
    '假；坏；否定',
    'perverse[pəˈvɜːs]a. 堕落的（per+vers转+e→转向坏的方面→堕落的）'
],
'38. post-':[
    '后，后面',
    '邮政'
],
'39. pre-':[
    '前；预先',
    'preclude[prɪˈkluːd]v. 妨碍；阻止（pre+clud关闭+e→在前面关闭→阻止）',
    'precaution[prɪˈkɔːʃn]n. 预防措施；预防（pre+caution小心→预先小心→预防）'
],
'40. pro-':[
    '向前，在前',
    '赞同；亲…，拥护',
    '代理，代替'
],
'41. re-':[
    '回；向后',
    'regress[rɪˈɡres]v. 倒退（re+gress走）',
    'retract[rɪˈtrækt]v. 缩回；收回（re+tract拉→拉回→缩回）',
    '相反；反对；不',
    'rebel[ˈrebl]v. 反叛（re+bel战斗→反过来打〔自己人〕→反叛）',
    'resist[rɪˈzɪst]v. 反抗，抵抗（re+sist站）',
    '一再，重新',
    'reassure[ˌriːəˈʃʊə(r)]v. 消除（某人）疑虑（re+assure放心→一再让人放心→消除（某人）疑虑）',
    ''
],
'42. se-':[
    '分开，离开'
],
'43. step-':[
    '后，继或前夫（妻）所生',
    'stepfather[ˈstepfɑːðə(r)]n. 继父（step+father父亲）',
    'stepdaughter[ˈstepdɔːtə(r)]n. 前夫或前妻所生之女（step+daughter女儿）'
],
'44. sub-':[
    '① 下',
    'subway[ˈsʌbweɪ]n. 地铁；地道（sub+way路）',
    '次，亚',
    'subtropics[ˌsʌbˈtrɒpɪks]n. 亚热带（sub+tropics热带',
    '副；分支；下级',
    'subordinate[səˈbɔːdɪnət]n. 下属（sub+ordin顺序+ate表人→顺序在下级→下属）',
    '稍，略，微',
    'subacid[sʌbˈæsɪd]a. 略酸的（sub+acid酸）',
    ' 接近，靠近',
    'suburb[ˈsʌbɜːb]n. 市郊（sub+urb城市）',
    '再，更',
    'sublet[ˌsʌbˈlet]v. 转租（sub+let出租）'
],
'45. suc-, suf-, sup-在同辅音词根前':[
    '下'
],
'46. super-':[
    '超，超级',
    'superlative[suˈpɜːlətɪv]a. 最佳的（super+lat拿出+ive…的→拿出超好的→最佳的）',
    'supernova[ˌsuːpəˈnəʊvə]n. 超新星（super+nova新星）'
    '过多，过分',
    'supercharge[ˌsuːpəˈtʃɑːdʒ]v. 使负载过重（super+charge负荷）',
    '上',
    'supersede[ˌsuːpəˈsiːd]v. 淘汰；取代（super+sed坐+e→坐在上面→取代）',
    'supervise[ˈsuːpəvaɪz]v. 监视（super+vis看+e→在上面〔往下〕看→监视）'
],
'47. sur-':[
    '上；超；外加',
    '（常在同辅音词根前）下'
],
'48. sus-':[
    '下，后'
],
'49. trans-（在s之前为tran-）':[
    '横过，越过',
    '变换，转移'
],
'50. tri-':[
    '三',
    'triple[ˈtrɪpl]a. 三倍的（tri+ple…倍的）',
    'tripod[ˈtraɪpɒd]n. 三脚架（tri+pod脚）'
],
'51. twi-':[
    '二，两',
    'twilight[ˈtwaɪlaɪt]n. 黎明；黄昏（twi+light光→黑白光交替→黎明）'
],
'52. un-':[
    '不，无，没有',
    'unbiased[ʌnˈbaɪəst]a. 没有偏见的（un+biased有偏见的）',
    '打开，解开，弄出',
    'unbind[ʌnˈbaɪnd]v. 解开（un+bind捆）',
    'unbutton[ˌʌnˈbʌtn]v. 解开纽扣（un+button纽扣）'
],
'53. under-':[
    '在…下或内',
    'underwear[ˈʌndəweə(r)]n. 内衣（under+wear穿',
    '不足，不够',
    'underdress[ˌʌndəˈdres]v. 穿得太单薄（under+dress穿衣）',
    'underrate[ˌʌndəˈreɪt]v. 对…评价过低（under+rate评估）',
    '副，次',
    'underwork[ˌʌndəˈwɜːk]n. 次要工作（under+work工作）'
],
'54. up-':[
    '上，向上'
],
'55. vice-':[
    '副，次'
],
'56. with-':[
    '向后；相反'
]
}

for key in content:
    t1 = r2.addSubTopic()
    t1.setTopicHyperlink(s2.getID()) 
    list=key.split(":")
    t1.setTitle(list[0])
    if len(list)>1:
        t1.setPlainNotes(list[1]) 
    # print(content[key])
    for i in content[key]:
        # print(type(i))
        if(type(i).__name__=='dict'):
            for t in i:
                t2 = t1.addSubTopic()
                t2.setTopicHyperlink(t1.getID()) 
                t2.setTitle(t)
                for j in i[t]:
                    #print(j)
                    if(type(j).__name__=='dict'):
                        for h in j:
                            t3 = t2.addSubTopic()
                            t3.setTopicHyperlink(t2.getID()) 
                            t3.setTitle(h) 
                            for m in j[h]:
                                if(type(m).__name__=='dict'):
                                    for n in m:
                                        t4 = t3.addSubTopic()
                                        t4.setTitle(n) 
                                        for l in m[n]:
                                            if(type(l).__name__=='dict'):
                                                for k in l:
                                                    t5 = t4.addSubTopic()       
                                                    t5.setTitle(k)
                                                    for p in l[k]:
                                                        if(type(p).__name__=='dict'):
                                                            for u in p:
                                                                t6 = t5.addSubTopic()
                                                                t6.setTitle(u)
                                                                for y in p[u]:
                                                                    if(type(y).__name__=='dict'):
                                                                        for a in y:
                                                                            t7 = t6.addSubTopic()
                                                                            t7.setTitle(a)
                                                                            for b in y[a]:
                                                                                t8 = t7.addSubTopic()
                                                                                t8.setTitle(b)
                                                                    else:
                                                                        t7 = t6.addSubTopic()
                                                                        t7.setTopicHyperlink(t2.getID()) 
                                                                        t7.setTitle(y)              
                                                        else:
                                                            t6 = t5.addSubTopic()
                                                            t6.setTopicHyperlink(t2.getID()) 
                                                            t6.setTitle(p)                                                        
                                            else:
                                                t5 = t4.addSubTopic()
                                                t5.setTopicHyperlink(t3.getID()) 
                                                t5.setTitle(l) 
                                else:
                                    t4 = t3.addSubTopic()
                                    t4.setTopicHyperlink(t3.getID()) 
                                    t4.setTitle(m) 
                    else:
                        t3 = t2.addSubTopic()
                        t3.setTopicHyperlink(t2.getID()) 
                        t3.setTitle(j) 
        else:
            t2 = t1.addSubTopic()
            t2.setTopicHyperlink(t1.getID()) 
            t2.setTitle(i) 



topics=r2.getSubTopics()
for topic in topics:
    topic.addMarker(MarkerId.starBlue)

xmind.save(w,"c:\\Users\\btr\\Desktop\\englishPrefix.xmind") 
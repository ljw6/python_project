import pandas as pd
import json
import jieba
import collections
df = pd.read_csv('tensent_news.csv',encoding='gb18030')
df =df.astype(str)
title = df['标题']
lable = df['标签']
all_list=[]
stopwords={}.fromkeys(['的','，','了','我','你','他','“','”'])
for x in range(len(lable)):
    if lable[x] == "F":
        alist = []
        m = jieba.cut_for_search(title[x])
        for mm in m:
            if mm == ";":
                continue
            elif mm not in stopwords:
                all_list.append(mm)
word_count = collections.Counter(all_list)
top20 = word_count.most_common(20)
top20.reverse()
dic = {}
for i in top20:
    dic[i[0]]=i[1]

with open("news_title.json","w",encoding="utf8") as f:
    json.dump(dic,f,ensure_ascii=False)
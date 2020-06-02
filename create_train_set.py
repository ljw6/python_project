import csv
import pandas as pd
import jieba
import json
with open("news_title.json",encoding='utf8') as f:
    x = json.load(f)
    f.close()
dic = x
df = pd.read_csv("tensent_news.csv",encoding='gb18030')
df =df.astype(str)
title = df['标题']
lable = df['标签']
all_list=[]
stopwords={}.fromkeys(['的','，','了','我','你','他','“','”'])
for x in range(len(lable)):
    alist = []
    m = jieba.cut_for_search(title[x])
    for mm in m:
        if mm == ";":
            continue
        elif mm not in stopwords:
            alist.append(mm)
    all_list.append(alist)

key_list=list(dic.keys())
k_list=[]
for i in range(len(all_list)):
    m = all_list[i]
    v_list=[]
    v_list.append(title[i])
    if lable[i]=="T":
        v_list.append(1)
    else:
        v_list.append(0)
    for mm in range(len(key_list)):
        if key_list[mm] in m:
            k = key_list[mm]
            weight = dic[k]
            v_list.append(weight)
        else:
            v_list.append(0)
    k_list.append(v_list)
def write():
    with open("news_train.csv","w",newline='',encoding='gb18030') as ff:
        headers = ['标题','标签']+key_list
        f_csv = csv.writer(ff)
        f_csv.writerow(headers)
def add_csv(list):
    with open("news_train.csv", "a", newline='',encoding='gb18030') as f:
        f_csv = csv.writer(f)
        f_csv.writerows(list)
write()
add_csv(k_list)
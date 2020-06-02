import numpy as np
import json
import jieba
with open("news_title.json",encoding='utf8') as f:
    x = json.load(f)
    f.close()
dic = x
keys=list(dic.keys())
#载入训练好的参数
w = np.load('weight.npy')
b = np.load('intercept.npy')
stopwords={}.fromkeys(['的','，','了','我','你','他','“','”'])
def check(st):
    k_list=[]
    s = jieba.cut_for_search(st)
    for m in s:
        if m == ';':
            continue
        elif m not in stopwords:
            k_list.append(m)
    return k_list
def proces(srt):
    x_lable=[]
    list = check(srt)
    for i in keys:
        if i in list:
            x_lable.append(dic[i])
        else:
            x_lable.append(0)
    y = np.matmul(x_lable,w)+b
    f = abs(y-1)
    if f <0.5:
        s = "妥妥的正宗新闻！"
    elif f < 0.7:
        s ="可能是标题党，请注意！"
    else:
        s ="小心标题党！！！"
    return s
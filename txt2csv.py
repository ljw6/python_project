import csv
import re
csv_list=[]
n_csv=[]
headers=['序号','分类','内容','字数']

# patten=r'(^[0-9][\uff0c]$)|(^[\u4e00-\u9fa5][\uff0c]$)|(^[0-9][\n]$)'
patten=r'(^[0-9])(?=([,]))'
patten1=r'([\u4e00-\u9fa5]|[\u3002\uff1b\uff0c\uff1a\u201c\u201d\uff08\uff09\u3001\uff1f\u300a\u300b]*)(?=([,]))'
patten2=r'[,\n]'

with open("G:\BaiduNetdiskDownload\souhu\sohu_train.txt","r") as f:
    try:
        for i in range(7000):
            x=f.readlines(32)
            csv_list.append(x)
    except:
        print("没有数据了")
        f.close()
csv_list.pop(0)
for indexs in range(len(csv_list)):
    s=csv_list[indexs][0]
    lists=[]
    while True:
        m=re.search(patten2,s)
        if m==None:
            break
        else:
            print(m.span())
            index=m.span()[0]
            lists.append(s[:index])
            s=s[index+1:]
    n_csv.append(lists)


with open("souhu_news.csv","w",newline='') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(n_csv)
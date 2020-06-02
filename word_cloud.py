import wordcloud as wc
import jieba as jb
import collections
import matplotlib.pyplot as plt
import matplotlib.gridspec as gs
import numpy as np
from PIL import Image as im
import csv
def main():
    with open("tensent_news.csv","r",encoding="gb18030") as f:
        f_csv = csv.reader(f)
        lists=[]
        for row in f_csv:
            x = jb.cut(row[3])
            # k_list = []
            for m in x:
                if m == ';':
                    continue
                else:
                    #k_list.append(m)
                    lists.append(m)
    word_counts = collections.Counter(lists) # 对分词做词频统计
    word_counts_top10 = word_counts.most_common(10) # 获取前10最高频的词
    word_counts_low10 = word_counts.most_common()[:-10:-1]
    mask=np.array(im.open("mask.png"))
    wcc=wc.WordCloud(font_path=r"C:\Windows\Fonts\simhei.ttf",mask=mask,max_words=2000,height=800,width=800,background_color='white',repeat=False)
    cc = wcc.generate_from_frequencies(word_counts)
    key = []
    val = []
    for m in word_counts_top10:
        key.append(m[0])
        val.append(m[1])
    colors = ['#ff0000','#cc9900','#ffff66','#663399','#66ff99','#339933','#ccffff','#003300','#cc6699','#000000']
    plt.figure(figsize=(8,6))
    gr =gs.GridSpec(1,2,width_ratios=[3,1])
    ax1 = plt.subplot(gr[0])
    ax1.imshow(cc)
    ax1.axis("off")
    ax0 = plt.subplot(gr[1])
    ax0.pie(val,labels=key,colors=colors,shadow=True)
    ax0.set(title="新闻热点top10")
    plt.axis("off")
    plt.show()
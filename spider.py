from lxml import etree
from fake_useragent import UserAgent
import urllib.parse as urllib
import urllib.request as urllib2
import json
import random
import re
import os
import datetime
import csv
import requests
def req(url,n):
    ua = UserAgent()
    ualist = []
    for i in range(10):
        ualist.append(ua.random)
        ual = random.choice(ualist)
    #ual='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3947.100 Safari/537.36'
    headers = {
        'User-Agent': ual
    }
    # res = requests.get(url,headers=headers)
    # res.encoding='gbk'
    # dom = etree.HTML(res.content)
    # linkji=dom.xpath("//div[@class='detail']/h3/a/@href")
    # titleji=dom.xpath("//div[@class='detail']/h3/a/text()")
    # patten=r'(?!(^((https|http|ftp|rtsp|mms)?:\/\/)[^\s]+))'
    reqest = urllib2.Request(url)
    result = urllib2.urlopen(reqest)
    resultji = json.loads(result.read())
    data=resultji['data']
    linkji = []
    titleji = []
    keywordsji = []
    categoryji = []
    for d in data:
        urls=d['vurl']
        titles = d['title']
        keywords = d['keywords']
        category = d['category_chn']
        linkji.append(urls)
        titleji.append(titles)
        keywordsji.append(keywords)
        categoryji.append(category)
    lists=[]
    for i in range(len(linkji)):
        s=''
        v_list=[]
        ress=requests.get(linkji[i],headers=headers)
        ress.encoding='gb18030'
        doms = etree.HTML(ress.text)
        contextji = doms.xpath("//div [@class='content-article']//p/text()|//div [@class='content-article']//p/strong/text()")
        for m in range(len(contextji)):
            s=s+contextji[m]
        v_list.append(str(n)+str(i+1)+'B')
        v_list.append(categoryji[i])
        v_list.append(titleji[i])
        v_list.append(keywordsji[i])
        v_list.append(s)
        if s == '':
            continue
        else:
            lists.append(v_list)
    return lists
##https://pacaio.match.qq.com/irs/rcd?cid=146&token=49cbb2154853ef1a74ff4e53723372ce&ext=lifes&page=6
def construct_url(page,key):
    url_list=[]
    for p in range(1,page+1):
        data={}
        data['cid']='146'
        data['token']='49cbb2154853ef1a74ff4e53723372ce'
        data['ext']=key
        data['page']=p
        url_values= urllib.urlencode(data)
        url='https://pacaio.match.qq.com/irs/rcd'+'?'+url_values
        url_list.append(url)
    return url_list
def write_csv():
    headers=['序号','主题','标题','关键词','内容']
    with open("tensent_news.csv", "w", newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
def add_csv(list):
    with open("tensent_news.csv", "a", newline='',encoding='gb18030') as f:
        f_csv = csv.writer(f)
        f_csv.writerows(list)
keylist = ['lifes','health','history']
for i in range(len(keylist)):
    print("写入{}中".format(i))
    key = keylist[i]
    urls = construct_url(35,key)
    for index in range(len(urls)):
        list = req(urls[index],index)
        add_csv(list)
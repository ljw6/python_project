from lxml import etree
import matplotlib.pyplot as plt
import simplejson as json
from matplotlib import gridspec
from matplotlib.font_manager import FontProperties
import numpy as np
import requests
font = FontProperties(fname=r"c:\windows\fonts\simhei.ttf", size=15)
def charts(cites,confirm,nowconfirm,suspect,dead,heal,pathname,total,totalconfirm):
    xlocation =  np.linspace(1, len(confirm) * 0.6, len(confirm)) 
    bar_width = 0.1
    plt.figure(figsize=(20, 8), dpi=80)
    confirmnum=plt.bar(xlocation+0.15,confirm, width=bar_width, label="确诊病例", color='#87CEFA')
    suspectnum=plt.bar(xlocation+0.25,suspect, width=bar_width, label="疑似病例", color='#ADFF2F')
    deadnum=plt.bar(xlocation+0.35,dead, width=bar_width, label="死亡病例", color='#FFD700')
    healnum=plt.bar(xlocation+0.45,heal, width=bar_width, label="治愈病例", color='#FFFACD')
    nowconfirmnum = plt.bar(xlocation+0.55,nowconfirm,width=bar_width,label="现存确诊",color='#FF0000')
    plt.xticks(xlocation+0.2,cites,fontsize=12,rotation=20)
    plt.xlabel('城市', fontsize=15, labelpad=10)
    plt.ylabel('病例数', fontsize=15, labelpad=10)
    for cn,sn,dn,hn,ncn,con,sun,den,hen,necn in zip(confirmnum,suspectnum,deadnum,healnum,nowconfirmnum,confirm,suspect,dead,heal,nowconfirm):
        h01 = cn.get_height()
        h02 = sn.get_height()
        h03 = dn.get_height()
        h04 = hn.get_height()
        h05 = ncn.get_height()
        plt.text(cn.get_x(), h01, con, fontsize=13, va ='bottom',rotation=20) 
        plt.text(sn.get_x(), h02, sun, fontsize=13, va ='bottom',rotation=20) 
        plt.text(dn.get_x(), h03, den, fontsize=13, va ='bottom',rotation=20) 
        plt.text(hn.get_x(), h04, hen, fontsize=13, va ='bottom',rotation=20)
        plt.text(ncn.get_x(),h05, necn, fontsize=13,va='bottom',rotation=20)
    plt.legend(loc=5)
    plt.title(pathname+"疫情"+"确诊总数"+str(total)+"\t"+"现存确诊"+str(totalconfirm))
    plt.show()
def userinput(province,kw):
    return province.index(kw)
def search(kw):
    url="https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5"
    headers = {
            'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }
    res=requests.post(url,headers,verify=False)
    text=res.text
    strtext=text.replace('\\"',"\'")
    ntext=json.loads(strtext)
    data=ntext['data']
    data=data.replace('\'','\"')
    data=json.loads(data)
    chinaTotal=data['chinaTotal']
    chinaTotalcofirm=chinaTotal['confirm']
    chinaTotalsuspect=chinaTotal['suspect']
    chinaTotaldead=chinaTotal['dead']
    chinaTotalheal=chinaTotal['heal']
    chinaAdd=data['chinaAdd']
    chinaAddconfirm=chinaAdd['confirm']
    chinaAddsuspect=chinaAdd['suspect']
    chinaAdddead=chinaAdd['dead']
    chinaAddheal=chinaAdd['heal']
    areatext=data['areaTree']
    area=areatext[0]
    province=area['children']
    provincelist=[]
    for pro in province:
        provincename=pro['name']
        provincelist.append(provincename)
    proindex=userinput(provincelist,kw)
    countries=province[proindex]['children']
    provinceTotal=province[proindex]['total']
    provincecofirm=provinceTotal['confirm']
    provincenowconfirm=provinceTotal['nowConfirm']
    cites=[]
    citesconfirm=[]
    citesnowconfirm=[]
    citessuspect=[]
    citesdead=[]
    citesheal=[]
    for cou in countries:
        # countriesrows=[]
        countriesname=cou['name']
        countriesTotal=cou['total']
        countriescofirm=countriesTotal['confirm']
        countriesnowconfirm = countriesTotal['nowConfirm']
        countriessuspect=countriesTotal['suspect']
        countriesdead=countriesTotal['dead']
        countriesheal=countriesTotal['heal']
        countrieshealRate=countriesTotal['healRate']
        countriesdeadRate=countriesTotal['deadRate']
        cites.append(countriesname)
        citesconfirm.append(countriescofirm)
        citesnowconfirm.append(countriesnowconfirm)
        citessuspect.append(countriessuspect)
        citesdead.append(countriesdead)
        citesheal.append(countriesheal)
    charts(cites,citesconfirm,citesnowconfirm,citessuspect,citesdead,citesheal,kw,provincecofirm,provincenowconfirm)
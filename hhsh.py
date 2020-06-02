#https://lab.magiconch.com/api/nbnhhsh/guess

import json
import requests
import re
def con_dic(cont):
    dic = {"text":cont}
    return dic
def req(cont):
    data = con_dic(cont)
    url ="https://lab.magiconch.com/api/nbnhhsh/guess"
    headers={'Content-Type': 'application/json'}
    response = requests.post(url=url, headers=headers, data=json.dumps(data))
    return response
def test(con):
    patten = r'\"([^\"]*)\"'
    x = req(con)
    x.encoding = "gb2132"
    context = x.text
    m = re.compile(patten)
    result = m.findall(context)
    r_dic={result.pop(0):result.pop(0),result.pop(0):result}
    return r_dic
def process(con):
    m = test(con)
    name = m["name"]
    result = m["trans"]
    return name,result
import datetime
import time
import requests
import json
from selenium import webdriver
import random

def get_time_interval():
    a = datetime.now()  # 获得当前时间
    time.sleep(22)  # 睡眠两秒
    b = datetime.now()  # 获取当前时间
    durn = (b - a).seconds  # 两个时间差，并以秒显示出来
    print(durn)

def today_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
def today_date():
    return time.strftime("%Y-%m-%d", time.localtime(time.time()))
def log_time():
    return "[" +today_time()+ "] "
def print_str(str):
    print(log_time() + str)

def create_counter_page():
    def increase():
        n = 0
        while True:
            n = n + 1
            yield n

    it = increase()
    def counter():
        return next(it)
    return counter

def create_counter():
    def increase():
        n = 5
        while True:
            n = n + 5
            yield n

    it = increase()
    def counter():
        return next(it)
    return counter

def counter_demo():
    _counter = create_counter() # 重置
    print_str(str(_counter())) # 每调用一次_counter()，递增一次
    print_str(str(_counter()))

    _counter = create_counter() # 重置
    print_str(str(_counter()))
    print_str(str(_counter()))
    print_str(str(_counter()))


def post(url, param):
    #jsoninfo = json.dumps(dict)  # 输出str类型
    #dictinfo = json.loads(json_str)  # 输出dict类型

    #url = 'http://beta.napi.huayunquan.com/basic/whbj/simplePublishForPython'
    # paramTest = {"goodsName": "测试1",
    #              "goodsWight": "31",
    #              "deliCity": "辽宁省,抚顺市",
    #              "arriCity": "黑龙江省,大庆市",
    #              "remark": "参考价格:160元,发布时间:1分钟前",
    #              "reptileUrl": "https://www.weihuabiaoju.com/ptnpc/index.html#/goodsdetail?gsid=5402533403",
    #              "reptileSource": "危化镖局"}
    res = requests.post(url, json=param)  # 接口调用
    resTest = json.loads(res.text)  # 将返回结果str转成dict
    # {'code': 0, 'message': 'Success', 'data': None}
    #print(resTest)
    return resTest['code']


def get_browser():
    option = webdriver.ChromeOptions()

    # 设置IP代理
    # thisapi = 'http://ip.ipjldl.com/index.php/api/entry?method=proxyServer.hdtiqu_api_url&packid=1&fa=0&groupid=0&fetch_key=&time=1&qty=19&port=1&format=txt&ss=1&css=&dt=&pro=&city=&usertype=4'
    # ippools = urllib.request.urlopen(thisapi).read().decode("utf-8", "ignore")
    # ipchoose = random.choice(ippools.split("\r\n"))
    # print("======== IP代理：" + ipchoose)
    # option.add_argument("--proxy-server="+ipchoose)

    # 设置用户代理
    uapools = [
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 QIHU 360EE",
    ]
    thisua = random.choice(uapools)
    option.add_argument("User-Agent="+thisua)

    path = r"huayunquanx"
    #option.add_argument('user-data-dir=%s' % path)
    option.add_argument('log-level=3')
    option.add_argument('disable-gpu')
    browser = webdriver.Chrome("../chromedriver.exe", options=option)
    return browser

def replace(str):
    str.replace("-| ", ",")


import re
if __name__ == '__main__':
    #counter_demo()
    content = '30吨'
    result = re.search('(\d+)', content).group()
    weight = "10吨".replace("吨", "")
    print(result)


    i=0



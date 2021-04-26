import requests
import json
import os

COOKIES = ""
cookies = {}

rollChance = 0
remainCoin = 0
Share = False

def split_cookie():
    list = COOKIES.split("; ")
    for data in list:
        key = data.split('=', 1)[0]
        value = data.split('=', 1)[1]
        cookies[key] = value

def roll():
    url = "https://ak.hypergryph.com/activity/preparation/activity/roll"
    response = requests.post(url, cookies = cookies)
    result = json.loads(response.text)
    return result['data']['coin']

def userInfo():
    global rollChance
    global remainCoin
    global Share
    url = "https://ak.hypergryph.com/activity/preparation/activity/userInfo"
    response = requests.get(url, cookies= cookies)
    result = json.loads(response.text)
    rollChance = result['data']['rollChance']
    remainCoin = result['data']['remainCoin']
    if(result['data']['share'] == 'true'):
        Share = True
    print("当前拥有「美味值」*%s，剩余获得「调色奶油袋」次数*%s"%(remainCoin, rollChance))

def share():
    url = "https://ak.hypergryph.com/activity/preparation/activity/share"
    requests.post(url, cookies= cookies)

def exchange():
    pass

if __name__ == '__main__':
    COOKIES: str = os.environ.get('COOKIES', None)
    split_cookie()
    userInfo()
    while rollChance:
        rollChance = rollChance-1
        print("获得「调色奶油袋」，助力收集「原料数」*10，「美味值」+%s，剩余获得次数*%s"%(roll(),rollChance))
    if Share:
        share()
        print("今日首次分享页面，助力收集「原料数」*10")
    userInfo()

# 由于上不了豆瓣 故只能爬百度首页的数据
from bs4 import BeautifulSoup
import requests
import time
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
    'host': 'www.baidu.com'
}
links = 'https://www.baidu.com'
response = requests.get(links, headers=headers,verify=False)
soup = BeautifulSoup(response.text, 'html.parser')
# 参考https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/#id48
aim_list=soup.find_all(attrs={"class" :'title-content-title'})
# 日期
day_time=time.strftime("%Y-%m-%d", time.localtime())
print('---------%s------------\n'%(day_time))
for i,x in enumerate(aim_list):
    with open('./baidu.txt','a+',encoding='utf-8') as f:
        if(i==0):
            f.write('\n---------%s------------\n'%(day_time))
        f.write('%s. %s\n'%(i+1,x.get_text()))
    print('%s. %s\n'%(i+1,x.get_text()))
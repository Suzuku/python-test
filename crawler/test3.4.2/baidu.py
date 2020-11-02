# 由于上不了豆瓣 故只能爬百度首页的数据
from bs4 import BeautifulSoup
import requests
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
    'host': 'www.baidu.com'
}
links = 'https://www.baidu.com'
response = requests.get(links, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
# 参考https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/#id48
aim_list=soup.find_all(attrs={"class" :'title-content-title'})
for i,x in enumerate(aim_list):
    print('%s. %s\n'%(i+1,x.get_text()))
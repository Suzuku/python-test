import requests
from lxml import etree
import json
from queue import Queue
import threading
 
class Qsbk(object):
  def __init__(self):
    self.headers = {
      "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
      "Referer": "https://www.qiushibaike.com/"
    }
    # 实例化三个队列，用来存放内容
    self.url_queue = Queue()
    self.html_queue = Queue()
    self.content_queue = Queue()
 
  def get_total_url(self):
    """
    获取了所有的页面url，并且返回url_list
    return:url_list
    现在放入url_queue队列中保存
    """
    url_temp = "https://www.qiushibaike.com/text/page/{}/"
    url_list = list()
    for i in range(1,13):
      # url_list.append(url_temp.format(i))
      # 将生成的url放入url_queue队列
      self.url_queue.put(url_temp.format(i))
 
  def parse_url(self):
    """
    发送请求，获取响应，同时etree处理html
    """
    while self.url_queue.not_empty:
      # 判断非空，为空时结束循环
 
      # 从队列中取出一个url
      url = self.url_queue.get()
      print("parsing url:",url)
      # 发送请求
      response = requests.get(url,headers=self.headers,timeout=10)
      # 获取html字符串
      html = response.content.decode()
      # 获取element类型的html
      html = etree.HTML(html)
      # 将生成的element对象放入html_queue队列
      self.html_queue.put(html)
      # Queue.task_done() 在完成一项工作之后，Queue.task_done()函数向任务已经完成的队列发送一个信号
      self.url_queue.task_done()
 
  def get_content(self):
    """
    解析网页内容，获取想要的信息
    """
    while self.html_queue.not_empty:
      items = list()
      html = self.html_queue.get()
      total_div = html.xpath("//div[@class='col1 old-style-col1']/div")
      for i in total_div:
 
        author_img = i.xpath(".//a[@rel='nofollow']/img/@src")
        author_img = "https"+author_img[0] if len(author_img)>0 else None
 
        author_name = i.xpath(".//a[@rel='nofollow']/img/@alt")
        author_name = author_name[0] if len(author_name)>0 else None
 
        author_href = i.xpath("./a/@href")
        author_href = "https://www.qiushibaike.com/"+author_href[0] if len(author_href)>0 else None
 
        author_gender = i.xpath("./div[1]/div/@class")
        author_gender = author_gender[0].split(" ")[-1].replace("Icon","").strip() if len(author_gender)>0 else None
 
        author_age = i.xpath("./div[1]/div/text()")
        author_age = author_age[0] if len(author_age)>0 else None
 
        content = i.xpath("./a/div/span/text()")
        content = content[0].strip() if len(content)>0 else None
 
        content_vote = i.xpath("./div[@class='stats']/span[@class='stats-vote']/i/text()")
        content_vote = content_vote[0] if len(content_vote)>0 else None
 
        content_comment_numbers = i.xpath("./div[@class='stats']/span[@class='stats-comments']/a/i/text()")
        content_comment_numbers = content_comment_numbers[0] if len(content_comment_numbers)>0 else None
 
        item = {
          "author_name":author_name,
          "author_age" :author_age,
          "author_gender":author_gender,
          "author_img":author_img,
          "author_href":author_href,
          "content":content,
          "content_vote":content_vote,
          "content_comment_numbers":content_comment_numbers,
        }
        items.append(item)
      self.content_queue.put(items)
      # task_done的时候，队列计数减一
      self.html_queue.task_done()
 
  def save_items(self):
    """
    保存items
    """
    while self.content_queue.not_empty:
      items = self.content_queue.get()
      with open("quishibaike.txt",'a',encoding='utf-8') as f:
        for i in items:
          json.dump(i,f,ensure_ascii=False,indent=2)
      self.content_queue.task_done()
 
  def run(self):
    # 获取url list
    thread_list = list()
    thread_url = threading.Thread(target=self.get_total_url)
    thread_list.append(thread_url)
 
    # 发送网络请求
    for i in range(10):
      thread_parse = threading.Thread(target=self.parse_url)
      thread_list.append(thread_parse)
 
    # 提取数据
    thread_get_content = threading.Thread(target=self.get_content)
    thread_list.append(thread_get_content)
 
    # 保存
    thread_save = threading.Thread(target=self.save_items)
    thread_list.append(thread_save)
 
 
    for t in thread_list:
      # 为每个进程设置为后台进程，效果是主进程退出子进程也会退出
      t.setDaemon(True)
      t.start()
     
    # 让主线程等待，所有的队列为空的时候才能退出
    self.url_queue.join()
    self.html_queue.join()
    self.content_queue.join()
 
 
if __name__=="__main__":
  obj = Qsbk()
  obj.run()

# 打印结果如下，主线程和子线程的先后是没有关系的，各自执行
import threading
import time

def thread_print(index,content):
    print('Thread %s start!'%(index))
    time.sleep(1)
    print(content)
    time.sleep(1)
    print('Thread %s end!'%(index))



print('Main thread start！')

thread_list=[]
for i in range(2):
    t=threading.Thread(target=thread_print,args=(i,'name %s'%(i)))
    t.start()
    thread_list.append(t)

for t in thread_list:
    t.join()
print('Main thread end！')

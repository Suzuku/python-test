import time
import threading

# 假定这是你的银行存款:
balance = 0


def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(100000):
        print('Thread %s is running >>%s' %
              (threading.current_thread().name, balance))
        change_it(n)


t1 = threading.Thread(target=run_thread, args=(5,), name='22')
t2 = threading.Thread(target=run_thread, args=(8,), name='33')
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

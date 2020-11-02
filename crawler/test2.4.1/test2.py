# 将符号变为空格  Python在for循环中直接修改列表元素值无效，需要用到索引
import re
str='你好$$$我正在学Python@#@#现在需要&*&*&修改字符串'

def replace(str):
    for x in str:
        if re.match(r'^[\$\#\@\&\*]+$',x):
            print(x)
            x=' '

replace(list(str))
print(str)
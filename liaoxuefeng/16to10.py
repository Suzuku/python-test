

# 整型会自己转为16进制。。下面来试试字符串
def transform(strArgs):
    counter=0
    strSlice=strArgs[2:]
    strAgainst=strSlice[::-1]
    for index,item in enumerate(strAgainst):
        counter+=int(item)*pow(16,index)
    print(counter)    

transform('0x7000')


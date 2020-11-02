# 打印9*9乘法表
def multiplication():
    for x in range(1,10):
        for j in range(1,10):
            print('%s * %s = %s'%(x,j,x*j))

multiplication()
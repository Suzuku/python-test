fpath = 'D:/Code-test/python/read.txt'


with open(fpath, 'a') as f:
    f.write('\n hello Ada')


with open(fpath, 'r')as f:
    str = f.read()
    print(str)

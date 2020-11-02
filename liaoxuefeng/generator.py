import sys
L = range(10)
g = (x*x for x in L)
for x in range(6):
    print(next(g))


print(sys.executable)

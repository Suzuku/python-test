
def odd(x):
    return x%2!=1

L=filter(odd,range(10))
print(list(L))
import time, functools

def metric(fn):
    print('%s executed in %s ms' % (fn.__name__, 10.24))
    return fn
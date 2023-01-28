import time

def cal_t(method):
    start_time = time.time()
    m = 2451966000072168
    n = 485897929014301292
    result = method(m, n)
    elapsed_time = time.time()-start_time
    print(f'Method : {str(method)}, Result : {result}, elapsed time : {elapsed_time:.10f}')

def gcd1(x, y):
    if x < y:
        x, y = y , x

    if y == 0:
        return x

    if x % y == 0:
        return y

    else:
        return gcd1(y, x % y)

    
def gcd2(x, y):
    while y != 0:
        t = x % y
        (x, y) = (y, t)
    return abs(x)

def gcd3(x, y):
    if y == 0:
        return x

    mod = x % y

    if mod != 0:
        x, y = y, mod
        return gcd4(x, y)
    
    else:
        return y


def gcd4(x, y):
    while y != 0:
        if x < y:
            x, y = y, x

        if y == 0:
            return x

        if x % y == 0:
            return y




methods = [gcd1, gcd2, gcd3, gcd4]

for m in methods:
    cal_t(m)
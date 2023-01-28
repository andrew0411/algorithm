import random

# N이 소수인지 판별하는 것인지
# N 이하의 소수가 몇 개인지 구하는 것인지
# N 이하의 소수를 모두 구하는 것인지


# 에라토스테네스의 체
# 거의 선형시간의 시간 복잡도 O(nlog(logn))

def prime_array(n):
    Sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m+1):
        if Sieve[i]:
            for j in range(i+1, n, i):
                Sieve[j] = False
    
    return [i for i in range(2, n) if Sieve[i]]


# 에라토스테네스의 체 - 짝수 제거 version
def prime_array(n):
    Sieve = [False] + [True] * (n // 2)
    for i in range(1, len(Sieve)):
        if Sieve[i]:
            print(2*i+1)
            for j in range(i + (2 * i + 1), len(Sieve), 2 * i + 1):
                Sieve[j] = False


# 거듭제곱 소수 판별
def isPrime(n):
    if n == 1:
        return 0
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return 0
    return 1
        
# 밀러-라빈 판별

def powmod(a,b,m):
    result = 1
    while b > 0:
        if b % 2 != 0:
            result = (result * a) % m
        b //= 2
        a = (a * a) % m

    return result

def mr(n,a):
    r = 0
    d = n-1
    while (d%2 == 0):
        r += 1
        d = d // 2
    x = powmod(a,d,n)
    if x == 1 or x == n-1:
        return True
    for i in range(0,r-1):
        x = powmod(x,2,n)
        if x == n-1:
            return True
    return False
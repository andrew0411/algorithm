a, b = map(int, input().split())

if b >= 10000000:
    b = 10000000


def isPalindrome(n):
    return str(n) == str(n)[::-1]

primes = [False] + [True] * (b//2)
for i in range(1, len(primes)):
    if primes[i]:
        if i*2+1>=a and isPalindrome(i*2+1):
            print(2*i + 1)
        for j in range(i + (2*i+1), len(primes), 2*i+1):
            primes[j] = False
print(-1)
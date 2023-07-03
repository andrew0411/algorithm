a = int(input())
if a % 2:
    print(f'{a} is odd')
else:
    print(f'{a} is even')

'''
파이썬 비트 연산자!

n & 1 -> 양의 정수의 짝수 홀수 판별
      -> n % 2 보다 효율이 좋다

1<<n  -> 2^n 을 계산하는 것보다 성능이 좋음
'''
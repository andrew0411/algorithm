import sys

input = sys.stdin.readline
n = list(map(int, input().split()))
if n == [i for i in range(1, 9)]:
    print('ascending')
elif n == [8-i for i in range(8)]:
    print('descending')
else:
    print('mixed')
        
    
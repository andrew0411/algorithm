import sys

input = sys.stdin.readline

N = int(input())

cnt = 1
num = 666

while cnt <= N:
    if '666' in str(num):
        cnt += 1
    num += 1
print(num - 1)
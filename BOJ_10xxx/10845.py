import sys

input = sys.stdin.readline

n = int(input())

que = []

for i in range(n):
    s = input().split()

    if s[0] == 'push':
        que.append(s[1])

    elif s[0] == 'pop':
        if que:
            print(que.pop(0))
        else:
            print(-1)

    elif s[0] == 'size':
        print(len(que))

    elif s[0] == 'empty':
        print(0) if que else print(1)

    elif s[0] == 'front':
        if que:
            print(que[0])
        else:
            print(-1)

    elif s[0] == 'back':
        if que:
            print(que[-1])
        else:
            print(-1)
import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    N = int(input())
    temp = []
    for i in range(N):
        temp.append(tuple(map(int, input().split())))
    temp.sort()
    cnt = 0
    ref = temp[0][1]
    for i in temp:
        if i == temp[0]:
            cnt += 1
        elif i[1] < ref:
            cnt += 1
            ref = i[1]
    print(cnt)
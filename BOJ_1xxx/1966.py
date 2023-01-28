import sys

input = sys.stdin.readline

cases = int(input())

result = []

for case in range(cases):
    n, m = map(int, input().split())
    cnt = 0
    imp = list(map(int, input().split()))
    que = [(idx, i) for idx, i in enumerate(imp)]

    while True:
        if que[0][1] == max(que, key=lambda x:x[1])[1]:
            cnt += 1
            if que[0][0] == m:
                result.append(cnt)
                break
            else:
                que.pop(0)
        else:
            que.append(que.pop(0))

print(*result, sep='\n')
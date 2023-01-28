import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
order = deque(list(map(int, input().split())))

que = deque([i for i in range(1, n+1)])

cnt = 0
while True:
    if len(order) > 0:
        if que[0] == order[0]:
            order.popleft()
            que.popleft()
        else:
            target = que.index(order[0])
            if target  < 0.5 * len(que):
                cnt += target
                que.rotate(-target)
            else:
                cnt += len(que) - target
                que.rotate(len(que) - target)
    else:
        print(cnt)
        break
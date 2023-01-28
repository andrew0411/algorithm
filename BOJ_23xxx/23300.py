import sys
from collections import deque

input = sys.stdin.readline

N, Q = map(int, input().split())

f_cache = deque()
b_cache = deque()
current = 0

for i in range(Q):
    s = input().rstrip()
    if len(s) >= 2:
        # forward cache 모두 삭제
        f_cache.clear()

        # 현재 페이지 backward 에 추가, 현재 페이지 갱신, 처음 경우 고려
        if current == 0:
            current = int(s.split()[1])
        else:
            b_cache.append(current)
            current = int(s.split()[1])

    elif s == 'B':
        # backward가 비어있으면 무시
        if not b_cache:
            continue
        # 현재 페이지 forward로 저장, backward 페이지 가져오기
        else:
            f_cache.appendleft(current)
            current = b_cache.pop()

    elif s == 'F':
        # forward가 비어있으면 무시
        if not f_cache:
            continue
        else:
            b_cache.append(current)
            current = f_cache.popleft()
    
    else:
        compress = 0
        if len(b_cache) >= 2:
            for i in range(len(b_cache)-1, -1, -1):
                if b_cache[i] == compress:
                    del b_cache[i]
                else: compress = b_cache[i]


print(current)
if b_cache:
    print(*reversed(b_cache))
else:
    print(-1)

if f_cache:
    print(*f_cache)
else:
    print(-1)
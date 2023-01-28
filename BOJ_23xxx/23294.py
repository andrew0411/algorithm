import sys
from collections import deque

input = sys.stdin.readline

N, Q, C = map(int, input().split())

cache = list(map(int, input().split()))

b_page = deque()
f_page = deque()
current_page = 0
current_cache = 0

for i in range(Q):
    s = input().rstrip()

    # A인 경우
    if len(s) >= 2:
        if f_page:
            for i in range(len(f_page)):
                current_cache -= cache[f_page[i] - 1]
            f_page.clear()
        if current_page != 0:
            b_page.append(current_page)
        
        current_page = int(s.split()[1])
        current_cache += cache[current_page - 1]
        while True:
            if current_cache <= C:
                break
            else:
                temp = b_page.popleft()
                current_cache -= cache[temp - 1]
    
    elif s == 'B':
        if b_page:
            f_page.appendleft(current_page)
            current_page = b_page.pop()

    elif s == 'F':
        if f_page:
            b_page.append(current_page)
            current_page = f_page.popleft()

    else:
        c = 0
        if len(b_page) >= 2:
            for i in range(len(b_page) - 1, -1, -1):
                if b_page[i] == c:
                    current_cache -= cache[b_page[i] - 1]
                    del b_page[i]
                else:
                    c = b_page[i]

    # print('page: ', current_page, b_page, f_page)
    # print('cache: ', current_cache)

print(current_page)
if b_page:
    print(*reversed(b_page))
else:
    print(-1)
if f_page:
    print(*f_page)
else:
    print(-1)
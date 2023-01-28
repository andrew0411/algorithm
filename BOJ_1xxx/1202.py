import sys
from queue import PriorityQueue
input = sys.stdin.readline

'''
que 생성 -- que = PriorityQueue()
원소 추가 -- que.put()
원소 삭제 -- que.get() : 가장 작은 원소를 que에서 제거함과 동시에 return (리스트 pop 같은 느낌)
정렬 기준 -- que.get()[1]

que.qsize() : que의 크기 반환
que.empty() : que가 비었으면 true
que.full()  : que가 다 찼으면 true
'''

### Receive inputs

N, K = map(int, input().split())
J = []
for i in range(N):
    m, v = map(int, input().split())
    J.append([m, v])

for i in range(K):
    J.append([int(input()), 1000001])

J.sort()
price = 0

que = PriorityQueue(maxsize=N)

for j in J:
    if j[1] != 1000001:
        que.put(-j[1])
    else:
        if not(que.empty()):
            temp = -que.get()
            price += temp
print(price)
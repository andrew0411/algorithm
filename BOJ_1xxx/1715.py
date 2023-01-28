import sys
from queue import PriorityQueue
input = sys.stdin.readline

N = int(input())
if N == 1:
    print(0)
else:    
    nums = [0] * N
    for i in range(N):
        nums[i] = int(input())

    que = PriorityQueue(maxsize=N)

    for n in nums:
        que.put(n)

    answer = 0

    while True:
        if que.qsize() == 1:
            print(answer)
            exit(0)
        else:
            a = que.get()
            b = que.get()
            answer += (a + b)
            que.put(a + b)
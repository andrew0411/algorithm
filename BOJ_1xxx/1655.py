import heapq
import sys

input = sys.stdin.readline

N = int(input())

left = []
right = []
median = []

for i in range(N):
    temp = int(input())

    if not left and not right:
        heapq.heappush(left, (-temp, temp))
        median.append(temp)
        continue
    
    if not right:
        if temp < left[0][1]:
            heapq.heappush(right, heapq.heappop(left)[1])
            heapq.heappush(left, (-temp, temp))
            median.append(left[0][1])
        else:
            heapq.heappush(right, temp)
            median.append(left[0][1])
        continue

    if len(left) == len(right):
        if temp >= right[0]:
            heapq.heappush(right, temp)
            median.append(right[0])
        else:
            heapq.heappush(left, (-temp, temp))
            median.append(left[0][1])
    
    elif len(left) > len(right):
        if temp >= right[0]:
            heapq.heappush(right, temp)
            median.append(left[0][1])
        else:
            heapq.heappush(left, (-temp, temp))
            heapq.heappush(right, heapq.heappop(left)[1])
            median.append(left[0][1])
    
    else:
        if temp >= right[0]:
            heapq.heappush(right, temp)
            t = heapq.heappop(right)
            heapq.heappush(left, (-t, t))
            median.append(left[0][1])
        else:
            heapq.heappush(left, (-temp, temp))
            median.append(left[0][1])

print(*median, sep='\n')
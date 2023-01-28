import sys
input = sys.stdin.readline

T=int(input())
result = [0] * T
for i in range(T):
    arr = list(map(int, input().split()))
    arr.sort()
    
    if arr[1]+4<=arr[3]:
        result[i] = 'KIN'
    else:
        result[i] = sum(arr[1:4])
print(*result, sep='\n')
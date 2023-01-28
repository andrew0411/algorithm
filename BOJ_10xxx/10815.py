import sys
input = sys.stdin.readline

N = input()
Ns = set(map(int, input().split()))
M = input()
Ms = list(map(int, input().split()))
for i in Ms:
    if i in Ns:
        print(1, end=' ')
    else:
        print(0, end=' ')


'''
Binary Search

import sys
input = sys.stdin.readline

N = int(input())
Ns = list(map(int, input().split()))
M = input()
Ms = list(map(int, input().split()))
Ns.sort()

def BinarySearch(arr, target, low, high):
    if low>high:
        return 0
    mid = int((low + high) / 2)

    if arr[mid] == target:
        return 1
    
    elif arr[mid] > target:
        return BinarySearch(arr, target, low, mid-1)
    else:
        return BinarySearch(arr, target, mid+1, high)

for i in Ms:
    print(BinarySearch(Ns, i, 0, N-1), end=' ')
'''
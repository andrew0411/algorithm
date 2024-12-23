import sys

input = sys.stdin.readline

N, M = map(int, input().split())

set1 = set()
set2 = set()

for i in range(N):
    set1.add(input().strip())
for i in range(M):
    set2.add(input().strip())

arr = sorted(list(set1 & set2))
print(len(arr))
print(*arr, sep='\n')

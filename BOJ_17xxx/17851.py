import sys
input = sys.stdin.readline

A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))

sum = 0
for i in range(5):
    sum += 1 if (A[i] > B[i]) else 0
print(sum)
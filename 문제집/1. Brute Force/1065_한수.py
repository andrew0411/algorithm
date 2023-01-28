import sys

input = sys.stdin.readline

N = int(input())

arr = [0 for i in range(N + 1)]

def isHan(num):
    s = str(num)
    if len(s) < 3:
        return 1
    else:
        if int(s[0]) + int(s[2]) == int(s[1]) * 2:
            return 1

        else:
            return 0

for i in range(1, N + 1):
    arr[i] = isHan(i)

print(sum(arr))

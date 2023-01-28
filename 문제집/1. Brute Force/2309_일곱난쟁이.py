import sys

input = sys.stdin.readline

arr = [int(input()) for _ in range(9)]

arr.sort(reverse=True)

first_break = False

for i in range(8):

    if first_break:
        break

    for j in range(8 - i):
        
        if arr[i] + arr[i + j + 1] == sum(arr) - 100:
            arr.pop(i)
            arr.pop(i + j)
            first_break = True
            break
        
print(*sorted(arr), sep='\n')
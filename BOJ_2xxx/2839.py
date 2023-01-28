N=int(input())
result = 0
if N % 5 == 0:
        result += N // 5 
else:
    while True:
        N -= 3
        result += 1
        if N % 5 == 0:
            result += N // 5
            break
        elif N == 0:
            break
        elif N <= 2:
            result = -1

print(result)
arr = [300, 60, 10]
n = int(input())
result = [0] * 3
for i in range(3):
    result[i] = n // arr[i]
    n %= arr[i]
if n == 0:
    print(*result)
else:
    print(-1)

'''
short coding

T=int(input)
print(*[[T//300, T//60%5, T//10%6], [-1]][T%10>0])
'''
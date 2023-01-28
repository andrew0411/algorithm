N, w, h = map(int, input().split())
d = (w**2 + h**2)**0.5

result = []
for i in range(N):
    x = int(input())
    if x <= d:
        result.append('DA')
    else:
        result.append('NE')

print(*result, sep='\n')
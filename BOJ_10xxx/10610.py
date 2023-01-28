N = input()
sum = 0
for i in list(N):
    sum+= int(i)

if '0' not in N or sum % 3 != 0:
    print(-1)
else:
    print(''.join(sorted(N, reverse=True)))
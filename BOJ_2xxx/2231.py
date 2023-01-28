def check(N):
    for i in range(N):
        if (i+sum(map(int,str(i)))) == N:
            return i
    return 0

N = int(input())
print(check(N))
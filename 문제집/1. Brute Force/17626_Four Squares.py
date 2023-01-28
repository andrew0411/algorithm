N = int(input())

# 모두 4개 이하의 제곱수 합으로 표현 가능하므로 일단 4로 초기화
arr = [4 for _ in range(N + 1)]

arr[0] = 0

# 제곱수인 애들 1로 초기화
for i in range(int(N**0.5)+ 1):
    arr[i**2] = 1

# 제곱수로 뺀 모든 경우의 수를 고려
for i in range(1, N + 1):
    if arr[i] != 1:
        temp = int(i**0.5)
        ls = []
        for j in range(1, temp + 1):
            ls.append(arr[i - j ** 2] + 1)
        arr[i] = min(ls)
print(arr[N])
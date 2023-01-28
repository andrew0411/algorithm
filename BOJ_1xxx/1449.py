N, L = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

cnt = 1
start = arr[0] - 0.5
for a in arr:
    if start + L >= a + 0.5:
        continue
    else:
        start = a - 0.5
        cnt += 1
print(cnt)
N = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))[:-1]
result = 0
min_price = 1000000000
for i in range(N-1):
    if price[i] < min_price:
        min_price = price[i]
    result += min_price * distance[i]
print(result)
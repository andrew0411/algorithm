t1 = input()
t2 = int(input())
h, m = list(map(int, t1.split(' ')))
h = h + (m + t2) // 60 if (m + t2) >= 60 else h
h = h % 24 if h >= 24 else h
m = m + t2 if (m + t2) < 60 else (m + t2) % 60
print(h, m)
arr = [True for i in range(10000)]
for i in range(1, 10001):
    s = str(i)
    res = eval('+'.join(s) + '+' + s)
    if res < 10000:
        arr[res] = False

for i in range(1, len(arr)):
    if arr[i]:
        print(i)
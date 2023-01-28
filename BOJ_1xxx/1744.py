N = int(input())
pos = []
neg = []
result = []
for i in range(N):
    temp = int(input())
    if temp <= 0:
        neg.append(temp)
    elif temp == 1:
        result.append(1)
    else:
        pos.append(temp)
pos.sort(reverse=True)
neg.sort()

while True:
    if len(neg) > 1:
        t1 = neg.pop(0)
        t2 = neg.pop(0)
        result.append(t1 * t2)
    elif len(neg) == 1:
        result.append(neg[0])
        break
    else:
        break
    
    
while True:
    if len(pos) > 1:
        t1 = pos.pop(0)
        t2 = pos.pop(0)
        result.append(t1 * t2)
    elif len(pos) == 1:
        result.append(pos[0])
        break
    else:
        break

print(sum(result))
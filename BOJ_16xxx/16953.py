A, B = map(int, input().split())
result = 0

while True:
    if str(B)[-1] == '1':
        B = int((B - 1) / 10)
        result += 1
        if B == A:
            print(result+1)
            break
        elif B < A:
            print(-1)
            break
        else:
            continue
    elif B % 2 == 0:
        B = int(B/2)
        result += 1
        if B == A:
            print(result+1)
            break
        elif B < A:
            print(-1)
            break
        else:
            continue
    else:
        print(-1)
        break
def solution(strArr):
    for i in range(len(strArr)):
        if i & 1:
            strArr[i] = strArr[i].upper()
        else:
            strArr[i] = strArr[i].lower()
    return strArr

'''
range 보다 enumerate 사용하는 것이 더 빠를수도

def solution(strArr):
    return [s.lower() if i % 2 == 0 else s.upper() for i, s in enumerate(strArr)]
'''
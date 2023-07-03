def solution(n):
    ternary = ''
    while n > 0:
        n, mod = divmod(n, 3)
        ternary += str(mod)

    answer = 0
    for i in range(len(ternary)):
        answer += int(ternary[i]) * (3 ** (len(ternary) - 1 - i))
    return answer


'''
### int(n, base) 일때
### n이라는 정수를 base-진법으로 변환해주는 기능이 있다.

def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer

'''
def solution(arr):
    answer = []
    for num in arr:
        answer += [num for _ in range(num)]
    return answer

'''
메모리 usage 측면에서 .append()를 쓰는 것이 += 쓰는 것보다 더 효율적임
def solution(arr):
    answer = []
    for x in arr:
        for i in range(x):
            answer.append(x)
    return answer
'''
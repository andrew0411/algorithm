def solution(num_list):
    if len(num_list) > 10:
        return sum(num_list)
    else:
        answer = 1
        for num in num_list:
            answer *= num
        return answer

'''
prod func()를 사용하면 리스트 내의 원소들의 곱을 얻을 수 있음
from math import prod
def solution(num_list):
    return sum(num_list) if len(num_list)>=11 else prod(num_list)
'''
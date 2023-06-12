def solution(num_list):
    SUM = sum(num_list) ** 2
    MUL = 1
    for i in num_list:
        MUL *= i
        
    if MUL < SUM:
        return 1
    else:
        return 0

'''
import math
def solution(num_list):
    answer = 0
    if math.prod(num_list) < (sum(num_list)**2):
        answer = 1
    return answer
'''
def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        answer.append(num_list[i])
    return answer

'''
리스트 내에서 바로 indexing 가능

def solution(num_list, n):
    return num_list[::n]
'''
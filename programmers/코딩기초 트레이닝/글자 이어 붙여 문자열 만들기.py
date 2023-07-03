def solution(my_string, index_list):
    answer = ''
    for idx in index_list:
        answer += my_string[idx]
    return answer

'''
''.join() 잘 쓰기

def solution(my_string, index_list):
    return ''.join([my_string[idx] for idx in index_list])
'''
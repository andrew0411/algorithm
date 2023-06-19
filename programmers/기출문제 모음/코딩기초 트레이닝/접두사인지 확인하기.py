def solution(my_string, is_prefix):
    if my_string[:len(is_prefix)] == is_prefix:
        return 1
    else:
        return 0

'''
string에서 startswith function() 사용

def solution(my_string, is_prefix):
    return int(my_string.startswith(is_prefix))
'''
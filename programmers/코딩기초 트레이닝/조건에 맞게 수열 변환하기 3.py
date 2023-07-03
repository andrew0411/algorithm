def solution(arr, k):
    if k % 2:
        return [i * k for i in arr]
    else:
        return [i + k for i in arr]
    
'''
# map + lambda 사용할수도
def solution(arr, k):
    if k % 2 != 0:
        return list(map(lambda x: x * k, arr))

    return list(map(lambda x: x + k, arr))
'''
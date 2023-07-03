from itertools import combinations

def solution(numbers):
    answer = []
    for i, j in combinations(range(len(numbers)), 2):
        if numbers[i] + numbers[j] not in answer:
            answer.append(numbers[i] + numbers[j]) 
    return sorted(answer)
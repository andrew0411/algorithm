from itertools import permutations

words = ['aya', 'ye', 'woo', 'ma']
dictionary = []

for i in range(1, 5):
    for word in permutations(words, i):
        dictionary.append(''.join(word))

def solution(babbling):
    cnt = 0
    for b in babbling:
        if b in dictionary:
            cnt += 1
            
    return cnt
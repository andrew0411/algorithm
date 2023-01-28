import sys

input = sys.stdin.readline

A, B = input().split()

def check(A, B):
    result = sum([A[i] != B[i] for i in range(len(A))])
    return result

if len(A) == len(B):
    print(check(A, B))
else:
    result = 50
    for i in range(len(B)-len(A)+1):
        temp = check(A, B[i:i+len(A)])
        if temp < result:
            result = temp  
    print(result)
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(sum(map(lambda a, b : a * b, sorted(A), sorted(B, reverse=True))))


'''
not sorting B

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

s = 0
for i in range(n):
    s += min(A) * max(B)
    A.pop(A.index(min(A)))
    B.pop(B.index(max(B)))

'''
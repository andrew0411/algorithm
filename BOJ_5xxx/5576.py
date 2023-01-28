import sys
input = sys.stdin.readline

scores = [0] * 20
for i in range(20):
    scores[i] = int(input())
print(sum(sorted(scores[:10])[7:]), sum(sorted(scores[10:])[7:]))

N = int(input())
ref = {}
for _ in range(N):
    s = list(input())
    for i in range(len(s)):
        if s[i] not in ref:
            ref[s[i]] = 0
        ref[s[i]] += 10 ** (len(s)-1-i)
ref = sorted(list(ref.values()), reverse=True)
num_ls = [9-i for i in range(9)]
print(sum(list(map(lambda a, b: a * b, ref, num_ls[:len(ref)+1]))))
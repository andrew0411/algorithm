line = input()
word = input()
result = 0
idx = 0

for i in range(len(line)):
    if idx > i :
        continue

    if word == line[i: i+len(word)]:
        result += 1
        idx = i + len(word)

print(result)
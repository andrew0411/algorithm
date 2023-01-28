A, B = input().split()

mini = [A.replace('6', '5'), B.replace('6', '5')]
maxi = [A.replace('5', '6'), B.replace('5', '6')]
print(sum(map(int, mini)), sum(map(int, maxi)))
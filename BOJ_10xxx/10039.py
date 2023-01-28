avg=0
for i in range(5):
    score = int(input())
    avg += score/5 if score > 40 else 8
print(int(avg))

'''
short coding

print(eval("+max(8,int(input())//5)"*5))
'''

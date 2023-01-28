import sys
import math
input = sys.stdin.readline
n = int(input())
t = math.ceil((-1+(1+8*n)**0.5)*0.5)
k = int(t*(t+1)*0.5)

ja=t-(k-n)
mo=t+1-ja
if t % 2 == 0:
    print(str(ja)+'/'+str(mo))
else:
    print(str(mo)+'/'+str(ja))
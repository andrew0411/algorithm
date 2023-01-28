w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
p += t % (2 * w)
q += t % (2 * h)

if p > w:
    p = abs(2 * w - p)
if q > h :
    q = abs(2 * h - q)

print(p, q)

'''
short coding

[w,h],[p,q],[t]=eval('map(int,input().split()),'*3)
for r,s in(p+t,w),(q+t,h):print(abs(r%(2*s)-r%s*2))
'''

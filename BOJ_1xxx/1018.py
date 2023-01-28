h,w=map(int,input().split())
chess=[]
min=1e5
for i in range(h):
    chess.append(input())

def check(i, j, arr):
    val1=0
    val2=0
    for w in range(8):
        for h in range(8):
            if (w+h)%2==0:
                val1+=(arr[i+w][j+h]=='B')
                val2+=(arr[i+w][j+h]=='W')
            else:
                val1+=(arr[i+w][j+h]=='W')
                val2+=(arr[i+w][j+h]=='B')

    return val1 if val1<val2 else val2

for i in range(h-7):
    for j in range(w-7):
        val=check(i, j, chess)
        if val<min:
            min=val
        
print(min)
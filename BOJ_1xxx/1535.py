N=int(input())
heal_ls=list(map(int, input().split()))
joy_ls=list(map(int, input().split()))
max_joy=0
def get(idx, heal, joy):
    global max_joy
    if idx==N:
        return

    get(idx+1, heal, joy)

    if heal-heal_ls[idx] <= 0:
        return 

    heal-=heal_ls[idx]
    joy+=joy_ls[idx]
    if max_joy<joy:
        max_joy=joy

    get(idx+1, heal, joy)
    

get(0, heal=100, joy=0)
print(max_joy)
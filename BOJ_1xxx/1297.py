import math
D, H, W = map(int, input().split())
d = math.sqrt(H**2+W**2)
print(int(D*H/d), int(D*W/d))
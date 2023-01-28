'''
input() 대신 sys.stdin.readline() 사용하면 더 빠름

#### 한개의 정수 입력받기

a = int(sys.stdin.readline())

-> sys.stdin.readline() 는 한 줄 단위로 입력을 받기 때문에
개행문자(\n)가 같이 입력으로 받아짐


#### 정해진 개수의 정수를 한줄에 입력받기

a, b, c = map(int, sys.stdin.readline().split())


#### 임의의 개수의 정수를 한줄에 입력받기

arr = list(map(int, sys.stdin.readline().split()))


#### 임의의 개수의 정수를 n줄 입력받기

arr = []
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))


#### 문자열 n 줄을 입력받기

arr = [sys.stdin.readline().strip() for i in range(n)]

-> strip() 은 문자열의 맨 앞과 맨 끝의 공백문자를 제거.
'''
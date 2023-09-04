"""
단어 정렬
"""
import sys

input = sys.stdin.readline


N = int(input())

arr = list(set([input().strip() for i in range(N)]))

print(*sorted(sorted(arr), key=len), sep='\n')
"""
소트인사이드
"""
import sys

input = sys.stdin.readline

N = input().strip()

temp = [i for i in N]

print(''.join(sorted(temp, reverse=True)))
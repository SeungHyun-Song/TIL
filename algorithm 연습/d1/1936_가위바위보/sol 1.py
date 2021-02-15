import sys
sys.stdin = open("input.txt")

A, B = list(map(int, input().split()))
# 가위 : 1, 바위 : 2, 보 : 3
# 숫자가 1이 높거나 2가 작으면 이긴다.

if A - B == 1 or A - B == -2:
    print('A')
else:
    print('B')

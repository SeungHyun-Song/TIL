import sys
sys.stdin = open("input.txt")

T = int(input())

a = 0 # 몫
b = 0 # 나머지


for tc in range(1, T+1):
    N, M = list(map(int, input().split()))

    a = N // M
    b = N % M
    result = '{} {}'.format(a, b)

    print('#{} {}'.format(tc, result))
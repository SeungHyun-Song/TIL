import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 2 <= N <= 1,000,000

    M = list(map(int, input().split())) # M <= 10,000

    # M이 뜻하는 것이 그 날의 가격.
    # (1) M의 원소가 오름차순일 경우가 가장 이상적. 맨날 사서 가장 비쌀 때 다 파는것.
    # (2) M의 원소가 내림차순일 경우 아무것도 사지 않는 것이 가장 이익
    # (2)의 경우 중 대표적인 case : M[0]이 다른 모든 원소들보다도 큰 것.

    # (3) 살 때는 하나만 살 수 있고 판매할 때는 제한이 없다는 조건도 구현해야함.









    print('#{} '.format(tc, ))
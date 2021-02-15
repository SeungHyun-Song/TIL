import sys
sys.stdin = open("input.txt")

T = int(input()) # 테스트 케이스 수

for tc in range(1, T+1):
    N, M = list(map(int, input().split())) # 각 tc의 비교할 숫자들 의미
    result = ''
    if N < M:
        result = '<'
    elif N == M:
        result = '='
    else:
        result = '>'

    print("#{} {}".format(tc, result))
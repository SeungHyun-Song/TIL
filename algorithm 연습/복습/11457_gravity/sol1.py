import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input()) # tc 아래의 숫자, 9를 의미

    arr = list(map(int, input().split())) # 그 이후 7 4 2 0 0 6 0 7 0을 리스트로 표현

    result_arr = [0] * N # N개의 요소를 갖는 리스트로 초기화

    for i in arr:
        for j in range(i):
            result_arr[i] += 1 # arr의 요소 i에 대해...? 어떻게 되는거지

    
    print("#{} ".format(tc, ))


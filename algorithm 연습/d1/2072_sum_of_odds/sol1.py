import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    before = list(map(int,input().split())) # 주어진 숫자들을 원소로 갖는 리스트
    sum_of_odds = 0 # 홀수들의 합 초기화

    for i in before: # 리스트 안의 원소 i에 대해
        if i%2: # i를 2로 나눈 나머지가 1일 때만 i들을 더해나간다.
            sum_of_odds += i

    print("#{} {}".format(tc, sum_of_odds))
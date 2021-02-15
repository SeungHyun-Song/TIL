import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    before = list(map(int,input().split())) # 주어진 숫자들을 원소로 갖는 리스트
    sum_of_odds = 0 # 홀수들의 합 초기화


    print("#{} {}".format(tc, sum_of_odds))


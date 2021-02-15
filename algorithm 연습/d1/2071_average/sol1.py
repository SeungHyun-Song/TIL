import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    numbers = list(map(int, input().split()))

    sum_of_nums = 0
    len_of_num_lists = 0 # 숫자들의 합과 숫자 리스트의 길이값 초기화

    for i in numbers:
        sum_of_nums += i
        len_of_num_lists += 1 # 숫자들의 합계에는 원소 i의 값을 더해주고 그 때마다 리스트 길이 값에 1 더해준다.

    average_of_numbers = sum_of_nums / len_of_num_lists # 이대로 쓰면 답이 정수로 나오지 않는다.

    result = round(average_of_numbers) # int는 버림, round는 반올림
    
    print("#{} {}".format(tc, result))


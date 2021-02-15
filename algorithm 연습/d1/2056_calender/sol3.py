import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    number = int(input())
    yyyy = number // 10000 # 10000으로 나눈 몫
    mm = (number % 10000) // 100 # 1만으로 나눈 나머지를 100으로 나눈 몫
    dd = number % 100

    if mm < 1 or mm > 12:
        print("#{} -1".format(tc))
        continue # 1~12 이외의 숫자를 월 에 입력하면 -1 출력, 아니면 아래로.

    if mm in [1, 3, 5, 7, 8, 10, 12]: # 31일까지 있는 달
        if dd < 1 or dd > 31:
            print("#{} -1".format(tc))
            continue

    if mm == 2:
        if yyyy % 4 == 0:
            if dd < 1 or dd > 29:
                print("#{} -1".format(tc))
        else: # 윤년이 아니면
            if dd < 1 or dd > 29:
                print("#{} -1".format(tc))
                continue
    
    print("#{0} {1:04d}/{2:02d}/{3:02d}".format(tc, yyyy, mm, dd))
    # 하나라도 format 내 원소에 대한 매칭을 시켜줬다면 나머지도 다 해줘야한다.
    # 하지 않으면 ValueError : cannot switch from manual field specification to automatic field numbering 오류 발생
    # :04d 의 의미는 :에 대해 4자리를 쓸건데 빈칸은 0을 출력하라는 의미

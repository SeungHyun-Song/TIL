import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    numbers = input() # 이 문제는 8자리 숫자를 쪼개서 써야하니 list(map(int, input().split())) 을 쓰지 말자

    yyyy = int(numbers[:4]) # 이렇게 하면 numbers에 해당하는 숫자의 앞 4자리만 잘라서 나온다.
    mm = int(numbers[4:6])
    dd = int(numbers[6:])

    if mm < 1 or mm > 12:
        print("#{} -1".format(tc))
        continue # 1~12 이외의 숫자를 월 에 입력하면 -1 출력, 아니면 아래로.

    if mm in [1, 3, 5, 7, 8, 10, 12]: # 31일까지 있는 달
        if dd < 1 or dd > 31:
            print("#{} -1".format(tc))
            continue

    if mm == 2:
        if yyyy % 4 == 0:
            if dd < 1 or dd > 30:
                print("#{} -1".format(tc))
        else: # 윤년이 아니면
            if dd < 1 or dd > 29:
                print("#{} -1".format(tc))
                continue


    if mm in [4, 6, 9, 11]:
        if dd < 1 or dd > 30:
            print("#{} -1".format(tc))
            continue


    
    # print("#{0} {1:04d}/{2:02d}/{3:02d}".format(tc, yyyy, mm, dd))
    print("#{} {:04d}/{:02d}/{:02d}".format(tc, yyyy, mm, dd))
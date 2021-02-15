import sys
sys.stdin = open("input.txt")

# 1. 가장 기초적인 방법 : 숫자 일일이 다 쪼개기
# N = int(input())
# a = N // 1000
# b = (N % 1000) // 100
# c = ((N % 1000) % 100) // 10
# d = N % 10
#
# sum_of_digits = a + b + c + d
# print(sum_of_digits)


N = input() # int(input()) 이 아니라 str 형태로 input 받아버리면 아래처럼

if int(N) > 9999:
    print("9999 아래의 숫자를 입력하세요") # (1 ≤ N ≤ 9999) 라는 조건을 살려봄.
else:
    a = int(N[:1])  # 6
    b = int(N[1:2])  # 7
    c = int(N[2:3])  # 8
    d = int(N[3:4])  # 9
    sum_of_digits = a + b + c + d
    print(sum_of_digits)
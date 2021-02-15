import sys
sys.stdin = open("input.txt")

N = int(input())
result1 = 1 if N%2 == 1 else 0
print(result1)

numbers = list(map(int, input().split()))
result2 = sum(numbers)
print(result2)

N = int(input())
number = []
for i in range(N):
    row = list(map(int, input().split()))
    number.append(row)
result3 = number[1][1]
print(result3)
import sys
sys.stdin = open("input.txt")

N = int(input())
my_sum = 0
for i in range(1, N+1):
    my_sum += i

print(my_sum)
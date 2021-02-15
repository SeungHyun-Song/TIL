import sys
sys.stdin = open("input.txt")

N = int(input())

for i in range(0, N+1):
    x = 2 ** i
    print(x, end = ' ')
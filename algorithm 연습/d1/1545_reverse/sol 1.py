import sys
sys.stdin = open("input.txt")

# N = int(input())
#
# for i in range(0, N+1):
#     print(N - i, end = ' ')


N = int(input())

for i in range(N, -1, -1):
    print( i, end = ' ')
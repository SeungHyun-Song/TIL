import sys
sys.stdin = open("input.txt")

N = input()

M = list(N) # => ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for i in range(len(M)):
    print(ord(M[i])-64, end = ' ')
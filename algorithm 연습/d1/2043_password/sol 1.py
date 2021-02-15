import sys
sys.stdin = open("input.txt")

P, K = list(map(int, input().split())) # P와 K의 값을 분리
print(abs(P - K) + 1)

# 다른 풀이...
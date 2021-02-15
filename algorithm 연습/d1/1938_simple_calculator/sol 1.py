import sys
sys.stdin = open("input.txt")

a, b = list(map(int, input().split()))

add = a + b
sub = a - b
mul = a * b
div = int(a / b)

print('{}\n{}\n{}\n{}\n'.format(add, sub, mul, div))
T = int(input())

for test_case in range(1, T + 1):
    if T % test_case == 0:
        print(f'{test_case}(은)는 {T}의 약수입니다.')
        test_case += 1

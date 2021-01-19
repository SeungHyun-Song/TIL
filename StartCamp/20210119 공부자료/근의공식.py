def roots(a, b, c):
    d = b * b - 4 * a * c
    if d > 0:
        x1 = round((- b - d**0.5) / 2 * a)
        x2 = round((- b + d**0.5) / 2 * a)
        print(x1, x2)
    elif d == 0:
        
        x = round(-b / 2 * a)
        print("중근")
        print(x)
    else:
        print("허근")

a = int(input("0이 아닌 a를 입력 = "))
b = int(input("b를 입력 = "))
c = int(input("c를 입력 = "))
roots(a, b, c)
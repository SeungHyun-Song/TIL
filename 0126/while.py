# 다르게 풀어봐라


def sum_list_while(numbers):

    total = 0
    i = 0
    while i < len(numbers):
        x, y = numbers[i]
        total += x + y
        i += 1
    return total

# 다르게 풀어봐라


print(sum_list_while([[1, 4], [10, 5], [20, 30]]))
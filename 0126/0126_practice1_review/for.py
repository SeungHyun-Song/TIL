def sum_list(numbers):
    total = 0
    for i in numbers:
        j = 0

        for j in range(len(i)):
            total += i[j]
            j += 1
            
    # for i in numbers:
    #     if type(i) == list:
    #         total += sum_list(i)
    #     else:
    #         total += i
            
    return total

print(sum_list([[1, 4], [10, 5], [20, 30], ]))
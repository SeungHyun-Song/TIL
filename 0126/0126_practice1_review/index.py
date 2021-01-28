def sum_list_index(numbers):
    
    total = 0
    i=0
    for i in range(len(numbers)):
        j=0
        for j in range(len(numbers[i])):
            
            total += numbers[i][j]
            j += 1

    return total


print(sum_list_index([[1, 4], [10, 5], [20, 30], [12, 3]]))

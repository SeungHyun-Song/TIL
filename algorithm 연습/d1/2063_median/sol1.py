import sys
sys.stdin = open("input.txt")

N = int(input())

def BubbleSort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

def my_median(arr):
    position = 0
    result = 0
    for i in range(len(arr)):
        position = int(len(arr)/2) # 중간 위치의 번호
        result = arr[position] # 리스트 안의 중간값

    return result

numbers = list(map(int, input().split())) # BubbleSort(numbers) # 위의 숫자들을 버블정렬로 오름차순 정리

s_nums = BubbleSort(numbers)

print(my_median(s_nums))
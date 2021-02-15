import sys
sys.stdin = open("input.txt")

T = int(input())

def selection_sort(arr): # 복잡도 N^2 의 정렬방식.
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

for tc in range(1, T+1):
    my_max = 0 # 나중에 가장 큰 값을 줄 것. 초기화
    N = list(map(int, input().split()))
    n = len(N)

    M = selection_sort(N)
    my_max = M[n-1]
    
    print("#{} {}".format(tc, my_max))
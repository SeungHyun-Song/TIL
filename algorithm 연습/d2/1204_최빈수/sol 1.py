import sys
sys.stdin = open("input.txt")

T = int(input()) # 테스트 케이스의 수

def score_lists(numbers):
    counter = [0] * 101 # 0점 이상 100점 이하 총 101개의 정수값이 있을 수 있다. 초기화!

    most = -1 # 가장 많이 나온 값을 담을 예정. 초기화!

    for number in numbers:
        counter[number] += 1 # 어떤 숫자를 찾으면 counter 라는 리스트의 해당 원소에 1을 더해준다.

    for i in range(len(counter)): # 0부터 101까지의 원소에 대해
        for j in range(len(counter)): # 또 다른 0부터 101까지의 원소

            if counter[i] > counter[j]: # 그 원소가 가장 많이 있을 경우
                most = i # most에 그 값을 담아준다.

            elif counter[i] == counter[j]: # 만약 두 원소의 개수가 같다면?

                if i > j: # i값이 j보다 크면 i을 most의 값으로
                    most = i

                else:
                    most = j

            else:
                most = j

        return most


for tc in range(1, T+1):
    N = int(input()) # 테스트 케이스의 번호
    scores = list(map(int, input().split())) # 테스트 케이스 내의 1000개의 점수들. 0점 이상 100점 이하

    result = score_lists(scores)
    print("#{} {}".format(tc, result))

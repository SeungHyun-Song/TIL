# import 문은 스크립트 파일 최상단에 위치한다.
import random
# 1~45번 숫자 만들어서 저장하기
numbers = range(1, 46)  #range를 쓸 때는 범위를 마지막 숫자보다 1 크게
# print(numbers)

# numbers에서 6개 숫자 뽑아서 저장하기
lucky_numbers = random.sample(numbers, 6)
print(sorted(lucky_numbers))  #sorted : 숫자들을 순서대로 정렬
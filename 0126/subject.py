students = [
 [100, 80, 100],
 [90, 90, 60],
 [80, 80, 80]
]

# IM 합격하기 위해 무수히 풀어볼 문제 유형
# 2중 for문을 순회하고,
# 2중 for문 안에서 내가 원하는 데이터만 적절히 가져오기


for x in range(len(students[0])): # 과목 : 0 - 국어, 1 - 수학, 2- 영어
    total = 0
    for y in range(len(students)): # 학생 : 0 - A, 1 - B, 2 - C
        
        
        total += students[y][x]
    print(total)
    
# 이 문제는 행렬처럼 접근하는 방식을 생각해봐야한다.
# 반드시 순서를 지킬 필요는 없다는 것


# students 라는 리스트에서
# [ [ A ] , [ B ] , [ C ] ]
# A[0] + B[0] + C[0]
# A[1] + B[1] + C[1]
# A[2] + B[2] + C[2]
# 이렇게 셋을 구하고 싶다.
# 
# 

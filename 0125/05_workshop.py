# # 1. 평균 점수 구하기
# def get_dict_avg(scores):
#     # score_total = 0
#     result = []

#     for score in scores.values():
#     # for score in scores: 일 때는 print(scores.get(score))로 쓰면 value값만 다 뽑아온다.
#         # score_total += score
#         result.append(score) # result 라는 리스트에 score라는 scores의 value값을 넣어준다.

#     return sum(result) / len(result)

# print(get_dict_avg({
#     'python': 80, 'algorithm': 90,
#     'django': 89, 'web': 83,
# })) #=> 85.5

# # 이 딕셔너리의 value를 뽑아내서 list로 만드는 방법?
# # 

# 2. 혈액형 분류하기
def count_blood(blood_list):
    # 1. 결과값 변수 초기화
    blood_dict = {}

    # 2-1. blood_list 순회
    # for blood in blood_list:
    #     # 혈액형 정보가 존재하면?
    #     if blood_dict.get(blood):
    #         blood_dict[blood] += 1 # 1더하기
    #     # 혈액형 정보가 없으면?
    #     else:
    #         blood_dict[blood] = 1 # 1로 초기화

    # 2-2.
    for blood in blood_list:
        # 혈액형 정보가 존재하면 -> 0이 아님 -> 기존값 + 1
        # 혈액형 정보가 없으면 -> 0 -> 0 + 1 (1로 초기화)
        blood_dict[blood] = blood_dict.get(blood, 0) + 1

    return blood_dict

print(count_blood([
    'A', 'B', 'A', 'O', 'AB', 'AB',
    'O', 'A', 'B', 'O', 'B', 'AB'
]))
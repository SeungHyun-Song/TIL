# # 1. 무엇이 중복일까
# def duplicated_letters(word):
#     duplicates = []

#     # apple -> a, p, p, ...
#     for char in word:
#         # 문자가 두 번 이상 나오고 + 중복 문자 리스트에 들어있지 않으면
#         if (word.count(char) > 1) and (char not in duplicates):
#             duplicates.append(char)

#     return duplicates

# print(duplicated_letters('apple'))  #=> ['p']
# print(duplicated_letters('banana')) #=> ['a', 'n']

# # 2. 소대소대
# def low_and_up(word):
#     new_str = ''

#     for idx, char in enumerate(word):
#         # print(idx, char) => 어떻게 나오는지 확인 한 번 해보고
        
#         # 홀수면 대문자 (나머지 있으면)
#         if idx % 2:
#             new_str += char.upper()
#         # 짝수면 소문자 (나머지 없으면)
#         else:
#             new_str += char.lower()
#     return new_str

# print(low_and_up('apple'))  # => 'aPpLe'
# print(low_and_up('banana')) # => 'bAnAnA'

# 3. 숫자의 의미
def lonely(numbers):
    lone = []

    for idx, number in enumerate(numbers):
        # 첫 번째 숫자는 일단 넣음 -> 비교대상으로 선정 / 어차피 혼자
        if idx == 0:
            lone.append(number)

        # 직전에 넣은 숫자와 지금 뽑은 숫자가 다르면 혼자! Append
        # 같으면 커플이기때문에 그냥 Pass
        if lone[-1] != number:
            lone.append(number)
    return lone


print(lonely([1, 1, 3, 3, 0, 1, 1])) # => [1, 3, 0, 1]
print(lonely([4, 4, 4, 3, 3])) # => [4, 3]
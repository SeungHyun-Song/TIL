# # 모음 세기
# def count_vowels(words):
#     result = 0
#     vowel = ['a', 'e', 'i', 'o', 'u']

#     for word in words:
#         if word in vowel:
#             result += 1
#     return result

# print(count_vowels('apple'))
# print(count_vowels('banana'))

# 정사각형만 만들기
def only_square_area(n, m):
    result = []

    for i in n:
        if i in m:
            j = i ** 2
            result.append(j)
    return result

print(only_square_area([32, 55, 63], [13, 32, 40, 55]))

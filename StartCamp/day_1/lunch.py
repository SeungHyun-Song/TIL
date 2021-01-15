menu = ['예향정', '장가계', '첨단공원국밥']
# print(menu)
# print(menu[0], menu[-1])

phone_book = {'예향정': '123-123', '장가계': '456-456', '첨단공원국밥': '789-789'}
# print(phone_book)
# print(phone_book['첨단공원국밥'])


# 1. 가게 하나 랜덤으로 추천받기
import random

my_menu = random.choice(menu)
print(my_menu + '의 전화번호는 ' + phone_book[my_menu] + '입니다')

# f-string -> python 3.6
print(f'할레할레! {my_menu} {phone_book[my_menu]}')
# 모듈 공부

import check, random
# from my_package.math import tools  # from 뒤에는 모듈이 있는 폴더, import 뒤에는 그 파일 이름
# from my_package.math.tools import pi, my_max # 원하는 것만 선택해서 들고올 수도 있다.
# from my_package.math.tools import * # 잘 안쓴다. 다른 사람은 뭔지 알기 힘들다.
from my_package.math.tools import pi as tools_pi

# print(dir(check))

# print(check.odd(5))
# seunghyun_odd = check.odd
# print(seunghyun_odd(10))

# print(dir(tools))
# print(tools.pi)
pi = '변수?'
print(pi, tools_pi)

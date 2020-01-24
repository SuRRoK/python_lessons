# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

from district.central_street.house1 import room1 as central_st_h1_r1, room2 as central_st_h1_r2
from district.central_street.house2 import room1 as central_st_h2_r1, room2 as central_st_h2_r2
from district.soviet_street.house1 import room1 as soviet_st_h1_r1, room2 as soviet_st_h1_r2
from district.soviet_street.house2 import room1 as soviet_st_h2_r1, room2 as soviet_st_h2_r2

folks_in_rooms = [
    central_st_h1_r1.folks,
    central_st_h1_r2.folks,
    central_st_h2_r1.folks,
    central_st_h2_r2.folks,
    soviet_st_h1_r1.folks,
    soviet_st_h1_r2.folks,
    soviet_st_h2_r1.folks,
    soviet_st_h2_r2.folks,
    ]

folks_as_array = []

for room in folks_in_rooms:
    for folk in room:
        folks_as_array.append(folk)

coma = ', '

print('На районе живут', coma.join(folks_as_array))

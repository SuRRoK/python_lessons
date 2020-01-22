# -*- coding: utf-8 -*-

# (if/elif/else)

# Заданы размеры envelop_x, envelop_y - размеры конверта и paper_x, paper_y листа бумаги
#
# Определить, поместится ли бумага в конверте (стороны листа параллельны сторонам конверта)
#
# Результат проверки вывести на консоль (ДА/НЕТ)
# Использовать только операторы if/elif/else, можно вложенные

envelop_x, envelop_y = 10, 7
# paper_x, paper_y = 8, 9
# проверить для
# paper_x, paper_y = 9, 8
# paper_x, paper_y = 6, 8
# paper_x, paper_y = 8, 6
# paper_x, paper_y = 3, 4
# paper_x, paper_y = 11, 9
paper_x, paper_y = 9, 11


# (просто раскоментировать нужную строку и проверить свой код)

def is_suitable_size(hole_x, hole_y, subject_x, subject_y):
    if (hole_x >= subject_x and hole_y >= subject_y) or (hole_x >= subject_y and hole_y >= subject_x):
        return 'Да'
    else:
        return 'Нет'


print(is_suitable_size(envelop_x, envelop_y, paper_x, paper_y))

# Усложненное задание, решать по желанию.
# Заданы размеры hole_x, hole_y прямоугольного отверстия и размеры brick_х, brick_у, brick_z кирпича (все размеры
# могут быть в диапазоне от 1 до 1000)
#
# Определить, пройдет ли кирпич через отверстие (грани кирпича параллельны сторонам отверстия)

hole_x, hole_y = 8, 9
# brick_x, brick_y, brick_z = 11, 10, 2
# brick_x, brick_y, brick_z = 11, 2, 10
# brick_x, brick_y, brick_z = 10, 11, 2
# brick_x, brick_y, brick_z = 10, 2, 11
# brick_x, brick_y, brick_z = 2, 10, 11
# brick_x, brick_y, brick_z = 2, 11, 10
# brick_x, brick_y, brick_z = 3, 5, 6
# brick_x, brick_y, brick_z = 3, 6, 5
# brick_x, brick_y, brick_z = 6, 3, 5
# brick_x, brick_y, brick_z = 6, 5, 3
# brick_x, brick_y, brick_z = 5, 6, 3
# brick_x, brick_y, brick_z = 5, 3, 6
# brick_x, brick_y, brick_z = 11, 3, 6
# brick_x, brick_y, brick_z = 11, 6, 3
# brick_x, brick_y, brick_z = 6, 11, 3
# brick_x, brick_y, brick_z = 6, 3, 11
# brick_x, brick_y, brick_z = 3, 6, 11
brick_x, brick_y, brick_z = 3, 11, 6


# (просто раскоментировать нужную строку и проверить свой код)

def min_2_el(a, b, c):
    min_1 = a
    min_2 = b
    if b < min_1:
        min_1 = b
        min_2 = a
        if c < min_2:
            min_2 = c
    else:
        if c < min_1:
            min_1 = c
        else:
            if c < min_2:
                min_2 = c
    return min_1, min_2


min_dim_1, min_dim_2 = min_2_el(brick_x, brick_y, brick_z)

print(is_suitable_size(hole_x, hole_y, min_dim_1, min_dim_2))

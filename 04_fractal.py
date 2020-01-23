# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1400, 800)

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения


def draw_branches(start_point, start_angle, branch_length):
    if branch_length < 10:
        return
    start_point = sd.vector(start_point, start_angle, branch_length)
    delta = 30
    branch_length *= .75

    shift_angle = start_angle + delta
    draw_branches(start_point, shift_angle, branch_length)

    shift_angle = start_angle - delta
    draw_branches(start_point, shift_angle, branch_length)


# root_point = sd.get_point(300, 30)
# draw_branches(root_point, 90, 100)

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

def rand_delta(number, percent=50, is_positive=False):
    if is_positive:
        rand = sd.random_number(0, percent * 10) / 1000
    else:
        rand = sd.random_number(-percent * 10, percent * 10) / 1000

    return number * rand


def draw_random_branches(start_point, start_angle, branch_length):
    if branch_length < 8:
        return
    start_point = sd.vector(start_point, start_angle, branch_length)
    delta = int(30 + rand_delta(30, percent=40))
    branch_length *= (.75 + rand_delta(0.75, percent=20, is_positive=True))
    print(rand_delta(30, percent=40), rand_delta(0.75, percent=20))
    shift_angle = start_angle + delta
    draw_random_branches(start_point, shift_angle, branch_length)

    shift_angle = start_angle - delta
    draw_random_branches(start_point, shift_angle, branch_length)


root_point = sd.get_point(600, 30)
draw_random_branches(root_point, 90, 80)

sd.pause()

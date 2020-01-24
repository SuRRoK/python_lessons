# -*- coding: utf-8 -*-
import simple_draw as sd
sd.resolution = (900, 900)

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg
colors = [sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN, sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE]
colors_names = ['Красный', 'Оранжевый', 'Жёлтый', 'Зелёный', 'Бирюзовый', 'Синий', 'Фиолетовый']

for i, color in enumerate(colors_names):
    print(i, '-', color)


def user_input():
    user_data = input("Введите номер цвета: ")
    color_num = int(user_data)
    if 0 <= color_num < 7:
        print('Вы ввели', color_num)
        return color_num
    else:
        print('Некорректные данные')


user_color = user_input()


def count_angle(start_point, zero_angle, side_length, sides_count, color_id):
    end_point = start_point
    angle_shift = int(360 / sides_count)
    for angle in range(0, 360 - angle_shift, angle_shift):
        start_point = sd.vector(start_point, angle + zero_angle, side_length, colors[color_id])

    sd.line(start_point, end_point, colors[color_id])


point = sd.get_point(300, 200)
count_angle(start_point=point, zero_angle=15, side_length=100, sides_count=3, color_id=user_color)

point = sd.get_point(600, 200)
count_angle(start_point=point, zero_angle=15, side_length=100, sides_count=4, color_id=user_color)

point = sd.get_point(600, 500)
count_angle(start_point=point, zero_angle=45, side_length=100, sides_count=5, color_id=user_color)

point = sd.get_point(300, 500)
count_angle(start_point=point, zero_angle=45, side_length=100, sides_count=6, color_id=user_color)

sd.pause()

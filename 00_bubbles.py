# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
point = sd.get_point(600, 300)


# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
def bubble(point, step, radius):
    for _ in range(3):
        sd.circle(point, radius)
        radius += step


# bubble(point, 5, 50)
# Нарисовать 10 пузырьков в ряд
def bubble_near(point_x, point_y, radius, count):
    for _ in range(count):
        center = sd.get_point(point_x, point_y)
        bubble(center, 5, radius)
        point_x += radius * 2


# bubble_near(100, 100, 50, 10)

# Нарисовать три ряда по 10 пузырьков
def bubble_near_and_bottom(point_x, point_y, radius, count_x, count_y):
    for __ in range(count_y):
        for _ in range(count_x):
            center = sd.get_point(point_x, point_y)
            bubble(center, 5, radius)
            point_x += radius * 2
        point_y += radius * 2
        point_x -= radius * 2 * count_x


# bubble_near_and_bottom(100, 100, 50, 10, 3)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for _ in range(100):
    point = sd.random_point()
    sd.circle(point, random.randint(30, 60), sd.random_color())

sd.pause()

# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd


# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

def smile(x, y, color):
    point_left = sd.get_point(x - 120, y - 100)
    point_right = sd.get_point(x, y)
    sd.ellipse(point_left, point_right, color)
    circle_point = sd.get_point(x - 35, y - 35)
    sd.circle(circle_point, 8, sd.invert_color(color))
    circle_point = sd.get_point(x - 85, y - 35)
    sd.circle(circle_point, 8, sd.invert_color(color))

    points = [
        sd.get_point(x - 85, y - 65),
        sd.get_point(x - 80, y - 70),
        sd.get_point(x - 75, y - 72),
        sd.get_point(x - 65, y - 74),
        sd.get_point(x - 61, y - 74),
        sd.get_point(x - 57, y - 74),
        sd.get_point(x - 47, y - 72),
        sd.get_point(x - 42, y - 70),
        sd.get_point(x - 37, y - 65),

        sd.get_point(x - 42, y - 75),
        sd.get_point(x - 47, y - 79),
        sd.get_point(x - 50, y - 81),
        sd.get_point(x - 57, y - 82),
        sd.get_point(x - 61, y - 82),
        sd.get_point(x - 65, y - 82),
        sd.get_point(x - 72, y - 80),
        sd.get_point(x - 75, y - 78),
        sd.get_point(x - 80, y - 75),
        sd.get_point(x - 85, y - 65),
    ]

    sd.lines(points, sd.invert_color(color))


for _ in range(10):
    smile(sd.randint(100, 600), sd.randint(100, 600), sd.random_color())

sd.pause()

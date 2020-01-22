# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
start_x, start_y = 50, 50
end_x, end_y = 350, 450
line_width = 20
# for i in range(7):
#     start_point = sd.get_point(start_x, start_y)
#     end_point = sd.get_point(end_x, end_y)
#     sd.line(start_point, end_point, rainbow_colors[i], line_width)
#     start_y += 5
#     end_y += 5

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
circle_center = sd.get_point(550, -200)
circle_start_radius = 600

for i in range(7):
    sd.circle(circle_center, circle_start_radius, rainbow_colors[i], line_width)
    circle_start_radius += 20

sd.pause()

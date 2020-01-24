# -*- coding: utf-8 -*-

# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)

import simple_draw as sd
import draw_library as dl

screen_width = 1400
screen_height = 1000
sd.resolution = (screen_width, screen_height)

# Радуга
rb_center = sd.get_point(500, -250)
rb_start_radius = 1100
rb_line_width = 18

dl.draw_rainbow(dl.rainbow_colors, rb_center, rb_start_radius, rb_line_width)

# Стена
brick_width, brick_height = 40, 20
wall_width, wall_height = 600, 400
start_wall_x, start_wall_y = 100, 80
wall_color = (255, 140, 0)

dl.draw_wall(wall_width, wall_height, brick_width, brick_height, start_wall_x, start_wall_y, wall_color)

# Окно
win_height = 160
win_width = 122
win_color = (240, 230, 140)
win_left_bottom = sd.get_point(wall_width/2 - win_width/2 + start_wall_x, wall_height/2 - win_height/4 + start_wall_y)
win_right_top = sd.get_point(wall_width/2 + win_width/2 + start_wall_x, wall_height/2 + win_height*3/4 + start_wall_y)

dl.draw_window(win_left_bottom, win_right_top, win_color)

dl.draw_smile(int(wall_width/2 + start_wall_x * 2)-40, int(wall_height/2 - start_wall_y) + 250, sd.COLOR_DARK_GREEN)

# Дерево
root_point = sd.get_point(1100, 290)
dl.draw_branches(root_point, 90, 45)

root_point = sd.get_point(750, 30)
dl.draw_branches(root_point, 90, 80)


sd.pause()

# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.

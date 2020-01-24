# -*- coding: utf-8 -*-
import simple_draw as sd

rainbow_colors = [sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE]


def draw_rainbow(rb_colors, center, start_radius, rb_line_width):
    for color in rb_colors:
        sd.circle(center, start_radius, color, rb_line_width)
        start_radius += rb_line_width


def draw_wall(wall_width, wall_height, brick_width, brick_height, wall_start_x, wall_start_y, color):

    border_line__left_start = sd.get_point(wall_start_x, wall_start_y)
    border_line_left_end = sd.get_point(wall_start_x, wall_start_y + wall_height)
    sd.line(border_line__left_start, border_line_left_end, color)  # Левая граница

    border_line_right_end = sd.get_point(wall_start_x + wall_width, wall_start_y + wall_height)
    border_line_right_start = sd.get_point(wall_start_x + wall_width, wall_start_y)
    sd.line(border_line_left_end, border_line_right_end, color)    # Верхняя граница
    sd.line(border_line_right_start, border_line_right_end, color)     # Правая граница

    for horizontal_line in range(wall_start_y, wall_height + wall_start_y, brick_height):
        start_line_point = sd.get_point(wall_start_x, horizontal_line)
        end_line_point = sd.get_point(wall_width + wall_start_x, horizontal_line)
        sd.line(start_line_point, end_line_point, color)

        if (horizontal_line + brick_height) % (brick_height * 2):
            x_shift = brick_width / 2
        else:
            x_shift = 0

        for vertical_line in range(wall_start_x, wall_width + wall_start_x, brick_width):
            start_line_point = sd.get_point(vertical_line + x_shift, horizontal_line)
            end_line_point = sd.get_point(vertical_line + x_shift, horizontal_line + brick_height)
            sd.line(start_line_point, end_line_point, color)


def rand_delta(number, percent=50, is_positive=False):
    if is_positive:
        rand = sd.random_number(0, percent * 10) / 1000
    else:
        rand = sd.random_number(-percent * 10, percent * 10) / 1000

    return number * rand


def branch_width_color(length):
    if length > 50:
        width = 4
        color = (139, 69, 19)
    elif length > 30:
        width = 3
        color = (128, 128, 0)
    elif length > 15:
        width = 2
        color = (107, 142, 35)
    elif length < 15:
        width = 1
        color = (124, 252, 0)

    return width, color


def draw_branches(start_point, start_angle, branch_length, width=1, color=(139, 69, 19)):

    if branch_length < 8:
        return

    width, color = branch_width_color(branch_length)

    start_point = sd.vector(start_point, start_angle, branch_length, color, width)
    delta = int(20 + rand_delta(30, percent=40))
    branch_length *= (.75 + rand_delta(0.75, percent=20, is_positive=True))
    shift_angle = start_angle + delta
    draw_branches(start_point, shift_angle, branch_length, width, color)

    shift_angle = start_angle - delta
    draw_branches(start_point, shift_angle, branch_length, width, color)


def draw_smile(x, y, color):
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


def draw_window(left_bottom, right_top, color):
    sd.rectangle(left_bottom, right_top, color)


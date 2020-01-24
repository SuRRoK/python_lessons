# -*- coding: utf-8 -*-
import simple_draw as sd

rainbow_colors = [sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE]


def draw_rainbow(rb_colors, center, start_radius, rb_line_width):
    for color in rb_colors:
        sd.circle(center, start_radius, color, rb_line_width)
        start_radius += rb_line_width
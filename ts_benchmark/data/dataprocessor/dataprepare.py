# -*- coding: utf-8 -*-
import os
from ts_benchmark.common.constant import ROOT_PATH
from typing import List


def prepare_data() -> List[str]:
    """
    prepare data organised as time/number, value, and channel.
    return: a list of data set
    """
    data_path = os.path.join(ROOT_PATH, "dataset", "interpolated.xlsx")
    correlation_path = os.path.join(ROOT_PATH, "dataset", "correlation.xlsx")

    a = []
    return a


import turtle


def draw_dragon():
    window = turtle.Screen()
    window.bgcolor("white")

    dragon = turtle.Turtle()
    dragon.shape("turtle")
    dragon.color("green")
    dragon.speed(10)

    def dragon_curve(t, order, size):
        if order == 0:
            t.forward(size)
        else:
            t.right(45)
            dragon_curve(t, order - 1, size)
            t.left(90)
            dragon_curve(t, order - 1, size)
            t.right(45)

    dragon.penup()
    dragon.goto(-200, 0)
    dragon.pendown()
    dragon_curve(dragon, 10, 10)

    window.exitonclick()


draw_dragon()

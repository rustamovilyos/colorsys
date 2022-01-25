import colorsys
# import tkinter
from turtle import *
import random

t = Turtle()
s = Screen()
s.bgcolor('Black')
t.speed(0.0001)
hue = 0.0
n = 30
h = 0

for i in range(360):
    c = colorsys.hsv_to_rgb(hue, 0.7, 0.7)
    t.color(c)
    t.left(40)
    hue += 0.6
    fd(i)
    # rand = random.randint(1, 2)
    # rand1 = random.randint(2, 5)
    for j in range(1, 30, 4):
        t.forward(230)
        t.left(125)

# t = Turtle()
# s = Screen()
# s.bgcolor('Black')
# t.speed(0)
# n = 38
# h = 0
# hue = 0.0
#
# for i in range(360):
#     c = colorsys.hsv_to_rgb(hue, 1, 0.7)
#     t.color(c)
#     t.left(20)
#     hue += 0.01
#     # rand = random.randint(1)
#     # rand1 = random.randint(8, 9)
#     for j in range(24):
#         t.forward(120)
#         # t.write('LORD')
#         t.left(60)
#         # t.back(10)
#         # t.clone()
#         # t.right(60)
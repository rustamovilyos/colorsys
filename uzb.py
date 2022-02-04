"""
#sariq va qizil rangli uchburchakdan iborat to'g'ri to'rtburchak 
turtle.color('white')
turtle.setx(-300)
turtle.sety(0)
turtle.color('black')
turtle.fillcolor('yellow')
turtle.begin_fill()
turtle.shapesize(0.4)
turtle.shape('circle')
turtle.speed(1)
turtle.forward(120)
turtle.goto(-300, 200)
turtle.goto(-300, 0)
turtle.end_fill()

turtle.setx(-300)
turtle.sety(0)
turtle.fillcolor('red')
turtle.begin_fill()
turtle.forward(120)
turtle.goto(-180, 200)
turtle.goto(-300, 200)
turtle.goto(-180, 0)
turtle.end_fill()
turtle.exitonclick()
"""

""" The flag of Uzbekistan """

import turtle
from turtle import Screen

# beginning
flag = turtle.Turtle()
screen = Screen().setup(width=.99, height=.99)

print(screen)
flag.speed(4)
flag.shapesize(0.1)
flag.shape('square')
flag.color('white')
flag.setx(-350)
flag.sety(250)

# blue sector
flag.color('black')
flag.fillcolor('blue')
flag.begin_fill()
flag.forward(750)
flag.goto(400, 100)
flag.back(750)
flag.goto(-350, 250)
flag.goto(-350, 100)
flag.end_fill()

# red sector up
flag.color('black')
flag.fillcolor('red')
flag.begin_fill()
flag.goto(-350, 95)
flag.forward(750)
flag.goto(400, 100)
flag.back(750)
flag.goto(-350, 95)
flag.end_fill()

# white sector
flag.color('black')
flag.fillcolor('')
flag.begin_fill()
flag.goto(-350, -55)
flag.forward(750)
flag.goto(400, 95)
flag.back(750)
flag.goto(-350, -55)
flag.end_fill()

# red sector up
flag.color('black')
flag.fillcolor('red')
flag.begin_fill()
flag.goto(-350, -60)
flag.forward(750)
flag.goto(400, -55)
flag.back(750)
flag.goto(-350, -60)
flag.end_fill()

# white green
flag.color('black')
flag.fillcolor('green')
flag.begin_fill()
flag.goto(-350, -210)
flag.forward(750)
flag.goto(400, -60)
flag.back(750)
flag.goto(-350, -210)
flag.end_fill()

# moon
flag.speed(10)
flag.up()
flag.goto(-260, 150)
flag.color('white')
flag.begin_fill()
flag.circle(38)
flag.end_fill()
flag.up()
flag.goto(-250, 156)
flag.color('blue')
flag.begin_fill()
flag.circle(32)
flag.end_fill()

# Starting a Working Screen
star = turtle.Screen()

# initializing a turtle instance
geekyTurtle = turtle.Turtle()

# first line 3 stars
for j in range(1):
    geekyTurtle.speed(0.1)
    geekyTurtle.color('')
    geekyTurtle.setx(-175)
    geekyTurtle.sety(210)
    # executing loop 5 times for a star
    for i in range(5):
        geekyTurtle.shapesize(0.1)
        geekyTurtle.shape('square')
        geekyTurtle.color('')
        # moving turtle 100 units forward
        geekyTurtle.color('white')
        geekyTurtle.forward(12)
        # rotating turtle 144 degree right
        geekyTurtle.right(144)

for x in range(1):
    geekyTurtle.speed(8)
    geekyTurtle.color('')
    geekyTurtle.setx(-155)
    geekyTurtle.sety(210)
    # executing loop 5 times for a star
    for y in range(5):
        geekyTurtle.shapesize(0.1)
        geekyTurtle.shape('square')
        geekyTurtle.color('')
        # moving turtle 100 units forward
        geekyTurtle.color('white')
        geekyTurtle.forward(12)
        # rotating turtle 144 degree right
        geekyTurtle.right(144)

for j in range(1):
    geekyTurtle.speed(8)
    geekyTurtle.color('')
    geekyTurtle.setx(-135)
    geekyTurtle.sety(210)
    # executing loop 5 times for a star
    for i in range(5):
        geekyTurtle.shapesize(0.1)
        geekyTurtle.shape('square')
        geekyTurtle.color('')
        # moving turtle 100 units forward
        geekyTurtle.color('white')
        geekyTurtle.forward(12)
        # rotating turtle 144 degree right
        geekyTurtle.right(144)

# second line 4stars
for x in range(1):
    geekyTurtle.speed(8)
    geekyTurtle.color('')
    geekyTurtle.setx(-195)
    geekyTurtle.sety(190)
    # executing loop 5 times for a star
    for y in range(5):
        geekyTurtle.shapesize(0.1)
        geekyTurtle.shape('square')
        geekyTurtle.color('')
        # moving turtle 100 units forward
        geekyTurtle.color('white')
        geekyTurtle.forward(12)
        # rotating turtle 144 degree right
        geekyTurtle.right(144)

for j in range(1):
    geekyTurtle.speed(8)
    geekyTurtle.color('')
    geekyTurtle.setx(-175)
    geekyTurtle.sety(190)
    # executing loop 5 times for a star
    for i in range(5):
        geekyTurtle.shapesize(0.1)
        geekyTurtle.shape('square')
        geekyTurtle.color('')
        # moving turtle 100 units forward
        geekyTurtle.color('white')
        geekyTurtle.forward(12)
        # rotating turtle 144 degree right
        geekyTurtle.right(144)

for x in range(1):
    geekyTurtle.speed(8)
    geekyTurtle.color('')
    geekyTurtle.setx(-155)
    geekyTurtle.sety(190)
    # executing loop 5 times for a star
    for y in range(5):
        geekyTurtle.shapesize(0.1)
        geekyTurtle.shape('square')
        geekyTurtle.color('')
        # moving turtle 100 units forward
        geekyTurtle.color('white')
        geekyTurtle.forward(12)
        # rotating turtle 144 degree right
        geekyTurtle.right(144)

for j in range(1):
    geekyTurtle.speed(8)
    geekyTurtle.color('')
    geekyTurtle.setx(-135)
    geekyTurtle.sety(190)
    # executing loop 5 times for a star
    for i in range(5):
        geekyTurtle.shapesize(0.1)
        geekyTurtle.shape('square')
        geekyTurtle.color('')
        # moving turtle 100 units forward
        geekyTurtle.color('white')
        geekyTurtle.forward(12)
        # rotating turtle 144 degree right
        geekyTurtle.right(144)

# third line 5stars
for x in range(1):
    geekyTurtle.speed(8)
    geekyTurtle.color('')
    geekyTurtle.setx(-215)
    geekyTurtle.sety(170)
    # executing loop 5 times for a star
    for y in range(5):
        geekyTurtle.shapesize(0.1)
        geekyTurtle.shape('square')
        geekyTurtle.color('')
        # moving turtle 100 units forward
        geekyTurtle.color('white')
        geekyTurtle.forward(12)
        # rotating turtle 144 degree right
        geekyTurtle.right(144)
for x in range(1):
    geekyTurtle.speed(8)
    geekyTurtle.color('')
    geekyTurtle.setx(-195)
    geekyTurtle.sety(170)
    # executing loop 5 times for a star
    for y in range(5):
        geekyTurtle.shapesize(0.1)
        geekyTurtle.shape('square')
        geekyTurtle.color('')
        # moving turtle 100 units forward
        geekyTurtle.color('white')
        geekyTurtle.forward(12)
        # rotating turtle 144 degree right
        geekyTurtle.right(144)

for j in range(1):
    geekyTurtle.speed(8)
    geekyTurtle.color('')
    geekyTurtle.setx(-175)
    geekyTurtle.sety(170)
    # executing loop 5 times for a star
    for i in range(5):
        geekyTurtle.shapesize(0.1)
        geekyTurtle.shape('square')
        geekyTurtle.color('')
        # moving turtle 100 units forward
        geekyTurtle.color('white')
        geekyTurtle.forward(12)
        # rotating turtle 144 degree right
        geekyTurtle.right(144)

for x in range(1):
    geekyTurtle.speed(8)
    geekyTurtle.color('')
    geekyTurtle.setx(-155)
    geekyTurtle.sety(170)
    # executing loop 5 times for a star
    for y in range(5):
        geekyTurtle.shapesize(0.1)
        geekyTurtle.shape('square')
        geekyTurtle.color('')
        # moving turtle 100 units forward
        geekyTurtle.color('white')
        geekyTurtle.forward(12)
        # rotating turtle 144 degree right
        geekyTurtle.right(144)

for j in range(1):
    geekyTurtle.speed(8)
    geekyTurtle.color('')
    geekyTurtle.setx(-135)
    geekyTurtle.sety(170)
    # executing loop 5 times for a star
    for i in range(5):
        geekyTurtle.shapesize(0.1)
        geekyTurtle.shape('square')
        geekyTurtle.color('')
        # moving turtle 100 units forward
        geekyTurtle.color('white')
        geekyTurtle.forward(12)
        # rotating turtle 144 degree right
        geekyTurtle.right(144)
turtle.exitonclick()

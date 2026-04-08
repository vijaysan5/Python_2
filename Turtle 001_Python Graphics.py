"""___point >>> x=0,y=0 center point___"""

from turtle import *

# Draw line
"""forward(100)
left(200)
forward(100)
right(200)
forward(200)
right(100)
forward(150)
left(100)
forward(150)
#clearscreen()
done()"""


"___fill Color___"
"""color("red")
fillcolor("lightpink")
width(3)
begin_fill()
for x in range(4):
    forward(100)
    left(90)
    forward(100)
end_fill()
done()""" 



"_____Draw a black and white box (3x3)_____"
"""begin_fill()
width(3)
for x in range(4):
    backward(100)
    right(90)
end_fill()
right(90)
forward(100)

begin_fill()
for x in range(3):
    left(90)
    forward(100)
end_fill()

forward(200)
begin_fill()
for x in range(3):
    left(90)
    forward(100)
end_fill()

forward(200)
begin_fill()
for x in range(3):
    left(90)
    forward(100)
end_fill()

forward(200)
begin_fill()
for x in range(3):
    left(90)
    forward(100)
end_fill()

forward(100)
left(90)
forward(100)
left(90)
forward(200)
for a in range(3):
    left(90)
    forward(300)
done()"""




"______penup and pendown______"
forward(100)
right(90)
penup()
forward(100)

right(90)
pendown()
forward(100)
hideturtle()              # hide >>> Arrow
#shape("turtle")          # Show Turtle mark insed of Arrow
done()
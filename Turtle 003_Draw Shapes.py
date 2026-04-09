from turtle import *

#_____Draw a Square Shape
"""for x in range(4):
    width(3)
    left(90)
    forward(100)
hideturtle()
done()"""


#_____Draw a Circle Shape
"""bgcolor("Black")
fillcolor("white")
begin_fill()
circle(123)
end_fill()
hideturtle()
done()"""


#_____Draw a Star Shape
"""width(3)
right(144)
forward(100)
for a in range(4):
    right(144)
    forward(100)
hideturtle()
done()"""


#_____Draw a Hexagon
width(3)
side = "6 >>> circle - 360/6 === 60"
"""for x in range(6):
    forward(150)
    right(60)
hideturtle()
done()"""

#_____Draw a Pentagon
"""for x in range(5):
    forward(150)
    left(72)
hideturtle()
done()"""

#_____Draw a Continue Square
"""import turtle 
wind = turtle.Screen()
wind.bgcolor("lightblue")
show = turtle.Turtle()
show.color("blue")

def square(size):
    for x in range(4):
        show.forward(size)
        show.right(90)
        size = size+2.5
square(6)
square(16)
square(26)
square(36)
square(46)
square(56)
square(66)
square(76)
square(86)
square(96)
square(106)
square(116)
square(126)
square(136)
hideturtle()
done()"""

#_____Draw a Continue Hexagon
"""import turtle
cool = ['red', 'blue', 'green', 'yellow', 'pink', 'white']
show = turtle.Pen()
turtle.bgcolor("black")
for x in range(360):
    show.speed(0)
    show.pencolor(cool[x%6])
    show.width(x//50+1)
    show.forward(x)
    show.left(59)"""

#_____Draw a Continue Circle
"""import turtle
turtle.Screen()
turtle.speed(0)

for x in range(50):
    turtle.circle(5*x)
    turtle.circle(-5*x)
    turtle.left(x)
turtle.exitonclick()"""

#_____Draw a Continue Star
"""color('navyblue')
width(1)
fillcolor('lightblue')
begin_fill()
while True:
    speed(0)
    forward(500)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
exitonclick()
hideturtle()
done()"""

"""import turtle
wind = turtle.Screen()
wind.title("Turtle Moving on Screen")

mov = turtle.Turtle()
mov.shape("turtle")
mov.color("navyblue")
# mov.penup()

def movetoclick(x,y):
    mov.goto(x,y)
    print(f"Turtle move to ({x}, {y})")

wind.onclick(movetoclick)
wind.mainloop()"""
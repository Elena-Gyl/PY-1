from turtle import *
from time import sleep
from random import randint

# def draw_window():
#     color('yellow')
#     begin_fill()
#     for i in range(4):
#         forward(15)
#         left(90)
#     end_fill()
#
# penup()
# goto(-170,-170)
# pendown()
# color('gray')
# begin_fill()
# for i in range(2):
#     forward(100)
#     left(90)
#     forward(200)
#     left(90)
# end_fill()
#
# for row in range(6):
#     for col in range(2):
#         penup()
#         goto(-145 + col * 30,-155 + row * 30)
#         pendown()
#         draw_window()


width = 300
height = 300
t = Turtle()
t.penup()
t.goto(-width, -height)
t.pendown()
t.speed(0)
t.color("lightgreen")
t.begin_fill()
for i in range(2):
    t.forward(width*2)
    t.left(90)
    t.forward(height*2)
    t.left(90)
t.end_fill()


t1 = Turtle()
t1.color("red")
t1.shape('turtle')
t1.width(5)

t2 = Turtle()
t2.color("yellow")
t2.shape('turtle')
t2.left(120)
t2.width(5)

t3 = Turtle()
t3.color("blue")
t3.shape('turtle')
t3.left(240)
t3.width(5)

def catch_t1(x,y):
    t1.penup()
    t1.goto(randint(-width, width),randint(-height, height))
    t1.pendown()
    t1.left(randint(0, 360))

def catch_t2(x,y):
    t2.penup()
    t2.goto(randint(-width, width),randint(-height, height))
    t2.pendown()
    t2.left(randint(0, 360))

def catch_t3(x,y):
    t3.penup()
    t3.goto(randint(-width, width),randint(-height, height))
    t3.pendown()
    t3.left(randint(0, 360))

def gamestop(t1, t2, t3):
    t1_outside = (abs(t1.xcor()) > width or
                  abs(t1.ycor()) > height)
    t2_outside = (abs(t2.xcor()) > width or
                  abs(t2.ycor()) > height)
    t3_outside = (abs(t3.xcor()) > width or
                  abs(t3.ycor()) > height)
    t_outside = t1_outside or t2_outside or t3_outside
    return t_outside


t1.onclick(catch_t1)
t2.onclick(catch_t2)
t3.onclick(catch_t3)

while gamestop(t1, t2, t3) != True:
    t1.forward(7)
    t2.forward(7)
    t3.forward(7)
    sleep(0.1)


else:
    t1.clear()
    t2.clear()
    t3.clear()
    t1.penup()
    t1.goto(-80,0)
    t1.write('Игра завершена', font=('Times New Roman', 24))
    t1.hideturtle()
    t2.hideturtle()
    t3.hideturtle()


mainloop()
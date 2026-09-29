from turtle import *

shape('turtle')
pensize(4)
speed(0.5)
# color("blue", '#27F5DD')
colormode(255)

# begin_fill()
# for _ in range(4):
#     forward(100)
#     left(90)
# end_fill()

pencolor('#A30080')
# begin_fill()
# for _ in range(3):
#     forward(100)
#     left(120)
# end_fill()

# fd(100)
# backward(100)
# penup()
# goto(-100,100)
# pendown()
r = 245
g = 39
b = 90
step = 0
for i in range(200, 10, -20):
    fillcolor(r, g, b)
    for _ in range(6):
        begin_fill()
        for _ in range(3):
            forward(i)
            left(120)
    #     circle(i)
        end_fill()
        rt(60)
    #r -= 90
    b += 10
    g += 10
    # penup()
    # step = step - i
    # goto(step,0)
    # pendown()
penup()
goto(0,0)
pendown()

mainloop()

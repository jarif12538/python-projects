from turtle import bgcolor, color, done, end_fill, begin_fill, forward, goto, pensize, penup, right, setheading, speed, pendown, Screen
import colorsys

screen = Screen()
screen.colormode(255)

speed(10)
bgcolor("white")
pensize(2)

num = 36
ang = 360 / num

for i in range(num):
    h = i / num
    r, g, b = colorsys.hsv_to_rgb(h, 1, 1)
    '''Convert to 0-255 range for RGB'''
    r, g, b = int(r * 255), int(g * 255), int(b * 255)
    color(r, g, b)
    penup()
    goto(0, 0)
    setheading(ang * i)
    forward(200)
    pendown()
    begin_fill()
    right(90)
    forward(150)
    right(60)
    forward(50)
    right(120)
    forward(50)
    right(60)
    forward(150)
    end_fill()
    penup()
done()

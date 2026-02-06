from turtle import bgcolor, color, done, forward, goto, left, pensize, setheading, speed, Screen

screen = Screen()
screen.colormode(255)
screen.title("Classical Rosette")

speed(6)
bgcolor("ivory")
pensize(2)

num = 24
ang = 360 / num

palette = [
    (45, 34, 26),
    (92, 76, 56),   
    (140, 116, 84), 
    (70, 58, 44),   
]
for index in range(num):
    color(palette[index % len(palette)])
    for arm in range(4):
        goto(0, 0)
        setheading(ang * index + (arm * 90))
        forward(180)
        left(90)
        arc = 120
        forward(arc)
        left(45)
        forward(40)
        left(90)
        forward(40)
        left(45)
        forward(arc)
done()
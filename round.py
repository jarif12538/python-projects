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
    (45, 34, 26),   # dark umber
    (92, 76, 56),   # warm brown
    (140, 116, 84), # tan
    (70, 58, 44),   # walnut
]


import turtle 
import random

window = turtle.Screen()
tommy = turtle.Turtle()
tommy.color('green')
tommy.shape('turtle')
tommy.speed(0)

distance = 10
angle = 90
is_in_screen = True 

colors = ["green", "blue", "purple"]

while is_in_screen: 
    coin = random.randrange(0,2)
    if coin == 0: 
        tommy.left(angle)
    elif coin == 1: 
        tommy.right(angle)
    tommy.forward(distance)

    x = tommy.xcor()
    y = tommy.ycor()

    xrange = window.window_width()/2
    yrange = window.window_height()/2

    tommy.color(colors[0])
    colors.append(colors.pop(0))

    if abs(x) > xrange or abs(y) > yrange: 
        is_in_screen = False
window.bgcolor('lightblue')
window.exitonclick()
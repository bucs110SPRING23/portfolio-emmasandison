import turtle

window = turtle.Screen()

window.bgcolor('green')

t = turtle.Turtle()
t.color('pink')
t.shape('turtle')
n = int(input("Enter the number of the sides of the shape : "))

l = int(input("Enter the length of the sides of the polygon : "))

for _ in range (n):
    turtle.forward(l)
    turtle.right(360 / n)

window.exitonclick()
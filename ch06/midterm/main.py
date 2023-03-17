import turtle 
window = turtle.Screen()
window.bgcolor('lightblue')


def mountains(color): 
    triangle = turtle.Turtle()
    triangle.forward(100)
    triangle.left(120)
    triangle.forward(100)
    triangle.left(120)
    triangle.forward(100)
    turtle.done()

def main():
    mountains("grey")

main()


    






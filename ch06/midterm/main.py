import turtle 
window = turtle.Screen()
window.bgcolor('lightblue')

def grass(color): 
    grassland = turtle.Turtle()
    grassland.penup()
    grassland.goto(-400,-200)
    grassland.pendown()
    grassland.color("limegreen")
    grassland.begin_fill()
    grassland.forward(800)
    grassland.right(90)
    grassland.forward(2000)
    grassland.right(90)
    grassland.end_fill()
    grassland.hideturtle()

def mountain1(color): 
    triangle1 = turtle.Turtle()
    triangle1.hideturtle()
    triangle1.penup()
    triangle1.goto(-350,-200)
    triangle1.pendown()
    triangle1.showturtle()
    triangle1.color("grey")
    triangle1.begin_fill()
    triangle1.forward(250)
    triangle1.left(120)
    triangle1.forward(300)
    triangle1.left(120)
    triangle1.forward(300)
    triangle1.right(180)
    triangle1.end_fill()
    triangle1.hideturtle()

def mountain2(color): 
    triangle2 = turtle.Turtle()
    triangle2.hideturtle()
    triangle2.penup()
    triangle2.goto(-125,-200)
    triangle2.pendown()
    triangle2.showturtle()
    triangle2.color("darkgrey")
    triangle2.begin_fill()
    triangle2.forward(250)
    triangle2.left(120)
    triangle2.forward(400)
    triangle2.left(120)
    triangle2.forward(400)
    triangle2.right(180)
    triangle2.end_fill()
    triangle2.hideturtle()

def mountain3(color): 
    triangle3 = turtle.Turtle()
    triangle3.hideturtle()
    triangle3.penup()
    triangle3.goto(100,-200)
    triangle3.pendown()
    triangle3.showturtle()
    triangle3.color("grey")
    triangle3.begin_fill()
    triangle3.forward(250)
    triangle3.left(120)
    triangle3.forward(300)
    triangle3.left(120)
    triangle3.forward(300)
    triangle3.right(180)
    triangle3.end_fill()
    triangle3.hideturtle()

def leftsnowcap(color): 
    leftsnow = turtle.Turtle()
    leftsnow.penup()
    leftsnow.goto(-290,-10)
    leftsnow.pendown()
    leftsnow.color("white")
    leftsnow.begin_fill()
    leftsnow.left(35)
    leftsnow.forward(30)
    leftsnow.right(90)
    leftsnow.forward(10)
    leftsnow.left(100)
    leftsnow.forward(25)
    leftsnow.right(85)
    leftsnow.forward(40)
    leftsnow.left(160)
    leftsnow.forward(82)
    leftsnow.end_fill()
    leftsnow.hideturtle()


def middlesnowcap(color): 
    middlesnow = turtle.Turtle()
    middlesnow.penup()
    middlesnow.goto(-150,15)
    middlesnow.pendown()
    middlesnow.color("white")
    middlesnow.begin_fill()
    middlesnow.left(35)
    middlesnow.forward(60)
    middlesnow.right(90)
    middlesnow.forward(30)
    middlesnow.left(100)
    middlesnow.forward(45)
    middlesnow.right(85)
    middlesnow.forward(70)
    middlesnow.left(160)
    middlesnow.forward(155)
    middlesnow.end_fill()
    middlesnow.hideturtle()

def rightsnowcap(color): 
    rightsnow = turtle.Turtle()
    rightsnow.penup()
    rightsnow.goto(160,-10)
    rightsnow.pendown()
    rightsnow.color("white")
    rightsnow.begin_fill()
    rightsnow.left(35)
    rightsnow.forward(30)
    rightsnow.right(90)
    rightsnow.forward(10)
    rightsnow.left(100)
    rightsnow.forward(25)
    rightsnow.right(85)
    rightsnow.forward(40)
    rightsnow.left(160)
    rightsnow.forward(82)
    rightsnow.end_fill()
    rightsnow.hideturtle()

def sun(color): 
    circle = turtle.Turtle()
    circle.penup()
    circle.goto(200,175)
    circle.pendown()
    circle.color("yellow")
    circle.begin_fill()
    circle.circle(75)
    circle.end_fill()
    circle.hideturtle()

def tree(): 
    trees = turtle.Turtle()
    trees.goto()
    trees.color("brown")
    trees.begin_fill()
    trees.forward(10)
    trees.left(90)
    trees.forward(30)
    trees.left(90)
    trees.forward(10)
    trees.left(90)
    trees.forward(30)    
    trees.end_fill()

    trees.right(180)
    trees.forward(30)
    trees.right(90)
    trees.forward(5)

    trees.color("darkgreen")
    trees.begin_fill()
    trees.circle(15)
    trees.end_fill()

    trees.right(90)

    trees.hideturtle()
    # return tree

def tree1(color):
    firsttree = turtle.Turtle()
    firsttree.penup()
    firsttree.goto(-200,-200)
    firsttree.pendown()
    tree()
    firsttree.hideturtle()

def tree2(color): 
    secondtree = turtle.Turtle()
    secondtree.penup()
    secondtree.goto(-200,-500)
    secondtree.pendown()
    tree()
    secondtree.hideturtle()

def tree3(color): 
    thirdtree = turtle.Turtle()
    thirdtree.penup()
    thirdtree.goto(-200,-500)
    thirdtree.pendown()
    tree()
    thirdtree.hideturtle()
    turtle.done()


def main():
    grass("limegreen")
    mountain1("grey")
    mountain2("darkgrey")
    mountain3("grey")
    leftsnowcap("white")
    middlesnowcap("white")
    rightsnowcap("white")
    sun("yellow")
    tree1("green")
    tree2("green")
    tree3("green")

    
main()


    






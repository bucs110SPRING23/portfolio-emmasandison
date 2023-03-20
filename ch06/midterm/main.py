import turtle 
window = turtle.Screen()
window.bgcolor('lightblue')

def grass(color): 
    """
    This function draws the grass
    args: color (string)
    """
    grassland = turtle.Turtle()
    grassland.penup()
    grassland.goto(-400,-200)
    grassland.pendown()
    grassland.color("limegreen")
    grassland.begin_fill()
    grassland.forward(800)
    grassland.right(90)
    grassland.forward(1800)
    grassland.right(90)
    grassland.end_fill()
    grassland.hideturtle()

def mountain1(color): 
    """
    This function draws the left mountain
    args: color (string)
    """
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
    """
    This function draws the middle mountain
    args: color (string)
    return: triangle2
    """
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
    """
    This function draws the right mountain
    args: color (string)
    """
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
    """
    This function draws the left snow cap
    args: color (string)
    """
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
    """
    This function draws the middle snow cap 
    args: color (string)
    """
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
    """
    This function draws the right snow cap 
    args: color (string)
    """
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
    """
    This function draws the sun 
    args: color (string)
    """
    circle = turtle.Turtle()
    circle.penup()
    circle.goto(200,175)
    circle.pendown()
    circle.color("yellow")
    circle.begin_fill()
    circle.circle(75)
    circle.end_fill()
    circle.hideturtle()

def tree1():
    """
    This function draws the trees
    """
    firsttree = turtle.Turtle()
    firsttree.penup()
    firsttree.goto(-300,-300)
    firsttree.pendown()
    firsttree.color("brown")
    firsttree.begin_fill()
    firsttree.forward(10)
    firsttree.left(90)
    firsttree.forward(30)
    firsttree.left(90)
    firsttree.forward(10)
    firsttree.left(90)
    firsttree.forward(30)
    firsttree.end_fill()

    firsttree.right(180)
    firsttree.forward(30)
    firsttree.right(90)
    firsttree.forward(5)

    firsttree.color("darkgreen")
    firsttree.begin_fill()
    firsttree.circle(20)
    firsttree.end_fill()

    firsttree.right(90)

    firsttree.hideturtle()

def tree2():
    """
    This function draws another tree
    """
    secondtree = turtle.Turtle()
    secondtree.penup()
    secondtree.goto(-150,-250)
    secondtree.pendown()
    secondtree.color("brown")
    secondtree.begin_fill()
    secondtree.forward(10)
    secondtree.left(90)
    secondtree.forward(30)
    secondtree.left(90)
    secondtree.forward(10)
    secondtree.left(90)
    secondtree.forward(30)
    secondtree.end_fill()

    secondtree.right(180)
    secondtree.forward(30)
    secondtree.right(90)
    secondtree.forward(5)

    secondtree.color("darkgreen")
    secondtree.begin_fill()
    secondtree.circle(20)
    secondtree.end_fill()

    secondtree.right(90)

    secondtree.hideturtle()

def tree3():
    """
    This function draws another tree
    """
    thirdtree = turtle.Turtle()
    thirdtree.penup()
    thirdtree.goto(100,-300)
    thirdtree.pendown()
    thirdtree.color("brown")
    thirdtree.begin_fill()
    thirdtree.forward(10)
    thirdtree.left(90)
    thirdtree.forward(30)
    thirdtree.left(90)
    thirdtree.forward(10)
    thirdtree.left(90)
    thirdtree.forward(30)
    thirdtree.end_fill()

    thirdtree.right(180)
    thirdtree.forward(30)
    thirdtree.right(90)
    thirdtree.forward(5)

    thirdtree.color("darkgreen")
    thirdtree.begin_fill()
    thirdtree.circle(20)
    thirdtree.end_fill()

    thirdtree.right(90)

    thirdtree.hideturtle()

    turtle.done()

def givearanking(num): 
    rank = num + 10 
    return rank

def main():
    grass("limegreen")
    mountain1("grey")
    mountain2("darkgrey")
    mountain3("grey")
    leftsnowcap("white")
    middlesnowcap("white")
    rightsnowcap("white")
    sun("yellow")
    tree1()
    tree2()
    tree3()
    result = givearanking(100)
    print("I ranked this drawing a", result)

main()

window.exitonclick()





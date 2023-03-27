
# 1. look in the current folder for the file/module
# 2. look in python installed modules 
# 3. look in the python library 
import point 
import random 
import turtle 
# import module
# good practice to make a new file for a new class 
# remember an example of a class is turtle and the creating the turtle object would be a point class 

p1 = point.Point() # initialize a Point object 

p2 = point.Point(3, 4, "yellow") # initialize another Point object

p1.xcoor = 10

print(p1.xcoor, p1.ycoor, p1.color, type(p1), id(p1))
print(p2.xcoor, p2.ycoor, p2.color, type(p2), id(p2))

# cases 
# - snake_case: snake_case: underscores for spaces, all lowercase (common for C)
# - camelCase: camelCase, starts lowercase, capital for spaces (common for Java)
# - TitleCase: TitleCase, capital for spaces, starts capital (usually means the definition of that class will never change)

points = []
for p in range(10): 
    x = random.randint(0, 250)
    y = random.randint(0, 250)
    points.append(point.Point(x, y))

t = turtle.Turtle()
for p in points: 
    p.random_color()
    t.color(p.color)
    t.goto(p.xcoor, p.ycoor)

turtle.Screen().exitonclick() 

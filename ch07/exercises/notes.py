# managing complexity - advanced programming just manages complexity 
# Unix - 10000 SLOC (source lines of code)
# Chrome - 10,000,000 SLOC
# OS X - 100,000,000 SLOC

# Complex Objects 
# - primitives: int, str, float, lists, dict, tuple 
# - turtle: x(int), y(int), heading, color(color), pensize(int), shape(str)

# bundle data and functions together 
# - state: the current values of the data in the object 
# - behavior: the functions that operate on the date in the object 

# Point 
# - object should do one thing
# - state: x, y, color 
# behavior: change_color, move 

# Classes == Type 
import turtle 

t = turtle.Turtle()
print(type(t)) # complex 
print(type(1)) # primitive 

# class are blueprint for objects 
# - functions are stored in algorithms 
# - class as a stored data type 
# - classes are not executable 
# - don't put executable code in global scope, definitions are fine 

# Point class
# - instance: an object created from a specific class 
#  - t = turtle.Turtle() # t is an instance of Turtle
# - instance variable: an internal variable that is part of an instance
#  - t.x, t.pos # x and pos are instance variables
# - interface: the functions and variables of an object 
#  - t.forward() # .forward() part of the interface of turtle 

# Point - make it a class ourselves 

# def make_point(x, y): 
class Point: 
    # user types (or classes) always start with a capital letter
    # usually, classes go in their own file 
    # 1 class per file 
    # - dunders = double underscores on both sides of the name 
    # adding self.var ties the scope of var to the object scope 

    def __init__(self): # self is the instance being created 
        self.x = 0 # dot operator accesses instance variables of object 
        self.y = 0 # create this instance (self) and then create y which is tied to scope of self 
        color = ""
    pass 

### main.py
import point

p1 = point.Point() # p1 is an instance of Point, Point is a class 
p1.x = 10

p2 = point.Point() # p2 is an instance of Point, Point is a class (type)
p2.x = 5

# state of p1(x = 10, y = 0, color = ""),
# state of p2( x = 5, y = 0, color = "")

p1.color = "red"
# state of p1(x = 10, y = 0, color = "red")


# MVC - Model View Controller 
# for GUI programs 
# like the accumulator pattern (for common programs)
# Design Patterns - language independent 

# View: displays things on screen 
#   - pygame 
#   - turtle 

# Controller: controls things on screen 
#   - keyboard 

# - Model 
# - a class 
# - contains data for the program 


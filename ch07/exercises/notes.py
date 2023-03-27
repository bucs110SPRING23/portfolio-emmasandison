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

print(type(turtle.Turtle()))

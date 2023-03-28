"""
does stuff
"""

import random

# blueprint for an object 
# def graph_point(): 
# class == type 
# class are names with TitleCase

class ColorPoint: 
    """doctring for Point"""
    # first parameter to any method is 'self' - self is the instance being created 
    def __init__(self, x=0, y=0, color="red"):
        self.xcoor = abs(x)
        self.ycoor = abs(y)
        self.color = color 

    def random_color(self): 
        colors = ["red", "green", "blue", "yellow", "orange", "purple"]
        self.color = random.choice(colors)

    # no return 
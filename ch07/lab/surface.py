from Rectangle import Rectangle

class Surface: 
    def __init__(self, filename, x, y, height, width):
        self.rect = Rectangle(x, y, height, width)
        self.image = filename 

    def getRect(self): 
        """
        This function returns the variable self.rect which is a rectangle created in the Rectangle class
        """
        return self.rect

        

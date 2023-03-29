class Rectangle: 
   def __init__(self, x, y, height, width): 
      self.x = abs(x)
      self.y = abs(y)
      self.height = abs(height)
      self.width = abs(width)

   def __str__(self):
      """This function returns the parameters of the __init__ in a string 
      """
      return F"x:{self.x} y:{self.y} width{self.width} height:{self.height}" 

# Rectangle (500, 500, 25, 50)




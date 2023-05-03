class Text:
  def __init__(self, x, y):
    """
    Initialize the text object
    args: x, y indicate the position of the text
    """
    self.color = "black" 
    self.msg = ""  
    self.fontsize = 15  

class Mushroom:
  def __init__(self, mnum=1):
    """
    Initialize the mushroom object
    args: mnum indicates the number of mushrooms at once 
    """
    self.speed = 10
    self.range = 10 # the hitbox 
    self.size = 10

class Block:
  def __init__(self, x, y, num):
    """
    Initialize the block object
    args: x, y indicate where the block is located on the screen and num is the number of blocks
    """
    self.num_of_boxes = num
    self.is_mystery = True # where the block is a mystery block or not
    self.can_breakopen = True # some blocks can be broken some can't 
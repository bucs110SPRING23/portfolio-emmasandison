# class == type 
# use 'class' for user-defined types 
# 'complex-type'

# class data: instance variables 

import turtle 

class Num: 
    def __init__(self, n): 
        self.data = n # instance variable for Num type objects 
        self.x = "string"

    # double under requirements: 
    #   - no parameters other than 'self'
    #   - must return a string 
    def __str__(self): 
        obj_str = f"The number is: {self.data}"
        return obj_str

    # object functions are called methods 
    # using self as the first parameter, makes it method 

    def addone(self): 
        self.data += 1
        # by using self.var I change the scope of the data to the object, not the method (function)
        self.var = "This is a value"

    def printval(self):
        print(self.var)

# function 
def addone(obj):
    obj.data += 1
    y = 2
    return



# class Foo: 

#     # def __init__(self, x, y, z, a, b, c):
#     #     self.x = x
#     #     self.y = y
#     # self..... # rest of parameters 
#     def __init__(self, **kwargs): 
#         self.__dict__ = kwargs

def main(): 

    mynum = Num(7)
    mynum2 = Num(9)
    mynum3 = {'data': 7, "x": "string"}

    print(mynum.data)
    print(mynum2.data)
    print(mynum3['data'])
    print(mynum.__dict__)

    mynum.addone()
    print(mynum.data)
    mynum2.addone()
    print(mynum2.data)

    # dictionary = {'x': 1, 'y': 2, 'z': 3}
    # foo = Foo(**dictionary)

    # t = turtle.Turtle()
    # t.forward()

    mystr = "Hello"

    length = len(mystr)
    mylist = [1, 2, 3]
    list_length = len([1, 2, 3])

    # call a method on an object 
    upper_str = mystr.upper()
    split_str = mystr.split("ll")
    mylist.upper() # Error 

    # mylist = [] # list() like str()
    # mylist.append()
    # index = 0
    # mylist.pop(index) 

    num = 5
    print(f"The number is: {num}") # 0101
    mynewnum = Num(5)
    print(f"The number is: {mynewnum}")

    print(num) # print is calling num.__str__()



main()

# Purpose of classes: 
#   - Grouping related functions and 
#       keeping them in one place (inside a class) provides a clean 
#       structure to the code which increases the readability of the program.
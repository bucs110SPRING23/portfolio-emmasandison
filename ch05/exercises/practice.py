# vending machine 
# black boxing 

print("Welcome to the vending machine")
code = input("Please enter a code: ")
money = int(input("Give me money: "))

# Scope - where the date/algorithm is accessible 
# Functions are always defined in global scope 

# def my_vending_machine(code, money): 
#     if code == "A":
#         if money >= 1: 
#             print("You got a coke")
#         else: 
#             print("You need more money")
#     elif code == "B": 
#         if money >= 1.5: 
#                 print("You got a water")
#         else: 
#              print("You need more money")
#     elif code == "C":
#          if money >= 2: 
#               print("You got a juice")
#          else: 
#               print("You need more money")
#     else: 
#          print("Invalid code")

# my_vending_machine()
# my_vending_machine()
# my_vending_machine()

# Single Responsibility Principle 
# A function should do one thing
# A function should never be responsible for input 

# can access variables in global scope 
def find_max(x, y, z): # x = a, y = b, z = c
    max = x 
    if y > max: 
        max = y
    if z > max: 
        max = z

    print(max)

for _ in range(3): 
    print("Please enter 3 numbers:")
    a = int(input(": "))
    b = int(input(": "))
    c = int(input(": "))
    find_max(a, b)

# collision 
# - two variables of the same name 
# - can't have variables of the same name in the same scope 

b = 5
b = "5"


def foo(var): 
    var += 1 
    print(var)

var = 5
foo(var)
print(var)




def my_func(x=0):
    return x + x # x is scoped to my_func so it can't be assessed out of the function

# nested functions execute from the inside out 
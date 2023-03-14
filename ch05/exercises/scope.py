# Write a function that multiplies two numbers together using a loop and accumulator (no multiplication) and return the resulting value

def multiply(x):
    """
    This function takes the number and multiplies it by 3
    """
    running_total = 0         
    for counter in range(3):
        running_total = running_total + x
    return running_total

num = 5
result = multiply(num) # Call function here
print("The result of", num, "mulitplied by 3 is", result)

# Write a function that takes a number and exponent as parameters and raises the number to the exponent and return the resulting value (no exponentiation)
def squared(x):
    """
    This function takes the number and squares it
    """
    running_total = 0         
    for counter in range(x):
        running_total = running_total + x
    return running_total   

num = 10
result = squared(num)
print("The result of", num, "squared is", result)


# Write another function, called square, that takes a single parameter and squares it by only calling your multiplication or exponent function and return the resulting value only one line of code
def square(): 
    """
    This function uses the previous function to square a number 
    """
    num = 10
    print("The result of", num, "squared is", squared(10))
square()

        


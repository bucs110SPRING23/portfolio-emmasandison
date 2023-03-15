# Write a function that multiplies two numbers together using a loop and accumulator (no multiplication) and return the resulting value

def multiply(x,y):
    """
    This function takes the x input and multiplies it by the y input
    """   
    accumulator = 0      
    for _ in range(y):
        accumulator = accumulator + x
    return accumulator 


# Write a function that takes a number and exponent as parameters and raises the number to the exponent and return the resulting value (no exponentiation)
def exponent(x,y):
    """
    This function takes the number and squares it
    """
    accumulator = 1      
    for _ in range(y):
        accumulator = accumulator * x
    return accumulator   

# Write another function, called square, that takes a single parameter and squares it by only calling your multiplication or exponent function and return the resulting value only one line of code
def square(x): 
    """
    This function uses the previous function to square a number 
    """
    return multiply(x,x)

def main(): 
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    result = multiply(x,y)
    print(result)
    result = exponent(x,y)
    print(result)
    result = square(x)
    print(result)

main()
        


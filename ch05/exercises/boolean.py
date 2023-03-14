def percentage_to_letter(percent):
    let = "A" 
    if 80 <= percent < 90: 
        let = "B"
    elif 70 <= percent < 80: 
        let = "C"
    elif 60 <= percent < 70: 
        let = "D"
    elif percent < 60: 
        let = "F"
    elif percent < 100: 
        let = "ABC"
    return let

def is_passing(letter): # boolean functions, is_ * convention  
    """
    This is a function that returns a letter grade based on a percentage 
    args: percent (int)
    return: letter (str)
    """
    return letter.lower() in "abc" 

def main(): #driver code 
    # No docstring 
    grades = [90, 80, 70, 60, 50]
    for grade in grades:
        letter = percentage_to_letter(grade)
        if is_passing(letter):
            print("You passed!")
        else: 
            print("Someone messed up your grades!")

# main()  #Only call in global space because it will call other functions 

# print(is_passing.__doc__)

# Programming Pattern
## for - programming pattern 
## accumulator pattern 
# result = 0
# for i in range(10):
#     result = result + i

# print (result)

# accumulator = start_value 
# for i in list: 
##  accumulator = accumulator + i (+ can be any operation)

def remove_vowels(string): 
    vowels = "aeiou"
    vowels += vowels.upper()
    result = " "
    for ch in string: 
        if ch not in vowels: 
            result += ch 
    return result 

def main(): 
    mystring = "Hello World"
    print(remove_vowels(mystring))
main()





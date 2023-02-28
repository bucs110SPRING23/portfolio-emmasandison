print("Enter numbers to sum['q' to quit]")

sum = 0
while sum != 'q': 
    value = input("number: ")
    if value.isdigit():
        value = int(value)
        sum += value 
    elif value == 'q':
        print("Your total is:", sum)
        sum = value 




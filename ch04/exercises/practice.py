# Iteration 
# iterable- you can loop over it 

mystr = "hello" # special iterable list of characters 
mynums = [1,2,3,4,5]

for ch in mystr: 
    print(ch)

for num in mynums: 
    print(num)

# anything iterable can be 'indexed' into 
print(mystr[0], mystr[1], mystr[2], mystr[3], mystr[4])

mynums[0] = 5
print(mynums)

# mystr[0] = "J" can't do this

# mutable = changeable 
# immutable = can't be changed once created 

# Iterable objects are not always mutable 

for i, v in enumerate(mynums): 
    # i- index in the list 
    # v- value at index location 
    print(i,v)

print(mynums)

# tuple - immutable list 
mynums = (5,8,1,12345679,5) # immutable 
# mynums[2] = 2.5 - can't do this 

x = 5
y = 6

# temp = x  - - - swaps out values, x becomes y and y becomes x 
# x = y
# y = temp
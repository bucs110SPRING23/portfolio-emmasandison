import json
# json is a string format, not a file format 
# need to use double quotes - no single quotes 

# files 
# - saved program state 

# Operating system: - manage files
# request file from OS
# - where 
# - name 
# - how to use it

# - working with files is one way 

def main(): 
    # file_pointer = open("assets/ideas.txt", "r") # opens file in read mode
    # # ideas = file_pointer.read()
    # # print(ideas)
    # ideas = file_pointer.readlines() # prints data in file in lines 
    # print(ideas) # print(ideas[2]) - prints the third line in the file 
    # ideas = file_pointer.readline() # prints the first line of date in file 
    # print(ideas)
    # ideas = file_pointer.readline() # prints the second line of data in file 
    # print(ideas)

    # file_pointer.close() # closes file 

    # file_pointer = open("assets/ideas.txt", "a") - append mode 
    file_pointer = open("assets/ideas.txt", "w") # writing mode, the file gets truncated 

    idea = input("Enter an idea: ")
    ideas = []
    ideas.append(idea)

    for i in ideas: 
        file_pointer.write(i + "\n")
        x = 5 / 0
    file_pointer.close() # always close files when writing 

    # idea = input("Enter an idea: ")
    # ideas = []
    # ideas.append(idea)
    # print(ideas)


main()
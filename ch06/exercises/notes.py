# files 
# - saved program state 

# Operating system: - manage files
# request file from OS
# - where 
# - name 
# - how to use it

# - working with files is one way 

def main(): 
    file_pointer = open("assets/ideas.txt")

    idea = input("Enter an idea: ")
    ideas = []
    ideas.append(idea)
    print(ideas)


main()
rows = int(input("How many rows?: "))

def star_pyramid(): 
    for i in range(1, rows + 1): 
        print(i * "*")
star_pyramid()

rows2 = int(input("How many rows?: "))

def rstar_pyramid(): 
    for i in range(rows2 + 1, 1): 
        print(i * "*")
rstar_pyramid()




    


import pygame 

# Part A
n = 101
count = 0
def threenp1(n): 
    while n > 1.0: 
        count += 1
        if n % 2 == 0: 
            n = int(n / 2)
        else: 
            n = int(3 * n + 1)
    return count 

def threenp1range(upper_limit):

    list = {}
    upper_limit = 20
    iters = []
    for _ in range(2, upper_limit + 1): 
        count = 0
        while n > 1.0: 
            count += 1
            if n % 2 == 0: 
                n = int(n / 2)
            else: 
                n = int(3 * n + 1)
        
            list[n] = count
            list.append(n)
    print(list)
   
# Part B 
def main(): 
    pygame.init()
    window = pygame.display.set_mode()
    window.fill("white")
    pygame.display.flip()

    def graph_coordinates(list): 
        coordinates = [(n, count)]
        new_display = pygame.transform.flip(window, False, True)
        width, height = new_display.get_size()
        new_display = pygame.transform.scale(new_display, (100 * 5, 100 * 5))
        window.blit(new_display, (0,0))
        for i in range(1, 21): 
            max_so_far = 0
            if count > max_so_far: 
                max_so_far = count 
            else: 
                max_so_far = 0

    font = pygame.font.Font(None, 16)
    msg = font.render("The max so far is: ", True, "green")
    window.blit(msg, (10,10))

            

import pygame 

# Part A
def main():
    upper_limit = 20
    def threenp1(n): 
        count = 0
        while n > 1.0: 
            count += 1
            if n % 2 == 0: 
                n = int(n / 2)
                print(n)
            else: 
                n = int(3 * n + 1)
                print(n)
        return count 
    
    # key=n, value=count (# of iterations)

    def threenp1range(upper_limit):
        dict = {}
        for i in range(2, upper_limit + 1): 
            dict[i] = threenp1(i)
        return dict
        
   
    # Part B 
 
    pygame.init()
    window = pygame.display.set_mode()
    window.fill("white")
    pygame.display.flip()

    def graph_coordinates(a): 
        coordinates = [(2, 1), (3, 7), (4, 2), (5, 5), (6, 8), (7, 16), (8, 3), (9, 19), (10, 6), (11, 14), (12, 9), (13, 9), (14, 17), (15, 17), (16, 4), (17, 12), (18, 20), (19, 20), (20, 7)]
        for point in coordinates: 
            pygame.draw.lines(window, "blue", False, coordinates)
        new_display = pygame.transform.flip(window, False, True)
        width, height = new_display.get_size()
        new_display = pygame.transform.scale(new_display, (100 * 5, 100 * 5))
        window.blit(new_display, (0,0))
        for i in range(1, 21): 
            max_so_far = 0
            if threenp1(i) > max_so_far: 
                max_so_far = threenp1(i) 
            else: 
                max_so_far = 0


    font = pygame.font.Font(None, 16)
    msg = font.render("The max so far is: ", True, "green")
    window.blit(msg, (10,10))

    a = threenp1range(upper_limit)
    print(a)
    # graph_coordinates()
    

    window.blit(window, [0,0])
    exit = False
    while not exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                exit = True
    pygame.display.update()

main()
    










            

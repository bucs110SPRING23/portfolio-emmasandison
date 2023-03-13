import pygame 

# Part A
def main():
    n = 101
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
    
    

    def threenp1range(upper_limit):

        # dict = []
        upper_limit = 20
        # iter = {}
        for _ in range(2, upper_limit + 1): 
            count = 0
            while n > 1.0: 
                count += 1
                if n % 2 == 0: 
                    n = int(n / 2)
                else: 
                    n = int(3 * n + 1)

                iter = {n:count}
            return dict
        
    # threenp1range()
   
    # Part B 
 
    count = 0
    pygame.init()
    window = pygame.display.set_mode()
    window.fill("white")
    pygame.display.flip()

    def graph_coordinates(threenp1range): 
        coordinates = [(1, iter[0]), (2, iter[1]), (3, iter[2]), (4, iter[3]), (5, iter[4]), (6, iter[5]), (7, iter[6]), (8, iter[7]), (9, iter[8]), (10, iter[9]), (11, iter[10]), (12, iter[11]), (13, iter[12]), (14, iter[13]), (15, iter[14]), (16, iter[15]), (17, iter[16]), (18, iter[17]), (19, iter[18]), (20, iter[19]), (21, iter[20])]
        for point in coordinates: 
            pygame.draw.lines(window, "blue", False, coordinates)
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



    # graph_coordinates()



    font = pygame.font.Font(None, 16)
    msg = font.render("The max so far is: ", True, "green")
    window.blit(msg, (10,10))

    threenp1()
    threenp1range()
    graph_coordinates()
    main()

    window.blit(window, [0,0])
    exit = False
    while not exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                exit = True
    pygame.display.update()


    











            

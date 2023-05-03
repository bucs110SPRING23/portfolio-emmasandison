import pygame

# Part A
def main():

    upper_limit = 100
    def threenp1(n):
        """
        This function performs the 3n+1 calculations and retuns the number of iterations.
        args: n (int)
        returns: count (int)
        """
        count = 0
        while n > 1.0:
            count += 1
            if n % 2 == 0:
                n = int(n / 2)
                # print(n)
            else:
                n = int(3 * n + 1)
                # print(n)
        return count

    # key=n, value=count (# of iterations)

    def threenp1range(upper_limit):
        """
        This function stores the number of iterations (count) and the number (n) calculated using the 3n+1 function (key) in a dictionary.
        args: upper limit (int)
        returns: dict (list)
        """
        dict = {}
        for i in range(2, upper_limit + 1):
            dict[i] = threenp1(i) # i is value in range and then this value is ran through threenp1 function
        return dict

    a = threenp1range(upper_limit)
    print(a)


    # Part B

    pygame.init()
    window = pygame.display.set_mode()
    window.fill("white")
    pygame.display.flip()

    def graph_coordinates(coordinates):
        """
        This function is supposed to graph the coordinates that are in the dictionary
        args: a (list)
        # """
        # coordinates = [(2, 1), (3, 7), (4, 2), (5, 5), (6, 8), (7, 16), (8, 3), (9, 19), (10, 6), (11, 14), (12, 9), (13, 9), (14, 17), (15, 17), (16, 4), (17, 12), (18, 20), (19, 20), (20, 7)]
        # for point in coordinates:
        #     pygame.draw.lines(window, "blue", False, coordinates)
        # new_display = pygame.transform.flip(window, False, True)
        # width, height = new_display.get_size()
        # new_display = pygame.transform.scale(new_display, (100 * 1, 100 * 1))
        # window.blit(new_display, (0,0))
        # for i in range(1, 21):
        #     max_so_far = 0
        #     if threenp1(i) > max_so_far:
        #         max_so_far = threenp1(i)
        #     else:
        #         max_so_far = 0
        coordinates = list(coordinates.items())
        print(coordinates)
        max_count = max(coordinates, key=lambda x: x[1])
        pygame.draw.lines(window, "blue", False, coordinates)
        width, height = window.get_size()
        new_display = pygame.transform.scale(window, (width * 5, height * 5))
        window.blit(new_display, (0,0))
        new_display = pygame.transform.flip(window, False, True)
        window.blit(new_display, (0,0))
        font = pygame.font.Font(None, 64)
        msg = font.render("Max Count: " + str(max_count[0]), False, "white", "black")
        window.blit(msg, (8, 8))
        pygame.display.flip()


    # font = pygame.font.Font(None, 16)
    # msg = font.render("The max so far is: ", True, "green")
    # window.blit(msg, (10,10))

    # window.blit(window, [0,0])

    graph_coordinates(a)
    exit = False
    while not exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
    pygame.display.update()

main()













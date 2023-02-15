import pygame
pygame.init()

while 1: 
    pygame.event.pump()
    screen = pygame.display.set_mode()
    dimensions = screen.get_size()
    starting_point = (dimensions[0] // 2, dimensions[1] // 2)
    radius = 50
    for _ in range(4):
        pygame.draw.circle(screen, "red", starting_point, radius)
        starting_point[1] = starting_point[1] - radius
        radius = radius // 2
        starting_point[1] = starting_point[1] - radius
    pygame.display.flip()  
    pygame.time.wait(2000)
    break























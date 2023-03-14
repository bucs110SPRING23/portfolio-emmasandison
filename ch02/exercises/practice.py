import pygame 

pygame.init()

# gets the display and makes it full screen 
# no arguments means full screen 

screen = pygame.display.set_mode()

screen.fill("red")
pygame.display.flip()

pygame.time.wait(500)

screen.fill("green")
pygame.display.flip()

pygame.time.wait(500)

screen.fill("blue")
pygame.display.flip()

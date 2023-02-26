import pygame  

pygame.init()
width = 1440
height = 900
screen = pygame.display.set_mode((width,height))
surface1 = pygame.Surface((width,height))
surface1.fill("blue")
pygame.draw.circle(surface1, "green", (720,450), 450)
screen.blit(surface1, (0,0))
exit = False
while not exit: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit = True
    pygame.display.update()

pygame.quit()


import pygame  
import math
import random

pygame.init()
width = 1440
height = 800
screen = pygame.display.set_mode((width,height))
surface1 = pygame.Surface((width,height))
surface1.fill("blue")

x = 720
y = 400
center = (x,y)
pygame.draw.circle(surface1, "orange", center, 400)
x2 = 720
y2 = 0
start_pos = (x2,y2)
x3 = 720
y3 = 800
end_pos = (x3,y3)
pygame.draw.line(surface1, "purple", start_pos, end_pos, 4)
x4 = 320
y4 = 400
start_pos2 = (x4,y4)
x5 = 1120
y5 = 400
end_pos2 = (x5,y5)
pygame.draw.line(surface1, "purple", start_pos2, end_pos2, 4)
pygame.display.flip()


for i in range(11): 
    x1 = random.randrange(0,width)
    y1 = random.randrange(0,height)
    coordinates = (x1, y1)
    distance_from_center = math.hypot(x-x1, y-y1)
    is_in_circle = distance_from_center <= width/2
    if is_in_circle == False:
        pygame.draw.circle(surface1,"red",coordinates,3)
        pygame.display.flip()
        pygame.time.wait(2500)
    if is_in_circle == True: 
        pygame.draw.circle(surface1,"green",coordinates,3)
        pygame.display.flip()
        pygame.time.wait(2500)


screen.blit(surface1, [0,0])
exit = False
while not exit: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit = True
    pygame.display.update()



        
            
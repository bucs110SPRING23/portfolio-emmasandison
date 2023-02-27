import pygame  
import math
import random

pygame.init()
width = 500
height = 500
screen = pygame.display.set_mode((width,height))
surface1 = pygame.Surface((width,height))
surface1.fill("blue")

x = 250
y = 250
center = (x,y)
pygame.draw.circle(surface1, "orange", center, 250)
x2 = 250
y2 = 0
start_pos = (x2,y2)
x3 = 250
y3 = 500
end_pos = (x3,y3)
pygame.draw.line(surface1, "purple", start_pos, end_pos, 4)
x4 = 0
y4 = 250
start_pos2 = (x4,y4)
x5 = 500
y5 = 250
end_pos2 = (x5,y5)
pygame.draw.line(surface1, "purple", start_pos2, end_pos2, 4)
pygame.display.flip()


for i in range(10): 
    x1 = random.randrange(0,width)
    y1 = random.randrange(0,height)
    coordinates = (x1, y1)
    distance_from_center = math.hypot(x1-x, y1-y)
    is_in_circle = distance_from_center <= width/2
    if is_in_circle == False:
        pygame.draw.circle(surface1,"red",coordinates,3)
        pygame.display.flip()
        pygame.time.wait(2000)
    if is_in_circle == True: 
        pygame.draw.circle(surface1,"green",coordinates,3)
        pygame.display.flip()
        pygame.time.wait(2000)
 
screen.blit(surface1, [0,0])
exit = False
while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            exit = True
    pygame.display.update()

            
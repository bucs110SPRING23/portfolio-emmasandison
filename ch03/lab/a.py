import pygame 
import random 
import math 
pygame.init()


# Part A
window_height = 500
window_width = 500
window = pygame.display.set_mode([window_height,window_width])

x = 250
y = 250 
center = (x,y)
window.fill([0,128,255])
pygame.draw.circle(window, "pink", center, 250)
x2 = 0 
y2 = 250
start_pos = (x2,y2)
x3 = 500
y3 = 250 
end_pos = (x3,y3)
pygame.draw.line(window, "black", start_pos, end_pos, width = 2)
x4 = 250 
y4 = 500
start_pos2 = (x4,y4)
x5 = 250 
y5 = 0 
end_pos2 = (x5,y5)
pygame.draw.line(window, "black", start_pos2, end_pos2, width = 2)
pygame.display.flip()

# Part B
for i in range(10):
    value = random.randrange(0, window_width)
    value2 = random.randrange(0, window_height)
    coordinates = (value, value2)
    distance_from_circle = math.hypot (value-x, value2-y)
    is_in_circle = distance_from_circle <= window_width/2
    if is_in_circle == False: 
        pygame.draw.circle(window,"red", coordinates,3)
        pygame.display.flip()
        pygame.time.wait(2500)
    if is_in_circle == True: 
        pygame.draw.circle(window,"green", coordinates,3)
        pygame.display.flip()
        pygame.time.wait(2500)
    print(coordinates)
    print(distance_from_circle)
    print(is_in_circle)



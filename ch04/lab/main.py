import pygame  
import math
import random
pygame.init()

 
width = 500
height = 500
screen = pygame.display.set_mode([width,height])
surface1 = pygame.Surface([width,height])
surface2 = pygame.Surface([width,height])

choice = ""
mouse_position = pygame.mouse.get_pos()
blue = pygame.draw.rect(surface2, "blue", (0, 0, 250, 500))
red = pygame.draw.rect(surface2, "red", (250, 0, 250, 500))
pygame.time.wait(2500)
screen.blit(surface2, [0,0])
pygame.display.flip()


Guess = True
while Guess == True: 
    for event in pygame.event.get(): 
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if event.pos[0] < width / 2: 
                playerchoice = "blue"
                Guess = False 
            elif event.pos[0] > width / 2: 
                playerchoice = "red"
                Guess = False
print("Your player is", playerchoice)
pygame.display.flip()
pygame.time.wait(1000)

print("Who will win, red or blue?")
pygame.display.flip()
pygame.time.wait(6000)

surface1.fill("white")
pygame.display.flip()
pygame.time.wait(2500)

x = 250
y = 250
center = (x,y)
surface1.fill("blue")
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

players = ["red","blue"]
red_score = 0
blue_score = 0

for i in range(10): 
    for player in players:
        x1 = random.randrange(0,width)
        y1 = random.randrange(0,height)
        coordinates = (x1, y1)
        distance_from_center = math.hypot(x1-x, y1-y)
        is_in_circle = distance_from_center <= width/2
        if is_in_circle == True:
            print(player, "hit the target")
            pygame.draw.circle(surface1, player, coordinates, 3)
            pygame.draw.circle(surface1, player, coordinates, 3)
        if player is players[0]:
            red_score = red_score + 1
        if player is players[1]:
            blue_score = blue_score + 1
        pygame.display.flip()
        pygame.time.wait(2500)
        if is_in_circle == False: 
            print(player, "did not hit the target")
            pygame.draw.circle(surface1,"yellow",coordinates,3)
            pygame.display.flip()
            pygame.time.wait(2500)
if i == 9: 
    if red_score > blue_score: 
        print(players[0], "has won the game!")
    if blue_score > red_score: 
        print(players[1], "has won the game!")
    if red_score == blue_score: 
        print("The game is tied.")
    pygame.display.flip()
    pygame.time.wait(1000)

pygame.display.flip()
pygame.time.wait(2500)



if Guess is playerchoice: 
    print("Your guess is correct!")
else:
    print("Your guess was incorrect.")
pygame.time.wait(1000)

 
screen.blit(surface1, [0,0])
exit = False
while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            exit = True
    pygame.display.update()
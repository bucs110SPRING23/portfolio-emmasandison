import random
import turtle 
import pygame
import math

# Part A

window = turtle.Screen()
window.bgcolor('lightblue')

# Race 1
value = random.randrange(1,101)
value_2 = random.randrange(1,101)
print(value)
print(value_2)

t = turtle.Turtle()
t.color('pink')
t.shape('turtle')
t.penup()
t.goto(-100,20)
t.pendown()

p = turtle.Turtle()
p.color('purple')
p.shape('turtle')
p.penup()
p.goto(-100,-20)
p.pendown()

t.forward(value)
p.forward(value_2)
t.penup()
t.goto(-100,20)
p.penup()
p.goto(-100,-20)
t.clear()
p.clear()


# Race 2
for _ in range(0,11): 
    t.forward(random.randrange(0,11))
    p.forward(random.randrange(0,11))
    t.penup()
    t.goto(-100,20)
    p.penup()
    p.goto(-100,-20)


# Part B

pygame.init()
screen = pygame.display.set_mode()

coord = []
num_sides = 3
side_length = 50
offset = 100

for i in range(num_sides): 
    theta = (2.0 * math.pi * (i)) / num_sides
    x = side_length * math.cos(theta) + offset
    y = side_length * math.sin(theta) + offset 
    points = (x,y)
    coord.append(points)

pygame.time.wait(2500)
pygame.draw.polygon(screen, "pink", coord)
pygame.display.flip()
screen.fill("black")

coord = []
num_sides = 4
side_length = 50
offset = 100

for i in range(num_sides): 
    theta = (2.0 * math.pi * (i)) / num_sides
    x = side_length * math.cos(theta) + offset
    y = side_length * math.sin(theta) + offset 
    points = (x,y)
    coord.append(points)

pygame.time.wait(2500)
pygame.draw.polygon(screen, "orange", coord)
pygame.display.flip()
screen.fill("black")

coord = []
num_sides = 6
side_length = 50
offset = 100

for i in range(num_sides): 
    theta = (2.0 * math.pi * (i)) / num_sides
    x = side_length * math.cos(theta) + offset
    y = side_length * math.sin(theta) + offset 
    points = (x,y)
    coord.append(points)

pygame.time.wait(2500)
pygame.draw.polygon(screen, "blue", coord)
pygame.display.flip()
screen.fill("black")

coord = []
num_sides = 20
side_length = 50
offset = 100

for i in range(num_sides): 
    theta = (2.0 * math.pi * (i)) / num_sides
    x = side_length * math.cos(theta) + offset
    y = side_length * math.sin(theta) + offset 
    points = (x,y)
    coord.append(points)

pygame.time.wait(2500)
pygame.draw.polygon(screen, "green", coord)
pygame.display.flip()
screen.fill("black")

coord = []
num_sides = 100
side_length = 50
offset = 100

for i in range(num_sides): 
    theta = (2.0 * math.pi * (i)) / num_sides
    x = side_length * math.cos(theta) + offset
    y = side_length * math.sin(theta) + offset 
    points = (x,y)
    coord.append(points)

pygame.time.wait(2500)
pygame.draw.polygon(screen, "purple", coord)
pygame.display.flip()
screen.fill("black")

coord = []
num_sides = 360
side_length = 50
offset = 100

for i in range(num_sides): 
    theta = (2.0 * math.pi * (i)) / num_sides
    x = side_length * math.cos(theta) + offset
    y = side_length * math.sin(theta) + offset 
    points = (x,y)
    coord.append(points)

pygame.time.wait(2500)
pygame.draw.polygon(screen, "red", coord)
pygame.display.flip()
screen.fill("black")


window.exitonclick()
import pygame

pygame.init()

screen = pygame.display.set_mode()

pygame.draw.circle(screen, "red", [200,  150], 50)
pygame.draw.circle(screen, "blue", [300, 250], 100)
pygame.draw.circle(screen, "green", [400, 350], 150)

import pygame
from sys import exit

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill("Red")




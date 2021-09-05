import pygame
from sys import exit

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pygame.time.Clock()

test_surface = pygame.Surface((100,200))
test_surface.fill("Red")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(test_surface,(0,0))

    pygame.display.update()
    clock.tick(60)




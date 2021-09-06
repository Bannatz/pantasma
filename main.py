import pygame
from sys import exit

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pygame.time.Clock()

sky_surface = pygame.image.load("Background/Sky.png").convert()
ground_surface = pygame.image.load("Ground/ground.png").convert()


player_surf = pygame.Surface((100,200))
player_surf.fill("Black")
player_rect = player_surf.get_rect(midbottom = (50,580))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.fill("#d1f4f7")
    screen.blit(sky_surface,(0,100))
    screen.blit(ground_surface,(0,580))
    screen.blit(player_surf,player_rect)

    pygame.display.update()
    clock.tick(60)




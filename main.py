import pygame
from sys import exit
from screen_settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,50))
        self.image.fill("Black")
        self.rect = self.image.get_rect(midbottom = (50,580))
        self.gravity = 0

    def control(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] or keys[pygame.K_w]:
            if self.rect.bottom == 580:
                self.gravity = -25
        
        elif keys[pygame.K_d]:
            self.rect.x += 5
        
        elif keys[pygame.K_a]:
            self.rect.x -= 5
        
        elif keys[pygame.K_s]:
            self.gravity = + 10
    
    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 580:
            self.rect.bottom = 580
    
    def update(self):
        self.control()
        self.apply_gravity()


class TestEnemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,50))
        self.image.fill("Red")
        self.rect = self.image.get_rect(midbottom = (100,580))
        self.gravity = 0
        self.turn_after = SCREEN_WIDTH
        self.pace_time = 0
        self.pace_size = 5
        self.pace_count = 0
        self.direction = -1
        self.speed = 10

    def run(self):
        time_now = pygame.time.get_ticks()
        if (time_now > self.pace_time + self.speed):
            self.pace_time = time_now

            # Walk Pace in the current Direction!
            self.pace_count += 1
            self.rect.x += self.direction * self.pace_size

            if(self.pace_count >= self.turn_after):
                self.direction *= -1
                self.pace_count = 0
            if (self.rect.x <= 0):
                self.direction = 1
                self.pace_count = 0
            elif (self.rect.x >= SCREEN_WIDTH - self.rect.width):
                self.direction = -1
                self.pace_count = 0


    def update(self):
        self.run()

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Movement Testing")
clock = pygame.time.Clock()

sky_surface = pygame.image.load("data/Background/Sky.png").convert()
ground_surface = pygame.image.load("data/Ground/ground.png").convert()

health_surf = pygame.Surface((300,50))
health_surf.fill("Red")

move = 100

#player_surf = pygame.Surface((move,200))
#player_surf.fill("Black")
#player_rect = player_surf.get_rect(midbottom = (50,580))
player = Player()
sprites = pygame.sprite.GroupSingle()
sprites.add(player)

enemy = pygame.sprite.GroupSingle()
enemy.add(TestEnemy())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.fill("#d1f4f7")
    screen.blit(sky_surface,(0,100))
    screen.blit(ground_surface,(0,580))
    #screen.blit(player_surf,player_rect)
    screen.blit(health_surf,(0,0))    
    # Player
    sprites.draw(screen)
    sprites.update()
    # The Test Enemy with an Basic Logic
    enemy.draw(screen)
    enemy.update()


    pygame.display.update()
    clock.tick(60)
    



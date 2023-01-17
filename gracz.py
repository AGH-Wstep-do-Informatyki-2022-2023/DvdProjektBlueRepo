from global_settings import Window, Colors
import pygame

WIDTH = Window.WIDTH
HEIGHT = Window.HEIGHT
GREEN = Colors.GREEN

# Klasa gracza
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speed_x = 0

    def update(self):
        self.speed_x = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speed_x = -2
        if keystate[pygame.K_RIGHT]:
            self.speed_x = 2
        self.rect.x += self.speed_x
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

# dopisuje.exe

#konflikt pawła

# cokoliwek dposiane 2

# test konfliktu
##3


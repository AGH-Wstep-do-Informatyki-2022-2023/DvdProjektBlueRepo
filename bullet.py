import pygame
from global_settings import Window, Colors

WHITE = Colors.WHITE

#from global_settings.Window import *
#from global_settings.Colors import *


class Bullet(pygame.sprite.Sprite):    
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/windows.png")
        self.image = pygame.transform.scale(self.image, (45, 45))
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10
 
    def update(self):
        self.rect.y += self.speedy
        # Jeśli pocisk wyjdzie poza ekran, usuwamy go z grupy
        if self.rect.bottom < 0:
            self.kill()


####################
#Komentarz, który ma wywołać konflikt

#######################
#test


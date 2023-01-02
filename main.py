import pygame
import random
 
# Inicjalizacja Pygame
pygame.init()
 
# Ustawienia gry
WIDTH = 800
HEIGHT = 600
FPS = 60

# Stworzenie okna gry
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Penguin Invaders")

# Zegar
clock = pygame.time.Clock()
 
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
            self.speed_x = -8
        if keystate[pygame.K_RIGHT]:
            self.speed_x = 8
        self.rect.x += self.speed_x
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
 
pygame.quit()

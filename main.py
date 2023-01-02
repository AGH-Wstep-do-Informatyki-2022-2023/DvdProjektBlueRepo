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
 
pygame.quit()
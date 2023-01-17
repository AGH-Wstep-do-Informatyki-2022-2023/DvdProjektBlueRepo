import pygame
import random
from bullet import Bullet
from menu import GameMenu
from gracz import Player
from enemy import Enemy
from global_settings import Window, Colors
 
# Inicjalizacja Pygame
pygame.init()
 
# Ustawienia gry
WIDTH = Window.WIDTH
HEIGHT = Window.HEIGHT
FPS = Window.FPS

WHITE = Colors.WHITE
BLACK = Colors.BLACK
RED = Colors.RED
GREEN = Colors.GREEN
BLUE = Colors.BLUE

clock = pygame.time.Clock()
clock.tick(FPS)

# Stworzenie okna gry
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Penguin Invaders")

# Grupy
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

# Tworzenie gracza
player = Player()
all_sprites.add(player)

# Tworzenie wrogów
for i in range(8):
    enemy = Enemy()
    enemies.add(enemy)
    all_sprites.add(enemy)

while True:
    # Pętla główna gry
    menu = GameMenu(screen)
    menu.run()
    running = True
    while running:
        # Sprawdzanie wydarzeń
        for event in pygame.event.get():       
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = Bullet(player.rect.centerx, player.rect.top)
                    all_sprites.add(bullet)
                    bullets.add(bullet)

        # Aktualizacja
        all_sprites.update()

        # Sprawdzenie, czy pocisk trafił wroga
        hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
        for hit in hits:
            enemy = Enemy()
            all_sprites.add(enemy)
            enemies.add(enemy)

        # Sprawdzenie, czy gracz trafił wroga
        hits = pygame.sprite.spritecollide(player, enemies, False)
        if hits:
            running = False

        # Rysowanie ekranu
        screen.fill(BLACK)
        all_sprites.draw(screen)
        pygame.display.flip()
        
pygame.quit()

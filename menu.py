import pygame

class GameMenu:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.waiting = True

    def run(self):
        self.screen.fill(BLACK)
        self.draw_text("Penguin Invaders", 64, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Naciśnij dowolny klawisz, aby rozpocząć grę", 22, WIDTH / 2, HEIGHT / 2)
        pygame.display.flip()
        while self.waiting:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYUP:
                    self.waiting = False

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(pygame.font.match_font('arial'), size)
        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)
import pygame


class Bullet:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/img_bullets.jpg').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 20))
        self.rect = self.image.get_rect()


    def draw(self, x, y):
        self.rect.center = x, y
        self.screen.screen.blit(self.image, self.rect)
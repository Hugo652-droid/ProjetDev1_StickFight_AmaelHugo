import pygame


class Bullet:
    def __init__(self, x, y):
        self.image = pygame.image.load('images/img_bullets.jpg').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 20))
        self.rect = self.image.get_rect()
        self.rect.center = x, y


    def draw(self, screen):
        screen.screen.blit(self.image, self.rect)
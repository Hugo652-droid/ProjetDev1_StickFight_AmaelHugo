import pygame


class Bullet():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/img_bullets.jpg').convert_alpha()
        self.rect = self.image.get_rect()


    def draw(self):
        self.rect.center = 500, 500
        self.screen.screen.blit(self.image, self.rect)
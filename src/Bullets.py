import pygame


class Bullet:
    def __init__(self, x, y, direction):
        self.image = pygame.image.load('images/img_bullets.jpg').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 20))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.direction = direction

    def draw(self, screen):
        self.rect.center = self.x, self.y
        screen.screen.blit(self.image, self.rect)

    def shot(self):
        if self.direction == 'Left':
            self.x -= 10
        elif self.direction == 'Right':
            self.x += 10
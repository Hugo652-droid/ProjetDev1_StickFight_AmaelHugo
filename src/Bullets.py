import pygame


class Bullet:
    def __init__(self, position, direction, playerAttackName):

        self.x = position[0]
        self.y = position[1]
        self.playerAttackName = playerAttackName
        self.direction = direction
        if self.direction == 'Left':
            self.image = pygame.image.load('images/img_bullets_left.jpg').convert_alpha()
            self.image = pygame.transform.scale(self.image, (50, 20))
            self.rect = self.image.get_rect()
        elif self.direction == 'Right':
            self.image = pygame.image.load('images/img_bullets_right.jpg').convert_alpha()
            self.image = pygame.transform.scale(self.image, (50, 20))
            self.rect = self.image.get_rect()


    def draw(self, screen):
        self.rect.center = self.x, self.y
        screen.screen.blit(self.image, self.rect)

    def shot(self):
        if self.direction == 'Left':
            self.x -= 10
        elif self.direction == 'Right':
            self.x += 10
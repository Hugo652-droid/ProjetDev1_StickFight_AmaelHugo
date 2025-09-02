import pygame

class Map:
    def __init__(self, window, x, y, w, h):
        self.window = window
        self.img_floor = pygame.image.load('./images/floor_test.png')
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rect = self.img_floor.get_rect()
        self.info_screen = pygame.display.Info()

    def draw(self, screen):
        self.img_floor = pygame.transform.scale(self.img_floor, (self.w, self.h))
        self.rect = self.img_floor.get_rect()
        self.rect.center = (self.x, self.y)
        screen.blit(self.img_floor, self.rect)


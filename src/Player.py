import pygame


class Player:
    def __init__(self, name, hp, weapon_id, x, y, image):
        self.name = name
        self.hp = hp
        self.weapon_id = weapon_id
        self.x = x
        self.y = y
        self.img = pygame.image.load(image).convert_alpha()

    def draw(self, screen):
        rect = self.img.get_rect()
        rect.center = (self.x, self.y)
        screen.blit(self.img, rect)

    def modifImage(self, image):
        self.img = pygame.image.load(image).convert_alpha()
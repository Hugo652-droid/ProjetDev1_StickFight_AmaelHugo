import pygame


class Player:
    def __init__(self, name, hp, weapon_id, x, y, image):
        self.name = name
        self.hp = hp
        self.weapon_id = weapon_id
        self.x = x
        self.y = y
        self.img = pygame.image.load(image).convert_alpha()
        self.rect = self.img.get_rect()

    def draw(self, screen):
        self.rect = self.img.get_rect()
        self.rect.center = (self.x, self.y)

        pygame.draw.rect(screen, (255,255,255), self.rect)

        screen.blit(self.img, self.rect)

    def modifImage(self, image):
        self.img = pygame.image.load(image).convert_alpha()
import pygame


class Player:
    def __init__(self, name, hp, weapon_id, x, y):
        self.name = name
        self.hp = hp
        self.weapon_id = weapon_id
        self.x = x
        self.y = y

    def draw(self, screen, image):
        image_a_afficher = pygame.image.load(image)
        image_convertie = image_a_afficher.convert()
        screen.blit(image_convertie, (self.x, self.y))

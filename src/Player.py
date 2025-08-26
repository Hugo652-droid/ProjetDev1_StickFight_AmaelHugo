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
        self.last_time_used_jump = 0
        self.cooldown = 1

        self.direct_player = None

    def draw(self, screen):
        self.rect = self.img.get_rect()
        self.rect.center = (self.x, self.y)
        screen.blit(self.img, self.rect)

    def modifImage(self, image):
        self.img = pygame.image.load(image).convert_alpha()

    def goUp(self, current_time):
        if current_time - self.last_time_used_jump > self.cooldown:
            self.y -= 300
            self.last_time_used_jump = current_time

    def goLeft(self):
        self.x -= 10
        self.direct_player = "Left"

    def goRight(self):
        self.x += 10
        self.direct_player = "Right"
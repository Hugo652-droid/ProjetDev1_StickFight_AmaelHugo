import pygame
from src.Bullets import Bullet

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
        self.last_time_used_attack = 0
        self.cooldown_jump = 1
        self.cooldown_attack = 1
        self.direct_player = None
        self.attacking = False
        self.weapon = 0

    def draw(self, screen, font):
        self.rect = self.img.get_rect()
        self.rect.center = (self.x, self.y)
        self.rect = pygame.Rect(self.x, self.y, self.rect.width, self.rect.height)
        screen.blit(self.img, self.rect)
        screen.blit(font.render(f'HP : {self.hp}', True, (0, 0, 0)), (self.x-25, self.y-150))

    def modifImage(self, image):
        self.img = pygame.image.load(image).convert_alpha()

    def goUp(self, current_time):
        if current_time - self.last_time_used_jump > self.cooldown_jump:
            self.y -= 300
            self.last_time_used_jump = current_time

    def goLeft(self):
        self.x -= 10
        self.direct_player = "Left"

    def goRight(self):
        self.x += 10
        self.direct_player = "Right"

    def dashLeft(self):
        self.x -= 150
        self.direct_player = "Left"

    def dashRight(self):
        self.x += 150
        self.direct_player = "Right"

    def tackDammage(self, damage):
        self.hp -= damage

    def playerIsDead(self):
        return self.hp <= 0

    def simple_attack(self, player_damaged):
        if self.weapon == 0:
            if self.rect.colliderect(player_damaged.rect):
                player_damaged.tackDammage(10)
                return False
        else :
            bullet = Bullet(self.x, self.y, self.direct_player)
            return bullet




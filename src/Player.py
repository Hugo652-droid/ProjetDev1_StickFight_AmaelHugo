import pygame

from src.Bullet import Bullet

class Player:
    def __init__(self, name, hp, x, y, image):
        self.name = name
        self.hp = hp
        self.x = x
        self.y = y
        self.info_screen = pygame.display.Info()
        self.img = pygame.image.load(image).convert_alpha()
        self.img = pygame.transform.scale(self.img, (200, 100))
        self.rect = self.img.get_rect()
        self.last_time_used_vertical = 0
        self.last_time_used_attack = 0
        self.cooldown_jump = 1
        self.cooldown_attack = 1
        self.cooldown_crouch = 1
        self.direct_player = "Left"
        self.attacking = False
        self.weapon = 0
        self.damage = 10

    def draw(self, screen, font):
        self.img = pygame.transform.scale(self.img, (150, 100))
        self.rect = self.img.get_rect()
        self.rect.center = (self.x, self.y)
        self.rect = pygame.Rect(self.x, self.y, self.rect.width, self.rect.height)
        screen.blit(self.img, self.rect)
        if self.weapon == 0:
            screen.blit(font.render(f'HP : {self.hp}', True, (0, 0, 0)), (self.x-25, self.y-150))
        else:
            screen.blit(font.render(f'HP : {self.hp} Ammo : {self.weapon.ammunition}', True, (0, 0, 0)), (self.x - 25, self.y - 150))

    def modifImage(self, image):
        self.img = pygame.image.load(image).convert_alpha()

    def goUp(self, current_time):
        if current_time - self.last_time_used_vertical > self.cooldown_jump:
            self.y -= self.info_screen.current_h/4
            self.last_time_used_vertical = current_time

    def goLeft(self):
        self.x -= 10
        self.direct_player = "Left"

    def goRight(self):
        self.x += 10
        self.direct_player = "Right"

    def goDown(self, current_time):
        if current_time - self.last_time_used_vertical > self.cooldown_crouch:
            self.y += 150
            self.last_time_used_vertical = current_time

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

    def simpleAttack(self, player_damaged):
        if self.weapon == 0:
            self.cooldown_attack = 1
            if self.rect.colliderect(player_damaged.rect):
                player_damaged.tackDammage(self.damage)
                return False
        else :
            if not self.weapon.noAmmunition():
                self.damage = self.weapon.dammage
                self.cooldown_attack = self.weapon.attackSpeed
                self.weapon.useAmmunition()
                bullet = Bullet(self.rect.center, self.direct_player, self.name, self.weapon.width, self.weapon.height)
                return bullet

    def noAmmunitionInWeapon(self):
        if self.weapon.noAmmunition():
            self.weapon = 0
            self.cooldown_attack = 1



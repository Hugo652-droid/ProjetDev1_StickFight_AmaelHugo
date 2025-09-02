import pygame
import random
import time

class Weapons():
    def __init__(self,id, img,dammage, attackSpeed, ammunition, width, height, floors, screen):
        self.id = id
        self.attackSpeed = attackSpeed
        self.ammunition = ammunition
        self.width = width
        self.height = height
        self.cooldown = 1
        self.img_weapom = pygame.image.load(img)
        self.rect_weapon = self.img_weapom.get_rect()
        self.img_weapom = pygame.transform.scale(self.img_weapom, (80, 30))
        self.rect_weapon = self.img_weapom.get_rect()
        self.info = pygame.display.Info()
        self.dammage = dammage
        self.screen = screen
        self.rect_weapon.x = random.randint(0, self.info.current_w - self.rect_weapon.width)
        self.rect_weapon.y = random.randint(0, self.info.current_h - self.rect_weapon.height)

    def draw(self):
        self.screen.blit(self.img_weapom, self.rect_weapon)

    def useAmmunition(self):
        self.ammunition -= 1

    def noAmmunition(self):
        return self.ammunition <= 0








import pygame
import random
import time

class Weapons():
    def __init__(self,img):
        self.cooldown = 1
        self.cooldown_dropweapon = 30
        self.lastused = 0
        self.lastdrop = time.time()
        self.img_weapom = pygame.image.load(img)
        self.rect_weapon = self.img_weapom.get_rect()
        self.img_weapom = pygame.transform.scale(self.img_weapom, (100, 70))
        self.rect_weapon = self.img_weapom.get_rect()
        info = pygame.display.Info()
        self.rect_weapon.x = random.randint(0, info.current_w - self.rect_weapon.width)
        self.rect_weapon.y = 0

    def draw(self, screen):
            screen.blit(self.img_weapom, self.rect_weapon)








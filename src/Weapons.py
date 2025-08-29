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
        self.visible = False


    def spawnWeapon(self, screen, current_time):

        if not self.visible and (current_time - self.lastdrop > self.cooldown_dropweapon):
            self.lastdrop = current_time

            info = pygame.display.Info()
            self.rect_weapon.x = random.randint(0, info.current_w - self.rect_weapon.width)
            self.rect_weapon.y = 0


            self.img_weapom = pygame.transform.scale(self.img_weapom, (120, 60))

            self.visible = True


        if self.visible:
            screen.blit(self.img_weapom, self.rect_weapon)







"""
--
Auteur : Amael Rochat et Hugo Rod
Date de départ : 18.08.2025
Date de fin : --.--.----
Projet : Projet Dev 1 (sticKOnion)
--
Nom fichier : Weapons.py
Description fichier : Creation et gestion des armes
--
"""

import pygame
import random

class Weapons():
    def __init__(self, weaponData, screen):
        self.id = weaponData["id"]
        self.attackSpeed = weaponData["attackSpeed"]
        self.ammunition = weaponData["ammunition"]
        self.width = weaponData["width"]
        self.height = weaponData["height"]
        self.cooldown = 1
        self.img_weapom = pygame.image.load(weaponData["img"])
        self.rect_weapon = self.img_weapom.get_rect()
        self.img_weapom = pygame.transform.scale(self.img_weapom, (80, 30))
        self.rect_weapon = self.img_weapom.get_rect()
        self.info = pygame.display.Info()
        self.dammage = weaponData["damage"]
        self.screen = screen
        self.placed = False

    def draw(self, floors, player1, player2):
        while not self.placed:
            self.rect_weapon.x = random.randint(0, self.info.current_w - self.rect_weapon.width)
            self.rect_weapon.y = random.randint(0, self.info.current_h - self.rect_weapon.height)

            # vérifie si au moins une condition dans une liste est vraie
            collision = any(self.rect_weapon.colliderect(floor.rect) for floor in floors)

            if not collision and not self.rect_weapon.colliderect(player1.rect) and not self.rect_weapon.colliderect(player2.rect) :
                self.placed = True
                self.screen.blit(self.img_weapom, self.rect_weapon)

        if self.placed:
            self.screen.blit(self.img_weapom, self.rect_weapon)

    def useAmmunition(self):
        self.ammunition -= 1

    def noAmmunition(self):
        return self.ammunition <= 0








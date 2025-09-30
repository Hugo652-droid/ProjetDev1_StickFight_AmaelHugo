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
        """
        Function for placing and drawing the weapons in the window
        :param floors: All the floors in the game
        :param player1: The player 1
        :param player2: The player 2
        :return: The weapon placed and drew in the window
        """
        while not self.placed:
            self.rect_weapon.x = random.randint(0, self.info.current_w - self.rect_weapon.width)
            self.rect_weapon.y = random.randint(0, self.info.current_h - self.rect_weapon.height)

            # check if the weapon appears in a floor
            collision = any(self.rect_weapon.colliderect(floor.rect) for floor in floors)

            if not collision and not self.rect_weapon.colliderect(player1.rect) and not self.rect_weapon.colliderect(player2.rect) :
                self.placed = True
                self.screen.blit(self.img_weapom, self.rect_weapon)

        if self.placed:
            self.screen.blit(self.img_weapom, self.rect_weapon)

    def useAmmunition(self):
        """
        Function that remove an ammunition in the weapon
        :return: The total of ammunition - 1
        """
        self.ammunition -= 1

    def noAmmunition(self):
        """
        Function that check if the weapon doesn't have an ammunition
        :return:
        """
        return self.ammunition <= 0








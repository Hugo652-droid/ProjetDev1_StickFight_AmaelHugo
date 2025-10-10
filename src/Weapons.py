"""
--
Auteur : Amael Rochat et Hugo Rod
Date de départ : 18.08.2025
Date de fin : 10.10.2025
Projet : Projet Dev 1 (sticKOnion)
--
Nom fichier : Weapons.py
Description fichier : Creation et gestion des armes
--
"""

import pygame
import random

INFO_SCREEN = pygame.display.Info()


class Weapon:
    def __init__(self, weapon_data, screen):
        """
        The weapon of the game
        :param weapon_data: The data of weapon [id, attackSpeed, ammunition, width, height, img, damage]
        :param screen: The window of the game
        """
        self.id = weapon_data["id"]
        self.attackSpeed = weapon_data["attackSpeed"]
        self.ammunition = weapon_data["ammunition"]
        self.width = weapon_data["width"]
        self.height = weapon_data["height"]
        self.cooldown = 1
        self.img_weapon = pygame.image.load(weapon_data["img"])
        self.rect_weapon = self.img_weapon.get_rect()
        self.img_weapon = pygame.transform.scale(self.img_weapon, (80, 30))
        self.rect_weapon = self.img_weapon.get_rect()
        self.damage = weapon_data["damage"]
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
            self.rect_weapon.x = random.randint(0, INFO_SCREEN.current_w - self.rect_weapon.width)
            self.rect_weapon.y = random.randint(0, INFO_SCREEN.current_h - self.rect_weapon.height)

            # check if the weapon appears in a floor
            collision = any(self.rect_weapon.colliderect(floor.rect) for floor in floors)

            if not collision and not self.rect_weapon.colliderect(player1.rect) and not self.rect_weapon.colliderect(
                    player2.rect):
                self.placed = True
                self.screen.blit(self.img_weapon, self.rect_weapon)

        if self.placed:
            self.screen.blit(self.img_weapon, self.rect_weapon)

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

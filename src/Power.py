"""
--
Auteur : Amael Rochat et Hugo Rod
Date de départ : 18.08.2025
Date de fin : 10.10.2025
Projet : Projet Dev 1 (sticKOnion)
--
Nom fichier : powers.py
Description fichier : Creation et gestion des armes
--
"""

import pygame
import random

INFO_SCREEN = pygame.display.Info()


class Power:
    def __init__(self, power_data, screen):
        """
        The power-up of the game
        :param power: The data of power [id, width, height, duration, health]
        :param screen: The window of the game
        """
        self.id = power_data["id"]
        self.width = power_data["width"]
        self.height = power_data["height"]
        self.duration = power_data["duration"]
        self.health = power_data["health"]
        self.img_power = pygame.image.load(power_data["img"])
        self.img_power = pygame.transform.scale(self.img_power, (50, 50))
        self.rect_power = self.img_power.get_rect()
        self.screen = screen
        self.placed = False

    def draw(self, floors, player1, player2):
        """
        Display the power
        :param floors: The platform of the stage
        :param player1: The player 1
        :param player2: The player 2
        :return: The power displayed
        """
        while not self.placed:
            self.rect_power.centerx = random.randint(0, INFO_SCREEN.current_w - self.rect_power.width)
            self.rect_power.centery = random.randint(0, INFO_SCREEN.current_h - self.rect_power.height)

            # vérifie si au moins une condition dans une liste est vraie
            collision = any(self.rect_power.colliderect(floor.rect) for floor in floors)

            if not collision and not self.rect_power.colliderect(player1.rect) and not self.rect_power.colliderect(
                    player2.rect):
                self.placed = True
                self.screen.blit(self.img_power, self.rect_power)

        if self.placed:
            self.screen.blit(self.img_power, self.rect_power)

    def takeDamage(self, damage):
        """
        Function for tacking damage
        :param damage: The damage to take
        :return: The health reduce by the damage
        """
        self.health -= damage

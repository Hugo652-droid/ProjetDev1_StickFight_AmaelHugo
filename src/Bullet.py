"""
--
Auteur : Amael Rochat et Hugo Rod
Date de départ : 18.08.2025
Date de fin : --.--.----
Projet : Projet Dev 1 (sticKOnion)
--
Nom fichier : Bullet.py
Description fichier : Creation et gestion des balles
--
"""

import pygame

class Bullet:
    def __init__(self, position, direction, player_attack_name, width, height):
        """
        The bullet of the game
        :param position: The position of the bullet
        :param direction: The direction of the bullet
        :param player_attack_name: The player who shoot the bullet
        :param width: The width of the bullet
        :param height: The height of the bullet
        """
        self.x = position[0]
        self.y = position[1]
        self.player_attack_name = player_attack_name
        self.direction = direction
        if self.direction == 'Left':
            self.image = pygame.image.load('images/imgGames/imgBullets/img_bullets_left.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (width, height))
            self.rect = self.image.get_rect()
        elif self.direction == 'Right':
            self.image = pygame.image.load('images/imgGames/imgBullets/img_bullets_right.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (width, height))
            self.rect = self.image.get_rect()


    def draw(self, screen):
        """
        Display the bullet on the screen
        :param screen: The window of the game
        :return: The bullet displayed
        """
        self.rect.center = self.x, self.y
        screen.screen.blit(self.image, self.rect)

    def shot(self):
        """
        Function for manage the bullet moving
        :return: The movement of the bullet
        """
        if self.direction == 'Left':
            self.x -= 20
        elif self.direction == 'Right':
            self.x += 20
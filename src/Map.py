"""
--
Auteur : Amael Rochat et Hugo Rod
Date de départ : 18.08.2025
Date de fin : --.--.----
Projet : Projet Dev 1 (sticKOnion)
--
Nom fichier : Player.py
Description fichier : Creation et gestion des platforms physique
--
"""

import pygame

class Map:
    def __init__(self, window, floor_data):
        """
        The platform of the game
        :param window: The window of the game
        :param floor_data: The data of platform [name, position x, position y, width, height, image (optional)]
        """
        self.screen = window.screen
        if floor_data['image'] != "":
            self.img_floor = pygame.image.load(floor_data['image'])
        else :
            self.img_floor = pygame.image.load('images/imgGames/imgFloors/floor1_dirt.png')
        self.x = floor_data['x']
        self.y = floor_data['y']
        self.w = floor_data['with']
        self.h = floor_data['height']
        self.rect = self.img_floor.get_rect()

    def draw(self):
        """
        display the platform
        :return: La platform displayed
        """
        self.img_floor = pygame.transform.scale(self.img_floor, (self.w, self.h))
        self.rect = self.img_floor.get_rect()
        self.rect.center = (self.x, self.y)
        self.screen.blit(self.img_floor, self.rect)



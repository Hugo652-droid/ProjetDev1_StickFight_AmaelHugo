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
    def __init__(self, window, x, y, w, h, image='images/imgGames/imgFloors/floor1_dirt.png'):
        self.window = window
        self.img_floor = pygame.image.load(image)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rect = self.img_floor.get_rect()
        self.info_screen = pygame.display.Info()

    def draw(self, screen):
        self.img_floor = pygame.transform.scale(self.img_floor, (self.w, self.h))
        self.rect = self.img_floor.get_rect()
        self.rect.center = (self.x, self.y)
        screen.blit(self.img_floor, self.rect)



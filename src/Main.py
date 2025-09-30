"""
--
Auteur : Amael Rochat et Hugo Rod
Date de départ : 18.08.2025
Date de fin : --.--.----
Projet : Projet Dev 1 (sticKOnion)
--
Nom fichier : Main.py
Description fichier : Lancement de l'application
--
"""

import pygame
from sys import exit
from Home import Home
from Root import Root

class Main:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.init()
        pygame.mixer.Channel(0).set_volume(1.0)
        pygame.mixer.Channel(1).set_volume(1.0)
        window = Root(pygame.font.Font("assets/Shooting Star.ttf", 100))
        home = Home(window)
        home.launch()
        pygame.quit()
        exit()

main = Main()
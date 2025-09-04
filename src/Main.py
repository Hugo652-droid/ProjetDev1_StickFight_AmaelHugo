"""
--
Auteur : Amael Rochat et Hugo Rod
Date de départ : 18.08.2025
Date de fin : --.--.----
Projet : Projet Dev 1 (sticKOnion)
--
Nom fichier : Main.py
Description fichier : Lancement de l'application et affichage de la page d'accueil
--
"""

import pygame
from sys import exit
from src.Home import Home

class Main():
    def __init__(self):
        pygame.init()
        home = Home()
        pygame.quit()
        exit()

main = Main()
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
from src.Root import Root
from src.Game import Game

class Main():
    def __init__(self):
        pygame.init()
        windowHome = Root(pygame)
        windowHome.changeBg('images/img_bg_main.png')
        windowHome.buttonPlay()
        windowHome.buttonQuit()
        windowHome.title('images/Image titre.png')
        self.font = pygame.font.SysFont('Arial', 25)
        windowHome.version(self.font)
        pygame.display.flip()
        runningHome = True
        while runningHome:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:

                        windowHome.closeRoot(pygame)
                        runningHome = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if windowHome.button_rect.collidepoint(event.pos):
                        windowHome.closeRoot(pygame)
                        runningHome = False
                        game = Game()

                    if windowHome.button_rect_quit.collidepoint(event.pos):
                        windowHome.closeRoot(pygame)
                        runningHome = False
        pygame.quit()
        exit()

main = Main()
"""
--
Auteur : Amael Rochat et Hugo Rod
Date de départ : 18.08.2025
Date de fin : --.--.----
Projet : Projet Dev 1 (sticKOnion)
--
Nom fichier : Main.py
Description fichier : Affichage de la page d'accueil
--
"""

import pygame
from src.Root import Root
from src.Game import Game

class Home :
    def __init__(self):
        self.windowHome = Root(pygame)
        self.windowHome.changeBg('images/imgBackgrounds/mainPageBg/mainBg/img_bg_main.png')
        self.windowHome.buttonPlay()
        self.windowHome.buttonQuit()
        self.windowHome.title('images/imgTexts/textsMain/textsMain/text_title.png')
        self.font = pygame.font.SysFont('Arial', 25)
        self.windowHome.version(self.font)
        
    def launch(self):
        pygame.display.flip()
        runningHome = True
        while runningHome:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.windowHome.closeRoot(pygame)
                        runningHome = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.windowHome.button_rect.collidepoint(event.pos):
                        self.windowHome.closeRoot(pygame)
                        runningHome = False
                        game = Game()
                        game.launchGame()

                    if self.windowHome.button_rect_quit.collidepoint(event.pos):
                        self.windowHome.closeRoot(pygame)
                        runningHome = False
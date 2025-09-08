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

class Home:
    def __init__(self):
        self.window_home = Root()
        self.window_home.changeBg('images/imgBackgrounds/mainPageBg/mainBg/img_bg_main.png')
        self.window_home.buttonPlay()
        self.window_home.buttonQuit()
        self.window_home.title('images/text_title.png')
        self.font = pygame.font.SysFont('Arial', 25)
        self.window_home.version(self.font)
        
    def launch(self):
        pygame.display.flip()
        running_home = True
        while running_home:
            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        self.window_home.closeRoot()
                        running_home = False
                    elif event.key != pygame.K_ESCAPE :
                        self.window_home.closeRoot()
                        running_home = False
                        game = Game()
                        game.launchGame()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.window_home.button_rect_play.collidepoint(event.pos):
                        self.window_home.closeRoot()
                        running_home = False
                        game = Game()
                        game.launchGame()

                    if self.window_home.button_rect_quit.collidepoint(event.pos):
                        self.window_home.closeRoot()
                        running_home = False

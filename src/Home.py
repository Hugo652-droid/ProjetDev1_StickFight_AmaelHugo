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
from src.Settings import Settings


class Home:
    def __init__(self):
        self.font = pygame.font.SysFont('Arial', 20)
        self.window_home = Root(self.font)
        self.reload()

    def launch(self):
        pygame.display.flip()
        running_home = True
        while running_home:
            if self.window_home.settings_screen :
                settings = Settings(self.window_home)
                self.window_home.settings_screen = False
            else :
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            self.window_home.closeRoot()
                            return
                        elif event.key != pygame.K_ESCAPE :
                            self.window_home.closeRoot()
                            running_home = False
                            game = Game()
                            game.launchGame()
                            self.window_home = Root(self.font)
                            self.reload()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.window_home.button_rect_play.collidepoint(event.pos):
                            self.window_home.closeRoot()
                            game = Game()
                            game.launchGame()
                            self.window_home = Root(self.font)
                            self.reload()

                        elif self.window_home.button_rect_quit.collidepoint(event.pos):
                            self.window_home.closeRoot()
                            return

                        if self.window_home.button_rect_setting.collidepoint(event.pos):
                            self.window_home.settings_screen = True
            self.reload()

    def reload(self):
        self.window_home.changeBg('images/imgBackgrounds/mainPageBg/mainBg/img_bg_main.png')
        self.window_home.buttonPlay()
        self.window_home.buttonSetting()
        self.window_home.buttonQuit()
        self.window_home.title('images/imgTexts/textsMain/textsMain/text_title.png')
        self.font = pygame.font.Font("assets/Shooting Star.ttf", 30)
        self.window_home.version(self.font)

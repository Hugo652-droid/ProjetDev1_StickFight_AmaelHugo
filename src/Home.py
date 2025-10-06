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
from Root import Root, INFO_SCREEN
from Game import Game
from Settings import Setting
from Credits import Credit
from assets.Buttons import Button


class Home:
    def __init__(self, window):
        """
        The home page
        :param window: The window of the game
        """
        self.font = pygame.font.Font("assets/Shooting Star.ttf", 20)
        self.window = window
        self.game_mod = 1

        self.button_play = Button(self.window.screen, (INFO_SCREEN.current_w - 160) // 2,
                                  INFO_SCREEN.current_h / 2 + 70,
                                  140,
                                  100,
                                  image='images/imgButtons/mainBtns/mainBtns/play_text_btn.png',
                                  image_scale=(140, 100))
        self.button_rect_play = None

        self.button_setting = Button(self.window.screen, (INFO_SCREEN.current_w - 160) // 2,
                                     INFO_SCREEN.current_h / 2 + 180,
                                     400,
                                     100,
                                     image='images/imgButtons/mainBtns/mainBtns/settings_text_btn.png',
                                     image_scale=(160, 120))
        self.button_rect_setting = None

        self.button_quit = Button(self.window.screen, (INFO_SCREEN.current_w - 160) // 2,
                                  INFO_SCREEN.current_h / 2 + 300,
                                  140,
                                  80,
                                  image='images/imgButtons/quit_text_btn.png',
                                  image_scale=(140, 80))
        self.button_rect_quit = None

        self.title = self.window.title('images/imgTexts/textsMain/textsMain/text_title.png')

    def launch(self):
        """
        Launch of the home page
        :return: The home page manage
        """
        running_home = True
        while running_home:
            if self.window.settings_screen :
                settings = Setting(self.window, self.game_mod)
                self.game_mod = settings.selected_mod
                self.window.settings_screen = False

            if self.window.credits_screen :
                Credit(self.window)
                self.window.credits_screen = False
            else :
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            return
                        elif event.key != pygame.K_ESCAPE :
                            running_home = False
                            game = Game(self.window, self.game_mod)
                            game.launchGame()
                            self.reload()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.button_rect_play.collidepoint(event.pos):
                            game = Game(self.window, self.game_mod)
                            game.launchGame()
                            self.window = Root(self.font)
                            self.reload()

                        elif self.button_rect_quit.collidepoint(event.pos):
                            return

                        if self.button_rect_setting.collidepoint(event.pos):
                            self.window.settings_screen = True

                        if self.title.collidepoint(event.pos):
                            self.window.credits_screen = True
            self.reload()

    def reload(self):
        """
        Display the home page
        :return: The home page displayed
        """
        self.window.changeBackground('images/imgBackgrounds/mainPageBg/mainBg/img_bg_main.png')
        self.window.version(self.font)
        self.button_rect_play = self.button_play.draw()
        self.button_rect_setting = self.button_setting.draw()
        self.button_rect_quit = self.button_quit.draw()
        self.title = self.window.title('images/imgTexts/textsMain/textsMain/text_title.png')

        pygame.display.flip()


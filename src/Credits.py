"""
--
Auteur : Amael Rochat et Hugo Rod
Date de départ : 18.08.2025
Date de fin : 10.10.2025
Projet : Projet Dev 1 (sticKOnion)
--
Nom fichier : Credits.py
Description fichier : Creation des crédits du jeu
--
"""

import pygame

INFO_SCREEN = pygame.display.Info()


class Credit:
    def __init__(self, screen):
        """
        The credit page
        :param screen: The window of the game
        """
        # Assets
        self.font = pygame.font.SysFont('Arial', 20)
        self.screen = screen
        self.color = (255, 0, 0)
        self.screen.changeColor(self.color)
        self.background = "images/imgBackgrounds/mainPageBg/mainBg/img_bg_main.png"

        # Screen info
        self.width_screen = INFO_SCREEN.current_w
        self.height_screen = INFO_SCREEN.current_h

        self.running_credits = True

    def launch(self):
        while self.running_credits:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running_credits = False
                    return

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running_credits = False
                        return

            self.reload()

    def reload(self):
        """
        display the credit page
        :return: The credit page displayed
        """
        self.screen.changeColor(self.color)
        self.screen.changeBackground(self.background)
        self.screen.showCredits()
        pygame.display.flip()

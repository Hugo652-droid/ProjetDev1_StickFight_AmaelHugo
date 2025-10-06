"""
--
Auteur : Amael Rochat et Hugo Rod
Date de départ : 18.08.2025
Date de fin : --.--.----
Projet : Projet Dev 1 (sticKOnion)
--
Nom fichier : Settings.py
Description fichier : Gestion des settings du jeu
--
"""

import pygame

from assets.Buttons import Button

class Setting:
    def __init__(self, screen, selected_mod):
        """
        The settings page
        :param screen: The window of the game
        :param selected_mod: The current game-mod
        """
        self.font = pygame.font.SysFont('Arial', 20)
        self.screen = screen
        self.color = (255,0,0)
        self.games_mods = {
            1: "Mode classique avec armes et pouvoirs",
            2: "Mode à main nue sans armes et sans pouvoirs",
            3: "Mode à main nue avec armes et sans pouvoirs",
        }
        self.mods_buttons = {}
        self.selected_mod = selected_mod
        self.volume_music = pygame.mixer.Channel(0).get_volume() * 100
        self.volume_effect = pygame.mixer.Channel(1).get_volume() * 100
        self.height = pygame.display.Info().current_h // 6
        self.creatModSelector()

        self.running_settings = True
        while self.running_settings:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running_game = False
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.soundBarEffect[0].collidepoint(event.pos):
                        if self.volume_effect > 0:
                            self.volume_effect -= 10
                            pygame.mixer.Channel(1).set_volume(self.volume_effect / 100)
                    elif self.soundBarEffect[1].collidepoint(event.pos):
                        if self.volume_effect < 100:
                            self.volume_effect += 10
                            pygame.mixer.Channel(1).set_volume(self.volume_effect / 100)
                    elif self.soundBarMusic[0].collidepoint(event.pos):
                        if self.volume_music > 0:
                            self.volume_music -= 10
                            pygame.mixer.Channel(0).set_volume(self.volume_music / 100)
                    elif self.soundBarMusic[1].collidepoint(event.pos):
                        if self.volume_music < 100:
                            self.volume_music += 10
                            pygame.mixer.Channel(0).set_volume(self.volume_music / 100)
                    else :
                        for mod in self.mods_buttons:
                            if self.mods_buttons[mod].collidepoint(event.pos):
                                self.selected_mod = mod

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running_game = False
                        return

            self.reload()

    def reload(self):
        """
        Display the settings page
        :return: The settings page displayed
        """
        self.height = pygame.display.Info().current_h // 6
        self.screen.changeBackground('images/imgBackgrounds/mainPageBg/mainBg/img_bg_main.png')

        self.soundBarMusic = self.screen.soundBar(self.volume_music, self.font, "Musique volume", self.height)
        self.height += 100
        self.soundBarEffect = self.screen.soundBar(self.volume_effect, self.font, "Effect volume", self.height)
        self.height += 50

        self.creatModSelector()

        pygame.display.flip()

    def creatModSelector(self):
        """
        Gestion de la selection de mods
        :return: Affichage des boutons de mods
        """
        for mod in self.games_mods:
            if mod == self.selected_mod:
                button_mod = Button(self.screen.screen, 80, self.height+mod*40, 15, 20, text="*", color_text=(0,0,0), color=(255,255,255))
                self.mods_buttons.update({mod: button_mod.draw()})
            else :
                button_mod = Button(self.screen.screen, 80, self.height+mod*40, 15, 20, color=(0,0,0))
                self.mods_buttons.update({mod: button_mod.draw()})
            text_title = self.font.render(self.games_mods[mod], True, (255, 255, 255))
            self.screen.screen.blit(text_title, (100, (self.height + mod * 40)))
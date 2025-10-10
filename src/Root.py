"""
--
Auteur : Amael Rochat et Hugo Rod
Date de départ : 18.08.2025
Date de fin : 10.10.2025
Projet : Projet Dev 1 (sticKOnion)
--
Nom fichier : Root.py
Description fichier : Creation et gestion des fenêtres de l'application
--
"""

from assets.Buttons import Button

import pygame

pygame.display.init()
INFO_SCREEN = pygame.display.Info()


def closeRoot():
    """
    Function for closing the window
    :return: The window closed
    """
    pygame.display.quit()


class Root:
    def __init__(self, font, width_screen=INFO_SCREEN.current_w, height_screen=INFO_SCREEN.current_h):
        """
        The creation and gestion of the window and buttons
        :param font: The font family of the window
        :param width_screen: the width of the window
        :param height_screen: the height of the window
        """
        self.width_screen = width_screen
        self.height_screen = height_screen
        self.font = font

        # Definition of the window size
        self.settings_screen = False
        self.credits_screen = False
        size_window = (self.width_screen, self.height_screen)
        self.screen = pygame.display.set_mode(size_window)

        # Name of the window
        pygame.display.set_caption("SticK.Onion")

        self.soundBars = []

    def changeBackground(self, img_bg):
        """
        Function for changing the background of the window
        :param img_bg: The background image
        :return: The changed background image
        """
        image = pygame.image.load(img_bg).convert()

        background = pygame.transform.scale(image, (self.width_screen, self.height_screen))

        self.screen.blit(background, (0, 0))

        icon_image = pygame.image.load('images/imgCharacters/imgPlayer1/stickman_stand_player1.png')

        pygame.display.set_icon(icon_image)

    def changeColor(self, color):
        """
        Function for changing the color of the window
        :param color: The color of the window
        :return: The colored window
        """
        self.screen.fill(color)

    def title(self, img):
        """
        Function for changing the title of the window
        :param img: The image of the window
        :return: The rectangle of the title
        """
        button_rect_title = pygame.Rect(((self.width_screen - 900) / 2), 100, 1000, 400)
        img_text = pygame.image.load(img)
        img_text = pygame.transform.scale(img_text, (900, 375))
        self.screen.blit(img_text, (button_rect_title.x, button_rect_title.y))

        return button_rect_title

    def scores_player1(self, score, color):
        """
        Display the score of the player1
        :param score: The score of the player 1
        :param color: The color of the player 1
        :return: The score of the player 1 displayed
        """
        score_text = self.font.render(f"{score}", True, color)
        self.screen.blit(score_text, (20, 30))

    def scores_player2(self, score, color):
        """
        Display the score of the player 2
        :param score: The score of the player 2
        :param color: The color of the player 2
        :return: The score of the player 2 displayed
        """
        score_text = self.font.render(f"{score}", True, color)
        text_width = score_text.get_width()
        self.screen.blit(score_text, (self.screen.get_width() - text_width - 20, 30))

    def version(self, font):
        """
        Display the version of the program
        :param font: The font-family of the text
        :return: The rectangle of the text
        """
        version_text = font.render("V1.0 - Amael Rochat & Hugo Rod", True, (0, 0, 0))
        text_rect = version_text.get_rect()

        text_rect.top_left = (20, self.screen.get_height() - text_rect.height - 20)

        self.screen.blit(version_text, text_rect)

        return text_rect

    def win(self, player_win):
        """
        Display the win
        :param player_win: The player who win
        :return: The win screen
        """
        font = pygame.font.Font('assets/Shooting Star.ttf', 200)
        win_text = font.render(f"Winner: {player_win.name}", True, player_win.color)

        text_rect = win_text.get_rect(center=(self.width_screen / 2, self.height_screen / 2))

        self.screen.blit(win_text, text_rect)

    def soundBar(self, volume, font, title, height):
        """
        Display the option for the sound bar
        :param volume: The current volume
        :param font: The font-family of the text
        :param title: The title of the sound bar
        :param height: The height of the sound bar
        :return: Buttons of the sound bar
        """
        i = 0
        text_title = font.render(title, True, (255, 255, 255))
        self.screen.blit(text_title, (80, (height - 50)))

        volume_down = Button(self.screen, 80, height, 15, 40, font=font, text=f"<",
                             color_text=(255, 255, 255), color=(0, 0, 0))
        while i <= 10:
            self.soundBars.append(pygame.rect.Rect((i*20+100), height, 15, 40))
            i += 1
        volume_up = Button(self.screen, (i*20+80), height, 15, 40, font=font, text=f">",
                           color_text=(255, 255, 255), color=(0, 0, 0))

        # Creation of the sound bar
        volume_index = 0
        for soundBar in self.soundBars:
            if volume > volume_index:
                pygame.draw.rect(self.screen, (0, 0, 255), soundBar)
            elif volume <= volume_index:
                pygame.draw.rect(self.screen, (0, 0, 0), soundBar)
            volume_index += 10
            if volume_index >= 100:
                break

        return volume_down.draw(), volume_up.draw()

    def showCredits(self):
        """
        Display the credits text
        :return: The credits text displayed
        """

        # Assets of the credit
        white = (0, 0, 0)
        section_font = pygame.font.Font('assets/Shooting Star.ttf', 30)  # Sections (ART / DEV)
        text_font = pygame.font.Font('assets/Shooting Star.ttf', 20)  # Détails

        # The title of the credit
        credits_text = pygame.font.Font('assets/Shooting Star.ttf', 150).render(f"Credits", True, (0, 0, 0))
        text_rect = credits_text.get_rect(center=(self.width_screen / 2, self.height_screen / 3))
        self.screen.blit(credits_text, text_rect)

        # Contain of the credit
        credits_text = [
            ("ART - Directeur artistique : Amael Rochat", section_font),
            ("Amael Rochat - Textes boutons et titres, choix des polices, choix des images", text_font),
            ("Hugo Rod - Choix des musique", text_font),
            ("", text_font),
            ("DEVELOPPEMENT - Directeur develeoppement : Hugo Rod", section_font),
            ("Amael - Developpement", text_font),
            ("Hugo - Developpement", text_font),
        ]

        start_y = self.height_screen - (self.height_screen // 2)

        y = start_y
        for text, font in credits_text:
            rendered_text = font.render(text, True, white)
            text_rect = rendered_text.get_rect(center=(self.width_screen // 2, y))
            self.screen.blit(rendered_text, text_rect)
            y += font.size(text)[1] + 10

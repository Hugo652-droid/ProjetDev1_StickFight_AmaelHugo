"""
--
Auteur : Amael Rochat et Hugo Rod
Date de départ : 18.08.2025
Date de fin : 10.10.2025
Projet : Projet Dev 1 (sticKOnion)
--
Nom fichier : Main.py
Description fichier : Gestion des buttons
--
"""

import pygame

pygame.display.init()

INFO_SCREEN = pygame.display.Info()


class Button:
    def __init__(self, screen, left_position, top_position, width, height, font=None, image=None, image_scale=None,
                 text=None, color=None, color_text=None):
        """
        Button of the game
        :param screen: The window of the game
        :param left_position: La position x
        :param top_position: La position y
        :param width: width of the button
        :param height: height of the button
        :param font: the font-family of the button (optional)
        :param image: image of the button (optional)
        :param image_scale: width and height of the image (width, height) (optional)
        :param text: The text of the button (optional)
        :param color: color of the button (r, g, b) (optional)
        :param color_text: color of the button's text (r, g, b) (optional)
        """
        self.width = width
        self.height = height
        self.screen = screen
        self.left_position = left_position
        self.top_position = top_position
        self.image = image
        self.image_scale = image_scale
        self.text = text
        self.color = color
        self.color_text = color_text
        self.font = font
        self.button = pygame.Rect(self.left_position, self.top_position, self.width, self.height)

    def draw(self):
        """
        Display the button of the game
        :return: The button displayed
        """
        # Adding the color
        if self.color:
            pygame.draw.rect(self.screen, self.color, self.button)

        # Adding the image
        if self.image:
            image = pygame.image.load(self.image).convert_alpha()
            if self.image_scale:
                image = pygame.transform.scale(image, self.image_scale)
            self.screen.blit(image, (self.button.x, self.button.y))

        # Adding the text
        if self.text and self.color_text:
            if self.font:
                text = self.font.render(self.text, True, self.color_text)
                self.screen.blit(text, (self.button.x, self.button.y))

        return self.button

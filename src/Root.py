"""
--
Auteur : Amael Rochat et Hugo Rod
Date de départ : 18.08.2025
Date de fin : --.--.----
Projet : Projet Dev 1 (sticKOnion)
--
Nom fichier : Root.py
Description fichier : Creation et gestion des fenêtres de l'application
--
"""

import pygame

pygame.display.init()
INFO = pygame.display.Info()

class Root:
    def __init__(self, font, width_screen=INFO.current_w, height_screen=INFO.current_h):
        self.width_screen = width_screen
        self.height_screen = height_screen

        self.font = font
        # Définir les dimensions de l'écran
        self.placer_screen_button_width = (self.width_screen - 140) // 2
        self.settings_screen = False
        self.credits_screen = False

        size_window = (self.width_screen, self.height_screen)
        self.screen = pygame.display.set_mode(size_window)

        self.rect = self.screen.get_rect()


        # Nom de la fenêtre
        pygame.display.set_caption("SticK.Onion")

    def closeRoot(self):
        pygame.display.quit()

    def changeBg(self, img_bg):
        # Charge l'image depuis le fichier 'mon_image.png'
        image_a_afficher = pygame.image.load(img_bg)

        # Convertit l'image dans un format optimal pour l'affichage
        image_convertie = image_a_afficher.convert()

        background = pygame.transform.scale(image_convertie, (self.width_screen, self.height_screen))

        self.screen.blit(background, (0,0))

        icon_image = pygame.image.load('images/imgCharacters/imgPlayer1/stickman_stand_player1.png')

        pygame.display.set_icon(icon_image)

    def changeColor(self, color):
        self.screen.fill(color)

################################################################################################ Accueil

    def buttonPlay(self):
        # Définir la position et la taille du bouton
        self.button_rect_play = pygame.Rect(self.placer_screen_button_width, self.height_screen / 2 + 70, 140, 100)

        # Ajouter du texte sur le bouton
        img_text = pygame.image.load('images/imgButtons/mainBtns/mainBtns/play_text_btn.png')

        img_text = pygame.transform.scale(img_text, (140, 100))

        self.screen.blit(img_text, (self.button_rect_play.x, self.button_rect_play.y))

    def buttonSetting(self):
        # Définir la position et la taille du bouton
        self.button_rect_setting = pygame.Rect((self.width_screen - 160) // 2, self.height_screen / 2 + 180, 400, 100)

        # Ajouter du texte sur le bouton
        img_text = pygame.image.load('images/imgButtons/mainBtns/mainBtns/settings_text_btn.png')

        img_text = pygame.transform.scale(img_text, (160, 120))

        self.screen.blit(img_text, (self.button_rect_setting.x, self.button_rect_setting.y))

    def buttonQuit(self):
        # Définir la position et la taille du bouton
        self.button_rect_quit = pygame.Rect(self.placer_screen_button_width, self.height_screen / 2 + 300, 400, 100)

        # Ajouter du texte sur le bouton
        img_text = pygame.image.load('images/imgButtons/quit_text_btn.png')
        img_text = pygame.transform.scale(img_text, (140, 80))
        self.screen.blit(img_text, (self.button_rect_quit.x, self.button_rect_quit.y))

    def buttonRestart(self):
        # Définir la position et la taille du bouton
        self.button_rect_restart = pygame.Rect(self.placer_screen_button_width, self.height_screen / 2 + 170, 400, 100)

        # Ajouter du texte sur le bouton
        img_text = pygame.image.load('images/imgButtons/gameBtns/pausedBtns/restart_text_btn.png')
        img_text = pygame.transform.scale(img_text, (140, 100))
        self.screen.blit(img_text, (self.button_rect_restart.x, self.button_rect_restart.y))

    def title(self,img):
        self.button_rect_title = pygame.Rect(((self.width_screen - 900) / 2), 100, 1000, 1000)

        # Ajouter du texte sur le bouton
        img_text = pygame.image.load(img)

        img_text = pygame.transform.scale(img_text, (900, 375))

        self.screen.blit(img_text, (self.button_rect_title.x, self.button_rect_title.y))

        pygame.display.flip()

    def scores_player1(self, font, score, player1):
        score_text = font.render(f"{score}",True, player1.color)
        self.screen.blit(score_text, (20, -30))

    def scores_player2(self, font, score, player2):
        score_text = font.render(f"{score}",True, player2.color)
        text_width = score_text.get_width()
        self.screen.blit(score_text, (self.screen.get_width() - text_width - 20, -30))

    def version(self, font):
        version_text = font.render("V1.0 - Amael Rochat & Hugo Rod", True, (0, 0, 0))
        self.text_rect = version_text.get_rect()

        self.text_rect.topleft = (20, self.screen.get_height() - self.text_rect.height - 20)

        self.screen.blit(version_text, self.text_rect)

    def win(self, player_win):
        font = pygame.font.Font('assets/Shooting Star.ttf', 200)
        win_text = font.render(f"Winner: {player_win.name}", True, player_win.color)

        text_rect = win_text.get_rect(center=(self.width_screen / 2, self.height_screen / 2))

        self.screen.blit(win_text, text_rect)

    ################################################################################################ Game

    def stop(self):
        self.changeBg('images/imgBackgrounds/gamePageBgs/pausedBg/img_bg_game_paused.png')

        self.buttonQuit()

        self.buttonRestart()

        self.title('images/imgTexts/textsGame/textsPaused/title_paused.png')

    ################################################################################################ Settings

    def soundBar(self, volume, font, title, height):
        i = 0


        text_title = font.render(title, True, (255, 255, 255))
        self.screen.blit(text_title, (80, (height - 50)))

        text_down = font.render(f"<",True, (255,255,255))
        volume_down = pygame.rect.Rect(80, height, 15, 40)
        pygame.draw.rect(self.screen, (0,0,0), volume_down)
        self.screen.blit(text_down, (volume_down.x, volume_down.centery - 13))

        self.soundBars = []
        while i <= 10:
            self.soundBars.append(pygame.rect.Rect((i*20+100), height, 15, 40))
            i += 1

        text_up = font.render(f">", True, (255, 255, 255))
        volume_up = pygame.rect.Rect((i*20+80), height, 15, 40)
        pygame.draw.rect(self.screen, (0, 0, 0), volume_up)
        self.screen.blit(text_up, (volume_up.x, volume_up.centery - 13))

        volume_index = 0
        for soundBar in self.soundBars:
            if volume > volume_index:
                pygame.draw.rect(self.screen, (0,0,255), soundBar)
            elif volume <= volume_index:
                pygame.draw.rect(self.screen, (0,0,0), soundBar)
            volume_index += 10
            if volume_index >= 100:
                break

        return volume_down, volume_up

    def modSelector(self, font, games_mods, selected_mod, height):
        for i in range(len(games_mods)):
            text_title = font.render(games_mods[i+1], True, (255, 255, 255))
            self.screen.blit(text_title, (120, (i*50+height)))
            if i+1 != selected_mod:
                text_down = font.render(f"[*]", True, (0, 255, 0))
                volume_down = pygame.rect.Rect(80, (i*50+height), 15, 40)
                pygame.draw.rect(self.screen, (0, 0, 0), volume_down)
                self.screen.blit(text_down, (volume_down.x, volume_down.centery - 13))
            else:
                text_down = font.render(f"[ ]", True, (255, 255, 255))
                volume_down = pygame.rect.Rect(80, (i*50+height), 15, 40)
                pygame.draw.rect(self.screen, (0, 0, 0), volume_down)
                self.screen.blit(text_down, (volume_down.x, volume_down.centery - 13))

    ################################################################################################ Credits

    def titleCredits(self, font):
        credits_text = font.render(f"Credits", True, (0, 0, 0))

        text_rect = credits_text.get_rect(center=(self.width_screen / 2, self.height_screen / 3))

        self.screen.blit(credits_text, text_rect)

    def showCredits(self):
        """
        Affiche les crédits de manière statique sur l'écran fourni.
        A appeler dans ta page pour afficher les crédits.
        """

        # Couleur et polices
        white = (0, 0, 0)
        section_font = pygame.font.Font('assets/Shooting Star.ttf', 30)    # Sections (ART / DEV)
        text_font = pygame.font.Font('assets/Shooting Star.ttf', 20)       # Détails

        # Contenu des crédits
        credits = [
            ("ART - Directeur artistique : Amael Rochat", section_font),
            ("Amael Rochat - Textes boutons et titres", text_font),
            ("Hugo Rod - Musique", text_font),
            ("", text_font),
            ("DEVELOPPEMENT - Directeur develeoppement : Hugo Rod", section_font),
            ("Amael - Developpement", text_font),
            ("Hugo - Developpement", text_font),
        ]

        start_y = self.height_screen - (self.height_screen // 2)

        y = start_y
        for text, font in credits:
            rendered_text = font.render(text, True, white)
            text_rect = rendered_text.get_rect(center=(self.width_screen // 2, y))
            self.screen.blit(rendered_text, text_rect)
            y += font.size(text)[1] + 10

        # Mettre à jour l'écran après affichage
        pygame.display.flip()

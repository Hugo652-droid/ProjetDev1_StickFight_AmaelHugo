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

class Root:
    def __init__(self, pygame):

        self.launchRoot(pygame)

    def launchRoot(self, pygame):
        # Définir les dimensions de l'écran

        info = pygame.display.Info()

        self.largeur_ecran = info.current_w
        self.hauteur_ecran = info.current_h

        self.placer_ecran_button = (self.largeur_ecran - 400) / 2

        taille_fenetre = (self.largeur_ecran, self.hauteur_ecran)
        self.screen = pygame.display.set_mode(taille_fenetre)
        self.rect = self.screen.get_rect()

        # Nom de la fenêtre
        pygame.display.set_caption("SticK.Onion")

    def closeRoot(self, pygame):
        pygame.display.quit()

    def changeBg(self, img_bg):
        # Charge l'image depuis le fichier 'mon_image.png'
        image_a_afficher = pygame.image.load(img_bg)

        # Convertit l'image dans un format optimal pour l'affichage
        image_convertie = image_a_afficher.convert()

        background = pygame.transform.scale(image_convertie, (self.largeur_ecran, self.hauteur_ecran))

        self.screen.blit(background, (0,0))

        icon_image = pygame.image.load('images/imgCharacters/imgPlayer1/stickman_stand_player1.png')

        pygame.display.set_icon(icon_image)

    def changeColor(self, color):
        self.screen.fill(color)

################################################################################################ Accueil

    def buttonPlay(self):
        # Définir la position et la taille du bouton
        self.button_rect = pygame.Rect(self.placer_ecran_button, 600, 400, 160)

        # Ajouter du texte sur le bouton
        img_text = pygame.image.load('images/imgButtons/mainBtns/mainBtns/play_text_btn.png')

        img_text = pygame.transform.scale(img_text, (400, 160))

        self.screen.blit(img_text, (self.button_rect.x, self.button_rect.y))

    def buttonQuit(self):
        # Définir la position et la taille du bouton
        self.button_rect_quit = pygame.Rect(self.placer_ecran_button, 780, 400, 160)

        # Ajouter du texte sur le bouton
        img_text = pygame.image.load('images/imgButtons/quit_text_btn.png')
        img_text = pygame.transform.scale(img_text, (400, 160))
        self.screen.blit(img_text, (self.button_rect_quit.x, self.button_rect_quit.y))

    def buttonRestart(self):
        # Définir la position et la taille du bouton
        self.button_rect_restart = pygame.Rect(self.placer_ecran_button, 600, 400, 160)

        # Ajouter du texte sur le bouton
        img_text = pygame.image.load('images/imgButtons/gameBtns/pausedBtns/restart_text_btn.png')
        img_text = pygame.transform.scale(img_text, (400, 160))
        self.screen.blit(img_text, (self.button_rect_restart.x, self.button_rect_restart.y))

    def title(self,img):
        self.button_rect_title = pygame.Rect(((self.largeur_ecran - 1200) / 2), 100, 1000, 1000)

        # Ajouter du texte sur le bouton
        img_text = pygame.image.load(img)

        img_text = pygame.transform.scale(img_text, (1200, 500))

        self.screen.blit(img_text, (self.button_rect_title.x, self.button_rect_title.y))

        pygame.display.flip()

    def scores(self, font, score1, score2):
        score_text = font.render(f"Scores:"
                                 f"    Joueur 1: {score1}  -  Joueur 2: {score2}",True, (0, 0, 0))
        self.screen.blit(score_text, (20, 20))

    def version(self, font):
        version_text = font.render("V1.0", True, (0, 0, 0))
        text_rect = version_text.get_rect()

        text_rect.topleft = (20, self.screen.get_height() - text_rect.height - 20)

        self.screen.blit(version_text, text_rect)

    def win(self, playerWin):
        font = pygame.font.SysFont('Arial', 200)
        win_text = font.render(f"VAINQUEUR:"
                                 f" {playerWin.name}", True, (0, 0, 0))
        self.screen.blit(win_text, (0, self.hauteur_ecran / 2))

    ################################################################################################ Game

    def stopButton(self, paused):
        self.button_rect_stop = pygame.Rect((self.largeur_ecran - 80), 10, 1000, 1000)

        if paused == False:
            img_stop = pygame.image.load('images/imgButtons/gameBtns/gameBtns/img_stop_button.png')

        else:
            img_stop = pygame.image.load('images/imgButtons/gameBtns/pausedBtns/img_paused_button.png')


        img_stop = pygame.transform.scale(img_stop, (70, 100))

        self.screen.blit(img_stop, (self.button_rect_stop.x, self.button_rect_stop.y))

        pygame.display.flip()

    def stop(self):
        self.changeBg('images/imgBackgrounds/gamePageBgs/pausedBg/img_bg_game_paused.png')

        self.buttonQuit()

        self.buttonRestart()

        self.title('images/imgTexts/textsGame/textsPaused/title_paused.png')

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

        # Nom de la fenêtre
        pygame.display.set_caption("SticK.Onion")

    def closeRoot(self, pygame):
        pygame.display.quit()

    def changeBg(self):
        # Charge l'image depuis le fichier 'mon_image.png'
        image_a_afficher = pygame.image.load('images/img.png')

        # Convertit l'image dans un format optimal pour l'affichage
        image_convertie = image_a_afficher.convert()

        background = pygame.transform.scale(image_convertie, (self.largeur_ecran, self.hauteur_ecran))

        self.screen.blit(background, (0,0))



    def changeColor(self, color):
        self.screen.fill(color)

################################################################################################ Accueil

    def buttonPlay(self):
        # Définir la position et la taille du bouton
        self.button_rect = pygame.Rect(self.placer_ecran_button, 600, 400, 160)

        # Dessiner le bouton
        pygame.draw.rect(self.screen, (255, 255, 255), self.button_rect)

        # Ajouter du texte sur le bouton
        img_text = pygame.image.load('images/jouer_text_test.png')

        img_text = pygame.transform.scale(img_text, (400, 160))

        self.screen.blit(img_text, (self.button_rect.x, self.button_rect.y))

    def buttonQuit(self):
        # Définir la position et la taille du bouton
        self.button_rect_quit = pygame.Rect(self.placer_ecran_button, 780, 400, 160)

        # Ajouter du texte sur le bouton
        img_text = pygame.image.load('images/quitter_text_test.png.png.png')
        img_text = pygame.transform.scale(img_text, (400, 160))
        self.screen.blit(img_text, (self.button_rect_quit.x, self.button_rect_quit.y))

    def title(self):
        self.button_rect_title = pygame.Rect(((self.largeur_ecran - 1200) / 2), 100, 1000, 1000)

        # Ajouter du texte sur le bouton
        img_text = pygame.image.load('images/Image titre.png')

        img_text = pygame.transform.scale(img_text, (1200, 500))

        self.screen.blit(img_text, (self.button_rect_title.x, self.button_rect_title.y))

        pygame.display.flip()

################################################################################################ Game

    def stopButton(self):
        self.button_rect_stop = pygame.Rect(((self.largeur_ecran - 80)), 10, 1000, 1000)

        img_stop = pygame.image.load('images/img_stopButton.png')

        img_stop = pygame.transform.scale(img_stop, (70, 100))

        self.screen.blit(img_stop, (self.button_rect_stop.x, self.button_rect_stop.y))

        pygame.display.flip()

    def stop(self):
        self.screen.fill((100, 100, 100, 128))










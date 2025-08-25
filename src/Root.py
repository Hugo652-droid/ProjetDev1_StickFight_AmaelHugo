import pygame


class Root:
    def __init__(self, pygame):

        self.launchRoot(pygame)

    def launchRoot(self, pygame):
        # Définir les dimensions de l'écran
        self.largeur_ecran = 1920
        self.hauteur_ecran = 1080
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

        pygame.display.flip()


    def changeColor(self, color):
        self.screen.fill(color)
        pygame.display.flip()

    def buttonPlay(self):
        # Définir la position et la taille du bouton
        self.button_rect = pygame.Rect(760, 310, 400, 160)

        # Dessiner le bouton
        pygame.draw.rect(self.screen, (255, 255, 255), self.button_rect)

        # Ajouter du texte sur le bouton
        img_text = pygame.image.load('images/jouer_text_test.png')

        img_text = pygame.transform.scale(img_text, (400, 160))

        self.screen.blit(img_text, (self.button_rect.x, self.button_rect.y))

        # Mettre à jour l'affichage
        pygame.display.flip()

    def buttonSettings(self):
        # Définir la position et la taille du bouton
        self.button_rect_settings = pygame.Rect(760, 500, 400, 160)

        # Ajouter du texte sur le bouton
        img_text = pygame.image.load('images/options_text_test.png.png')

        img_text = pygame.transform.scale(img_text, (400, 160))

        self.screen.blit(img_text, (self.button_rect_settings.x, self.button_rect_settings.y))

        # Mettre à jour l'affichage
        pygame.display.flip()

    def buttonQuit(self):
        # Définir la position et la taille du bouton
        self.button_rect_quit = pygame.Rect(760, 690, 400, 160)

        # Ajouter du texte sur le bouton
        img_text = pygame.image.load('images/quitter_text_test.png.png.png')

        img_text = pygame.transform.scale(img_text, (400, 160))

        self.screen.blit(img_text, (self.button_rect_quit.x, self.button_rect_quit.y))

        # Mettre à jour l'affichage
        pygame.display.flip()





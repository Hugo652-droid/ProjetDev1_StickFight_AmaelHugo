import pygame


class Root:
    def __init__(self, pygame):

        self.launchRoot(pygame)

    def launchRoot(self, pygame):
        # Définir les dimensions de l'écran
        largeur_ecran = 1920
        hauteur_ecran = 1080
        taille_fenetre = (largeur_ecran, hauteur_ecran)
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

        self.screen.blit(image_convertie, (0,0))

        pygame.display.flip()


    def changeColor(self, color):
        self.screen.fill(color)
        pygame.display.flip()

    def buttonPlay(self):
        # Définir la position et la taille du bouton
        self.button_rect = pygame.Rect(960, 250, 200, 80)

        # Police pour le texte
        font = pygame.font.Font(None, 36)

        # Dessiner le bouton
        pygame.draw.rect(self.screen, (255, 255, 255), self.button_rect)

        # Ajouter du texte sur le bouton
        text = font.render("Jouer", True, (0, 0, 0))
        self.screen.blit(text, (self.button_rect.x + 50, self.button_rect.y + 25))

        # Mettre à jour l'affichage
        pygame.display.flip()

    def buttonQuit(self):
        # Définir la position et la taille du bouton
        self.button_rect_quit = pygame.Rect(960, 340, 200, 80)

        # Police pour le texte
        font = pygame.font.Font(None, 36)

        # Dessiner le bouton
        pygame.draw.rect(self.screen, (255, 255, 255), self.button_rect_quit)

        # Ajouter du texte sur le bouton
        text = font.render("Quitter", True, (0, 0, 0))
        self.screen.blit(text, (self.button_rect_quit.x + 50, self.button_rect_quit.y + 25))

        # Mettre à jour l'affichage
        pygame.display.flip()





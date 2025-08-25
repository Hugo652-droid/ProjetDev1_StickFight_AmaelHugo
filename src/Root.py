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

        self.screen.blit(image_convertie, (100, 50))

        pygame.display.flip()






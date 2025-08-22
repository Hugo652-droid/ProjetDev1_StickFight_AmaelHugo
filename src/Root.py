import pygame


class Root:
    def __init__(self, pygame):

        self.launchRoot(pygame)

    def launchRoot(self, pygame):
        # Définir les dimensions de l'écran
        largeur_ecran = 1920
        hauteur_ecran = 1080
        taille_fenetre = (largeur_ecran, hauteur_ecran)
        screen = pygame.display.set_mode(taille_fenetre)

        # Nom de la fenêtre
        pygame.display.set_caption("SticK.Onion")

    def closeRoot(self, pygame):
        pygame.display.quit()





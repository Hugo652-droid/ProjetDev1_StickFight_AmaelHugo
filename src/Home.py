import pygame

#Initialisation de Pygame
pygame.init()

#Définir les dimensions de l'écran
largeur_ecran = 1920
hauteur_ecran = 1080
taille_fenetre = (largeur_ecran, hauteur_ecran)
screen = pygame.display.set_mode(taille_fenetre)

#Nom de la fenêtre
pygame.display.set_caption("SticK.Onion")

#Boucle d'événements (la boucle du jeu)
running = True
while running:
    #Gérer les événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Si l'utilisateur clique sur la croix pour fermer
            running = False

    pygame.display.flip() # Met à jour l'intégralité de l'écran

# Quitter Pygame proprement
pygame.quit()

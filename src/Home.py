import pygame
from src.Root import Root
from src.Game import Game

class Home :
    def __init__(self):
        windowHome = Root(pygame)
        windowHome.changeBg('images/img_bg_main.png')
        windowHome.buttonPlay()
        windowHome.buttonQuit()
        windowHome.title('images/Image titre.png')
        self.font = pygame.font.SysFont('Arial', 25)
        windowHome.version(self.font)
        pygame.display.flip()
        runningHome = True
        while runningHome:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        windowHome.closeRoot(pygame)
                        runningHome = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if windowHome.button_rect.collidepoint(event.pos):
                        windowHome.closeRoot(pygame)
                        runningHome = False
                        game = Game()

                    if windowHome.button_rect_quit.collidepoint(event.pos):
                        windowHome.closeRoot(pygame)
                        runningHome = False
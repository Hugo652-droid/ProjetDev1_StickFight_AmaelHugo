import pygame

from src.assets.InputBox import InputBox
from src.Root import Root

class Credits:
    def __init__(self, screen):
        self.font = pygame.font.SysFont('Arial', 20)
        self.screen = screen
        self.color = (255,0,0)
        self.screen.changeColor(self.color)
        self.bg = "images/imgBackgrounds/mainPageBg/mainBg/img_bg_main.png"
        self.font_title = pygame.font.Font('assets/Shooting Star.ttf', 200)


        self.running_credits = True
        while self.running_credits:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running_game = False
                    return
            
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running_game = False
                        return

            self.reload()

    def reload(self):
        self.screen.changeColor(self.color)

        self.screen.changeBg(self.bg)

        self.screen.titleCredits(self.font_title)

        self.screen.show_credits()



        pygame.display.flip()





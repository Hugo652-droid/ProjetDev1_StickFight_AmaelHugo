import pygame

from src.assets.InputBox import InputBox

class Settings:
    def __init__(self, screen):
        self.font = pygame.font.SysFont('Arial', 20)
        self.screen = screen
        self.color = (255,0,0)
        self.screen.changeColor(self.color)
        input_box2 = InputBox(200, 500, 140, 32, self.font, (0, 0, 0), (255, 255, 255))
        self.input_boxes = [input_box2]
        self.volume = 100


        self.running_settings = True
        while self.running_settings:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running_game = False
                    return
                for box in self.input_boxes:
                    box.handleEvent(event)
                if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.screen.volume_down.collidepoint(event.pos):
                            if self.volume > 0:
                                self.volume -= 10
                        if self.screen.volume_up.collidepoint(event.pos):
                            if self.volume < 100:
                                self.volume += 10

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running_game = False
                        return

            for box in self.input_boxes:
                box.update()

            self.reload()

    def reload(self):
        self.screen.changeBg('images/imgBackgrounds/mainPageBg/mainBg/img_bg_main.png')

        for box in self.input_boxes:
            box.draw(self.screen.screen)

        self.screen.soundBar(self.volume, self.font)

        pygame.display.flip()





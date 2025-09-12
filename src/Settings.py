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
        self.volume_main = max(pygame.mixer.Channel(0).get_volume() * 100, pygame.mixer.Channel(1).get_volume() * 100)
        self.volume_effect = pygame.mixer.Channel(0).get_volume() * 100
        self.volume_musique = pygame.mixer.Channel(1).get_volume() * 100
        print(self.volume_main)


        self.running_settings = True
        while self.running_settings:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running_game = False
                    return
                for box in self.input_boxes:
                    box.handleEvent(event)
                if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.soundBarMain[0].collidepoint(event.pos):
                            if self.volume_main > 0:
                                self.volume_main -= 10
                                pygame.mixer.Channel(0).set_volume(min(self.volume_main, self.volume_musique) / 100)
                                pygame.mixer.Channel(1).set_volume(min(self.volume_main, self.volume_effect) / 100)
                        elif self.soundBarMain[1].collidepoint(event.pos):
                            if self.volume_main < 100:
                                self.volume_main += 10
                                pygame.mixer.Channel(0).set_volume(min(self.volume_main, self.volume_musique) / 100)
                                pygame.mixer.Channel(1).set_volume(min(self.volume_main, self.volume_effect) / 100)
                        elif self.soundBarEffect[0].collidepoint(event.pos):
                            if self.volume_effect > 0:
                                self.volume_effect -= 10
                                pygame.mixer.Channel(0).set_volume(self.volume_effect / 100)
                                pygame.mixer.Channel(1).set_volume(self.volume_effect / 100)
                        elif self.soundBarEffect[1].collidepoint(event.pos):
                            if self.volume_effect < 100:
                                self.volume_effect += 10
                                pygame.mixer.Channel(0).set_volume(self.volume_effect / 100)
                                pygame.mixer.Channel(1).set_volume(self.volume_effect / 100)
                        elif self.soundBarMusic[0].collidepoint(event.pos):
                            if self.volume_musique > 0:
                                self.volume_musique -= 10
                                pygame.mixer.Channel(0).set_volume(self.volume_musique / 100)
                                pygame.mixer.Channel(1).set_volume(self.volume_musique / 100)
                        elif self.soundBarMusic[1].collidepoint(event.pos):
                            if self.volume_musique < 100:
                                self.volume_musique += 10
                                pygame.mixer.Channel(0).set_volume(self.volume_musique / 100)
                                pygame.mixer.Channel(1).set_volume(self.volume_musique / 100)

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

        self.soundBarMain = self.screen.soundBar(self.volume_main, self.font, "Main volume", pygame.display.Info().current_h // 4)

        self.soundBarMusic = self.screen.soundBar(self.volume_musique, self.font, "Musique volume", (pygame.display.Info().current_h // 4 + 100))

        self.soundBarEffect = self.screen.soundBar(self.volume_effect, self.font, "Effect volume", (pygame.display.Info().current_h // 4 + 200))

        pygame.display.flip()





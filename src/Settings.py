import pygame

from src.assets.InputBox import InputBox

class Settings:
    def __init__(self, screen):
        self.font = pygame.font.SysFont('Arial', 20)
        self.screen = screen
        self.color = (255,0,0)
        self.games_mods = {
            1: "Mode classique avec armes et pouvoirs",
            2: "Mode à main nue sans armes et sans pouvoirs",
        }

        self.selected_mod = 1
        self.screen.changeColor(self.color)
        self.volume_music = pygame.mixer.Channel(0).get_volume() * 100
        self.volume_effect = pygame.mixer.Channel(1).get_volume() * 100

        self.running_settings = True
        while self.running_settings:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running_game = False
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.soundBarEffect[0].collidepoint(event.pos):
                        if self.volume_effect > 0:
                            self.volume_effect -= 10
                            pygame.mixer.Channel(1).set_volume(self.volume_effect / 100)
                    elif self.soundBarEffect[1].collidepoint(event.pos):
                        if self.volume_effect < 100:
                            self.volume_effect += 10
                            pygame.mixer.Channel(1).set_volume(self.volume_effect / 100)
                    elif self.soundBarMusic[0].collidepoint(event.pos):
                        if self.volume_music > 0:
                            self.volume_music -= 10
                            pygame.mixer.Channel(0).set_volume(self.volume_music / 100)
                    elif self.soundBarMusic[1].collidepoint(event.pos):
                        if self.volume_music < 100:
                            self.volume_music += 10
                            pygame.mixer.Channel(0).set_volume(self.volume_music / 100)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running_game = False
                        return

            self.reload()

    def reload(self):
        self.screen.changeBg('images/imgBackgrounds/mainPageBg/mainBg/img_bg_main.png')

        self.soundBarMusic = self.screen.soundBar(self.volume_music, self.font, "Musique volume", (pygame.display.Info().current_h // 4))

        self.soundBarEffect = self.screen.soundBar(self.volume_effect, self.font, "Effect volume", (pygame.display.Info().current_h // 4 + 100))

        self.modSelector = self.screen.modSelector(self.font, self.games_mods, self.selected_mod, 100)

        pygame.display.flip()





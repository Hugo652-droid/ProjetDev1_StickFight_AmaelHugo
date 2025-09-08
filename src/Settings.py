import pygame

from src.Root import Root

class InputBox:
    def __init__(self, x, y, w, h, font, color_active, color_inactive, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color_inactive = color_inactive
        self.color_active = color_active
        self.color = color_inactive
        self.text = text
        self.font = font
        self.txt_surface = font.render(text, True, self.color)
        self.active = False

    def handleEvent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = self.color_active if self.active else self.color_inactive
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = self.font.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)

class Settings:
    def __init__(self):
        self.font = pygame.font.SysFont('Arial', 20)
        self.window_settings = Root(self.font, width_screen=pygame.display.Info().current_w//2, height_screen=pygame.display.Info().current_h//2)
        self.window_settings.changeBg('images/imgBackgrounds/gamePageBgs/pausedBg/img_bg_game_paused.png')
        input_box1 = InputBox(100, 100, 140, 32, self.font, (0, 0, 0), (255, 255, 255))
        input_box2 = InputBox(100, 300, 140, 32, self.font, (0, 0, 0), (255, 255, 255))
        input_boxes = [input_box1, input_box2]

        self.running_settings = True
        while self.running_settings:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running_game = False
                for box in input_boxes:
                    box.handleEvent(event)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running_game = False

            for box in input_boxes:
                box.update()

            for box in input_boxes:
                box.draw(self.window_settings.screen)

        self.window_settings.closeRoot()



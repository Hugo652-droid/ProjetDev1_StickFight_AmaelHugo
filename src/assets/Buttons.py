import pygame

INFO_SCREEN = pygame.display.Info()

class Button:
    def __init__(self, screen, left_position, top_position, width, height, font=None, image=None, image_scale=None, text=None, color=None, color_text=None):
        self.width = width
        self.height = height
        self.screen = screen
        self.left_position = left_position
        self.top_position = top_position
        self.image = image
        self.image_scale = image_scale
        self.text = text
        self.color = color
        self.color_text = color_text
        self.font = font
        self.button = pygame.Rect(self.left_position, self.top_position, self.width, self.height)

    def draw(self):
        # Adding the color
        if self.color:
            pygame.draw.rect(self.screen, self.color, self.button)

        # Adding the image
        if self.image:
            image = pygame.image.load(self.image).convert_alpha()
            if self.image_scale:
                image = pygame.transform.scale(image, self.image_scale)
            self.screen.blit(image, (self.button.x, self.button.y))

        # Adding the text
        if self.text and self.color_text:
            if self.font:
                text = self.font.render(self.text, True, self.color_text)
                self.screen.blit(text, (self.button.x, self.button.y))

        return self.button
class Map:
    def __init__(self, window, pygame, x, y):
        self.pygame = pygame
        self.window = window
        self.img_floor = self.pygame.image.load('./images/floor_test.png')
        self.x = x
        self.y = y
        self.rect = self.img_floor.get_rect()
        self.info_screen = pygame.display.Info()

    def draw(self, screen):
        self.img_floor = self.pygame.transform.scale(self.img_floor, ((self.info_screen.current_w-200), 200))
        self.rect = self.img_floor.get_rect()
        self.rect.center = (self.x, self.y)
        screen.blit(self.img_floor, self.rect)


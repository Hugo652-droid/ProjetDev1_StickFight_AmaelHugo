
class Settings:
    def __init__(self, windowSettings, pygame):

        windowSettings.changeColor((255, 255, 255))
        runningSettings = True
        while runningSettings:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        runningSettings.closeRoot(pygame)
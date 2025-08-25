import pygame

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()

# Starting position
x, y = 300, 220
a, b = 200, 320
speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get pressed keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    if keys[pygame.K_a]:
        a -= 10
    if keys[pygame.K_d]:
        a += 10
    if keys[pygame.K_w]:
        b -= 10
    if keys[pygame.K_s]:
        b += 10

    # 1. Clear the screen each frame
    screen.fill((0, 0, 0))  # Black background

    # 2. Draw the object
    pygame.draw.rect(screen, (0, 255, 0), (x, y, 50, 50))  # Green rectangle
    pygame.draw.rect(screen, (0, 255, 0), (a, b, 50, 50))  # Green rectangle

    # 3. Update the display
    pygame.display.flip()

    # 4. Control the frame rate
    clock.tick(60)

pygame.quit()

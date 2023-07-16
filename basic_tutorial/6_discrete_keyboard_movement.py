import pygame

# Init Pygame
pygame.init()

# Create a display surface and set its caption
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Discret Movement')

VELOCITY = 20
dragon_image = pygame.image.load('images/dragon_right.png')
dragon_rect = dragon_image.get_rect()
dragon_rect.centerx = WINDOW_WIDTH // 2
dragon_rect.bottom = WINDOW_HEIGHT

# Main game loop
running = True

while running:

    # events which occurred
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dragon_rect.x -= VELOCITY
            elif event.key == pygame.K_RIGHT:
                dragon_rect.x += VELOCITY
            elif event.key == pygame.K_UP:
                dragon_rect.y -= VELOCITY
            elif event.key == pygame.K_DOWN:
                dragon_rect.y += VELOCITY

    display_surface.fill((0, 0, 0))
    display_surface.blit(dragon_image, dragon_rect)

    # update display
    pygame.display.update()

# End
pygame.quit()

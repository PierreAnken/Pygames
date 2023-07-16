import pygame

# Init Pygame
pygame.init()

# Create a display surface and set its caption
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Mouse Movement')

VELOCITY = 1
dragon_image = pygame.image.load('images/dragon_right.png')
dragon_rect = dragon_image.get_rect()
dragon_rect.center = 25, 25
destination = 25, 25

# Main game loop
running = True

while running:

    # events which occurred
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            destination = event.pos

    # Move towards destination
    if dragon_rect.centerx < destination[0]:
        dragon_rect.centerx += VELOCITY
    elif dragon_rect.centerx > destination[0]:
        dragon_rect.centerx -= VELOCITY

    if dragon_rect.centery < destination[1]:
        dragon_rect.centery += VELOCITY
    elif dragon_rect.centery > destination[1]:
        dragon_rect.centery -= VELOCITY

    display_surface.fill((0, 0, 0))
    display_surface.blit(dragon_image, dragon_rect)

    # update display
    pygame.display.update()

# End
pygame.quit()

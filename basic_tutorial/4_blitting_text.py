import pygame

# Init Pygame
pygame.init()

# Create a display surface and set its caption
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Blitting texts')

GREEN = 0, 255, 0
DARKGREEN = 10, 50, 10
BLACK = 0, 0, 0

custom_font = pygame.font.Font('fonts/AttackGraffiti.ttf', 32)

system_text = custom_font.render('Dragon Rule!', True, GREEN, DARKGREEN)
system_text_rect = system_text.get_rect()
system_text_rect.center = WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2

custom_text = custom_font.render('Move the dragon soon!', True, GREEN)
custom_text_rect = custom_text.get_rect()
custom_text_rect.center = WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 100

# Main game loop
running = True

while running:

    # events which occurred
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.blit(system_text, system_text_rect)
    display_surface.blit(custom_text, custom_text_rect)

    # update display
    pygame.display.update()

# End
pygame.quit()

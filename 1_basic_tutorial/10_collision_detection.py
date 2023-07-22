import pygame
import random

# Init Pygame
pygame.init()

# Create a display surface and set its caption
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Collision Detection')

FPS = 60
clock = pygame.time.Clock()

VELOCITY = 5
dragon_image = pygame.image.load('images/dragon_right.png')
dragon_rect = dragon_image.get_rect()
dragon_rect.center = 25, 25

coin_image = pygame.image.load('images/coin.png')
coin_rect = coin_image.get_rect()
coin_rect.center = WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2

# Main game loop
running = True

while running:

    # events which occurred
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys currently pressed down
    keys = pygame.key.get_pressed()

    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and dragon_rect.left > 0:
        dragon_rect.x -= VELOCITY
    elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and dragon_rect.right < WINDOW_WIDTH:
        dragon_rect.x += VELOCITY
    elif (keys[pygame.K_UP] or keys[pygame.K_w]) and dragon_rect.top > 0:
        dragon_rect.y -= VELOCITY
    elif (keys[pygame.K_DOWN] or keys[pygame.K_s]) and dragon_rect.bottom < WINDOW_HEIGHT:
        dragon_rect.y += VELOCITY

    display_surface.fill((0, 0, 0))

    # Check for collisions
    if dragon_rect.colliderect(coin_rect):
        coin_rect.left = random.randint(0,WINDOW_WIDTH-coin_rect.width)
        coin_rect.top = random.randint(0,WINDOW_HEIGHT-coin_rect.height)

    # Draw rects of objects
    pygame.draw.rect(display_surface, (0, 255, 0), dragon_rect, 1)
    pygame.draw.rect(display_surface, (255, 255, 0), coin_rect, 1)

    display_surface.blit(dragon_image, dragon_rect)
    display_surface.blit(coin_image, coin_rect)

    # update display
    pygame.display.update()
    clock.tick(FPS)

# End
pygame.quit()

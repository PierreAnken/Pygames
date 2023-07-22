import pygame

# Init Pygame
pygame.init()

# Create a display surface and set its caption
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Adding Sounds')

sound_1 = pygame.mixer.Sound('sounds/sound_1.wav')
sound_2 = pygame.mixer.Sound('sounds/sound_2.wav')
sound_2.set_volume(0.1)

sound_1.play()
pygame.time.delay(2000)
sound_2.play()
pygame.time.delay(2000)

pygame.mixer.music.load('sounds/music.wav')
pygame.mixer.music.play(-1, 0.0)
pygame.time.delay(5000)
pygame.mixer.music.stop()

# Main game loop
running = True

while running:

    # events which occurred
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# End
pygame.quit()

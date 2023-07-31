import pygame

pygame.init()

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 400
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Feed the Dragon')

FPS = 60
clock = pygame.time.Clock()

PLAYER_STARTING_LIVES = 5
PLAYER_VELOCITY = 5
COIN_STARTING_VELOCITY = 5
COIN_ACCELERATION = .5
BUFFER_DISTANCE = 500

score = 0
player_lives = PLAYER_STARTING_LIVES
coin_velocity = COIN_STARTING_VELOCITY

GREEN = 0, 255, 0
DARKGREEN = 10, 50, 10
WHITE = 255, 255, 255
BLACK = 0, 0, 0

font = pygame.font.Font('fonts/AttackGraffiti.ttf', 32)

score_text = font.render(f"Score: {score}", True, GREEN, DARKGREEN)
score_rect = score_text.get_rect()
score_rect.topleft = 10, 10

title_text = font.render("Feed the Dragon", True, GREEN, WHITE)
title_rect = title_text.get_rect()
title_rect.centerx = WINDOW_WIDTH // 2
title_rect.y = WINDOW_HEIGHT // 2

lives_test = font.render(f"Lives: {player_lives}", True, GREEN, DARKGREEN)
lives_rect = lives_test.get_rect()
lives_rect.topright = WINDOW_WIDTH - 10, 10

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

import pygame
import sys
import settings
from level import Level
from game_data import level_0

# INI PYGAME
pygame.init()
screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
clock = pygame.time.Clock()
# level = Level(settings.level_map, screen)
level = Level(level_0, screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')
    level.run()

    pygame.display.update()
    clock.tick(settings.fps)

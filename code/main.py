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
pygame.display.set_caption('Super Mario World v.02')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('white')
    level.run()

    pygame.display.update()
    clock.tick(settings.fps)

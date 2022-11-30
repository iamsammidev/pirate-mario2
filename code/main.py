import pygame
import sys
import settings
from level import Level
from not_need import level_0
from overworld import Overworld


class Game:
    def __init__(self):
        self.max_level = 2
        self.overworld = Overworld(1, self.max_level, screen)

    def run(self):
        self.overworld.run()


pygame.init()
screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
clock = pygame.time.Clock()
game = Game()
level = Level(level_0, screen)
pygame.display.set_caption('Super Mario World v.02')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')
    game.run()
    pygame.display.update()
    clock.tick(settings.fps)

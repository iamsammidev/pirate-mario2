import pygame
from game_data import levels

class Node(pygame.sprite.Sprite):
    def __init__(self, pos, status):
        super().__init__()
        self.image = pygame.Surface((100, 80))
        if status == 'available':
            self.image.fill('red')
        else:
            self.image.fill('grey')
        self.rect = self.image.get_rect(center=pos)

class Icon(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill('blue')
        self.rect = self.image.get_rect(center=pos)

class Overworld:
    def __init__(self, start_level, max_level, surface):

        # setup
        self.display_surface = surface
        self.max_level = max_level
        self.current_level = start_level

        # sprites
        self.setup_nodes()
        self.setup_icon()

    def setup_nodes(self):
        self.nodes = pygame.sprite.Group()

        for index, node_data in enumerate(levels.values()):
            if index <= self.max_level:
                node_sprites = Node(node_data['node_pos'], 'available')
            else:
                node_sprites = Node(node_data['node_pos'], 'locked')
            self.nodes.add(node_sprites)

    def draw_paths(self):
        points = [node['node_pos'] for index, node in enumerate(levels.values()) if index <= self.max_level]
        pygame.draw.lines(self.display_surface, 'red', False, points, 6)

    def setup_icon(self):
        self.icon = pygame.sprite.GroupSingle()
        icon_sprites = Icon(self.nodes.sprites()[self.current_level].rect.center)
        self.icon.add(icon_sprites)

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] and self.current_level < self.max_level:
            self.move_direction = self.get_movement_data()
            self.current_level += 1
        elif keys[pygame.K_LEFT] and self.current_level > 0:
            self.current_level -= 1

    def update_icon_pos(self):
        pass

    def run(self):
        self.input()
        self.update_icon_pos()
        self.draw_paths()
        self.nodes.draw(self.display_surface)
        self.icon.draw(self.display_surface)

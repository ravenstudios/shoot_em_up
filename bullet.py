from constants import *
import pygame
import player
class Bullet:
    def __init__(self):
        self.y = GAME_HEIGHT - BLOCK_SIZE
        self.x = GAME_WIDTH // 2
        self.width = BLOCK_SIZE
        self.height = BLOCK_SIZE
        self.speed = 5
        self.color = YELLOW
        self.count = 0
        self.color_index = [RED, GREEN, BLUE, (127, 255, 0), (255, 255, 255)]
        self.score = 0
        self.hit_box = pygame.Rect(self.y, self.x, self.width, self.height)

    def update(self):
        self.key_input()
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

    def key_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            self.y -= self.speed

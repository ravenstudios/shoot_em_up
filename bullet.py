from constants import *
import pygame


class Bullet:
    def __init__(self, x, y):
        self.y = x
        self.x = y
        self.width = BLOCK_SIZE // 4
        self.height = BLOCK_SIZE
        self.speed = 5
        self.color = YELLOW
        self.hit_box = pygame.Rect(self.y, self.x, self.width, self.height)
        self.can_delete = False



    def update(self):
        self.hit_box = self.hit_box.move(0, -self.speed)
        if self.hit_box.y + self.hit_box.height  < 0:
            self.can_delete = True

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.hit_box)

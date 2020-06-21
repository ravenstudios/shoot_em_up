import pygame
from constants import *
class Enemy_master():

    def __init__(self, pattern):

        self.width = BLOCK_SIZE
        self.height = BLOCK_SIZE

        self.x_speed = 10
        self.y_speed = 10

        self.nodes = pattern
        self.x = self.nodes[0][0]
        self.y = self.nodes[0][1]

        self.hit_box = pygame.Rect(self.x, self.y, self.width, self.height)

        self.node_index = 0
        self.next_pos = self.nodes[0]

    def update(self):
        self.pattern()

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.hit_box)

    def pattern(self):
        #if the enemy is at next_pos move to next node
        x_range = range(self.next_pos[0] - self.x_speed, self.next_pos[0] + self.x_speed)
        y_range = range(self.next_pos[1] - self.y_speed, self.next_pos[1] + self.y_speed)

        if self.hit_box.x in x_range and self.hit_box.y in y_range and self.node_index < len(self.nodes) - 1:

            self.node_index += 1
            self.next_pos = self.nodes[self.node_index]

        #x <
        if self.hit_box.x <= self.next_pos[0]:
            self.hit_box = self.hit_box.move(self.x_speed, 0)
        #x >
        if self.hit_box.x >= self.next_pos[0]:
            self.hit_box = self.hit_box.move(-self.x_speed, 0)
        #y <
        if self.hit_box.y <= self.next_pos[1]:
            self.hit_box = self.hit_box.move(0, self.y_speed)
        #y >
        if self.hit_box.y >= self.next_pos[1]:
            self.hit_box = self.hit_box.move(0, -self.y_speed)

from constants import *
import pygame
import random

class Star():
    def __init__(self):
        self.min_size = BLOCK_SIZE // 20
        self.max_size = BLOCK_SIZE // 10
        self.size = random.randint(self.min_size, self.max_size)
        self.x = random.randint(0, GAME_WIDTH - self.size)
        self.y = random.randint(0, GAME_HEIGHT - self.size)

        self.speed = self.size * 2

    def update(self):
        self.y += self.speed
        if self.y > GAME_HEIGHT:
            self.reset()

    def draw(self, surface):
        pygame.draw.circle(surface, WHITE, (self.x, self.y), self.size)


    def reset(self):
        self.min_size = BLOCK_SIZE // 20
        self.max_size = BLOCK_SIZE // 10
        self.size = random.randint(self.min_size, self.max_size)
        self.x = random.randint(0, GAME_WIDTH - self.size)
        self.y = random.randint(-(GAME_HEIGHT - self.size), 0)

        self.speed = self.size * 2



class Star_Manager():
    def __init__(self):
        self.stars = []
        self.num_of_stars = 40

        for i in range(self.num_of_stars):
            self.stars.append(Star())


    def update(self):
        for star in self.stars:
            star.update()


    def draw(self, surface):
        for star in self.stars:
            star.draw(surface)

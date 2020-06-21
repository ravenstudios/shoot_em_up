import pygame
from constants import *
import bullet

class Bullet_manager():

    def __init__(self):
        self.bullets = []
        self.fire_rate = 250
        self.now = pygame.time.get_ticks()
        self.last_shot = 0

    def update(self, player):
        print(pygame.time.get_ticks())
        self.key_input(player)
        for b in self.bullets:
            b.update()
            if b.can_delete == True:
                self.bullets.remove(b)


    def draw(self, surface):
        for b in self.bullets:
            b.draw(surface)

    def add_bullet(self, player):
        self.bullets.append(bullet.Bullet(player.hit_box.x, player.hit_box.y))

    def key_input(self, player):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:

            self.now = pygame.time.get_ticks()

            if self.now > self.last_shot + self.fire_rate:
                self.add_bullet(player)

                self.last_shot = self.now

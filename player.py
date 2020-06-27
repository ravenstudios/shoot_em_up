from constants import *
import pygame
class Char:
    def __init__(self):
        self.x = GAME_WIDTH // 2
        self.y = GAME_HEIGHT - BLOCK_SIZE

        self.width, self.height = BLOCK_SIZE, BLOCK_SIZE

        self.speed = 5
        self.color = GREEN

        self.hit_box = pygame.Rect(self.x, self.y, self.width, self.height)

        self.img = pygame.image.load('images/ship1.png')

        self.animation_index = 0
        self.animation_speed = 60
        self.now = pygame.time.get_ticks()
        self.last_frame = 0
        # self.img = pygame.transform.scale(self.img, (self.width, self.height))


    def update(self):
        self.key_input()

    def draw(self, surface):
        # pygame.draw.rect(surface, self.color, self.hit_box)

        surface.blit(self.get_next_frame(), self.hit_box)

        # surface.blit(self.img, self.hit_box)

    def key_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            if self.hit_box.y > 0:
                self.hit_box.y += -self.speed

        if keys[pygame.K_DOWN]:
            if self.hit_box.y < GAME_HEIGHT - self.hit_box.height:
                self.hit_box.y += self.speed


        if keys[pygame.K_LEFT]:
            if self.hit_box.x > 0:
                self.hit_box.x += -self.speed

        if keys[pygame.K_RIGHT]:
            if self.hit_box.x < GAME_WIDTH - self.hit_box.width:
                self.hit_box.x += self.speed


    def get_next_frame(self):
        image = pygame.Surface([BLOCK_SIZE, BLOCK_SIZE])
        self.now = pygame.time.get_ticks()

        if self.now > self.last_frame + self.animation_speed:
            self.animation_index += 1
            self.last_frame = self.now

        if self.animation_index > 3:
            self.animation_index = 0
        image.blit(self.img, (0, 0), (self.animation_index * BLOCK_SIZE, 0, BLOCK_SIZE, BLOCK_SIZE))
        # self.img = pygame.transform.scale(self.img, (self.width, self.height))

        return pygame.transform.scale(image, (BLOCK_SIZE * 2, BLOCK_SIZE * 2))

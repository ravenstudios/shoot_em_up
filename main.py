from constants import *
import pygame

import enemy_master

clock = pygame.time.Clock()
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))



p = [
    (0, 0),
    (400, 0),
    (400, 400),
    (0, 0),
    (0, 500),
    (300, 300),
    (800, 800)
]
em = enemy_master.Enemy_master(p)
pygame.init()


def main():
    running = True

    while running:
        clock.tick(TICK_RATE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw()
        update()

    pygame.quit()



def draw():
    surface.fill((0, 0, 0))#background

    em.draw(surface)
    pygame.display.flip()



def update():
    em.update()



if __name__ == "__main__":
    main()

from constants import *
import pygame

import enemy_master
import player
import bullet_manager
import stars

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
bm = bullet_manager.Bullet_manager()
player = player.Char()
stars = stars.Star_Manager()

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
    stars.draw(surface)
    em.draw(surface)
    player.draw(surface)
    bm.draw(surface)


    pygame.display.flip()


def update():
    em.update()
    player.update()
    bm.update(player)
    stars.update()



if __name__ == "__main__":
    main()

from constants import *
import pygame
import player
import bullet


clock = pygame.time.Clock()
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

pygame.init()

char = player.Char()
bullet = bullet.Bullet()
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
    char.draw(surface)
    bullet.draw(surface)
    pygame.display.flip()


def update():
    char.update()
    bullet.update()


if __name__ == "__main__":
    main()

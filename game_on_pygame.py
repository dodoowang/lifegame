import fire
import pygame
from pygame import draw
import sys
from time import sleep
from grid import Grid


def GameOfLife(n=10, day0=40, frames=2):
        grid = Grid(n, day0)
        timer_interval = 1.0 / frames

        pygame.init()
        screen = pygame.display.set_mode((500, 500))
        while True:
            show(screen, grid)
            pygame.display.update()
            grid.update()
            sleep(timer_interval)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)


def show(screen, grid):
    screen.fill((189, 189, 189))
    size_screen = screen.get_width()
    n = grid.size
    sz = size_screen // n
    for i in range(n + 1):
        draw.line(screen, (184, 184, 184), (0, i * sz), (n * sz, i * sz))
        draw.line(screen, (184, 184, 184), (i * sz, 0), (i * sz, n * sz))
    for i in range(1, grid.size + 1):
        for j in range(1, grid.size + 1):
            if grid.data[i][j] == 1:
                cell = (sz * (i - 1), sz * (j - 1), sz, sz)
                draw.rect(screen, (244, 152, 66), cell, 0)


if __name__ == "__main__":
    fire.Fire(GameOfLife)

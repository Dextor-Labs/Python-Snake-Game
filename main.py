# main.py

import pygame

from settings import WIDTH, HEIGHT
from game import run_game


def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")

    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 36)

    run_game(screen, clock, font)


main()

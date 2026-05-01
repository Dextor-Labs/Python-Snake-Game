# helpers

import random
import pygame

from settings import WIDTH, HEIGHT, CELL_SIZE, WHITE

def draw_text(screen, font, text, x, y):
    image = font.render(text, True, WHITE)
    screen.blit(image, (x, y))

def random_food_position():
    x = random.randrange(0, WIDTH, CELL_SIZE)
    y = random.randrange(0, HEIGHT, CELL_SIZE)
    return [x, y]

# game

# game.py

import pygame
import sys

from settings import (
    WIDTH,
    HEIGHT,
    CELL_SIZE,
    BLACK,
    GREEN,
    DARK_GREEN,
    RED,
    FPS,
)

from helpers import draw_text, random_food_position


def game_over_screen(screen, font, score):
    screen.fill(BLACK)

    draw_text(screen, font, "Game Over!", 220, 140)
    draw_text(screen, font, f"Score: {score}", 245, 180)
    draw_text(screen, font, "Press R to restart or Q to quit", 120, 230)

    pygame.display.update()


def run_game(screen, clock, font):
    snake = [[100, 100], [80, 100], [60, 100]]
    direction = "RIGHT"
    next_direction = "RIGHT"

    food = random_food_position()
    score = 0

    while True:
        # --------------------
        # Events / controls
        # --------------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != "DOWN":
                    next_direction = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    next_direction = "DOWN"
                elif event.key == pygame.K_LEFT and direction != "RIGHT":
                    next_direction = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    next_direction = "RIGHT"

        direction = next_direction

        # --------------------
        # Move snake
        # --------------------
        head_x, head_y = snake[0]

        if direction == "UP":
            head_y -= CELL_SIZE
        elif direction == "DOWN":
            head_y += CELL_SIZE
        elif direction == "LEFT":
            head_x -= CELL_SIZE
        elif direction == "RIGHT":
            head_x += CELL_SIZE

        new_head = [head_x, head_y]
        snake.insert(0, new_head)

        # --------------------
        # Eat food
        # --------------------
        if new_head == food:
            score += 1
            food = random_food_position()
        else:
            snake.pop()

        # --------------------
        # Check collisions
        # --------------------
        hit_wall = (
            head_x < 0
            or head_x >= WIDTH
            or head_y < 0
            or head_y >= HEIGHT
        )

        hit_self = new_head in snake[1:]

        if hit_wall or hit_self:
            game_over_screen(screen, font, score)

            waiting = True

            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:
                            return run_game(screen, clock, font)
                        elif event.key == pygame.K_q:
                            pygame.quit()
                            sys.exit()

        # --------------------
        # Draw everything
        # --------------------
        screen.fill(BLACK)

        pygame.draw.rect(
            screen,
            RED,
            pygame.Rect(food[0], food[1], CELL_SIZE, CELL_SIZE),
        )

        for index, body_part in enumerate(snake):
            colour = GREEN if index == 0 else DARK_GREEN

            pygame.draw.rect(
                screen,
                colour,
                pygame.Rect(
                    body_part[0],
                    body_part[1],
                    CELL_SIZE,
                    CELL_SIZE,
                ),
            )

        draw_text(screen, font, f"Score: {score}", 10, 10)

        pygame.display.update()

        clock.tick(FPS)



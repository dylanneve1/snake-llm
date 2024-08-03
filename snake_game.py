import pygame
import time
import random

# Initialize the game
pygame.init()

# Set colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set display dimensions
WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Game settings
SNAKE_BLOCK = 10
SNAKE_SPEED = 15

# Initialize the clock
clock = pygame.time.Clock()

# Function to draw the snake
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, GREEN, [x[0], x[1], snake_block, snake_block])

# Game over function
def display_message(msg):
    font_style = pygame.font.SysFont(None, 50)
    mesg = font_style.render(msg, True, RED)
    screen.blit(mesg, [WIDTH / 6, HEIGHT / 3])

# Main game loop
def game_loop():
    running = True
    x1 = WIDTH / 2
    x1_change = 0
    y1 = HEIGHT / 2
    y1_change = 0
    snake_list = []
    snake_length = 1
    score = 0
    foodx = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
    foody = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -SNAKE_BLOCK
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = SNAKE_BLOCK
                    x1_change = 0

        x1 += x1_change
        y1 += y1_change
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, [x1, y1, SNAKE_BLOCK, SNAKE_BLOCK])
        pygame.draw.rect(screen, RED, [foodx, foody, SNAKE_BLOCK, SNAKE_BLOCK])

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
            foody = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0
            snake_length += 1
            score += 1

        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            running = False

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        draw_snake(SNAKE_BLOCK, snake_list)
        font_style = pygame.font.SysFont(None, 35)
        score_display = font_style.render(f'Score: {score}', True, WHITE)
        screen.blit(score_display, [0, 0])
        pygame.display.update()
        clock.tick(SNAKE_SPEED)

    # Game over message
    display_message('Game Over! Press C to Play Again or Q to Quit')
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_c:
                    game_loop()
                    break

# Start the game loop
if __name__ == '__main__':
    game_loop()
pygame.quit()
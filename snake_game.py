
import pygame
import time
import random

# Initialize the game
pygame.init()

# Set colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

# Set display dimensions
width = 600
height = 400
screen = pygame.display.set_mode((width, height))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(black)
    pygame.display.update()

pygame.quit()

# Game settings
snake_block = 10
snake_speed = 15

# Initialize the clock
clock = pygame.time.Clock()

# Function to draw the snake
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, green, [x[0], x[1], snake_block, snake_block])

# Main game loop
snake_list = []
snake_length = 1
x1 = width / 2
y1 = height / 2
x1_change = 0
y1_change = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -snake_block
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = snake_block
                x1_change = 0

    x1 += x1_change
    y1 += y1_change
    screen.fill(black)
    pygame.draw.rect(screen, white, [x1, y1, snake_block, snake_block])
    pygame.display.update()
    clock.tick(snake_speed)

# Food generation
foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

# Main game loop (continued)
while running:
    # ... (previous code)
    pygame.draw.rect(screen, red, [foodx, foody, snake_block, snake_block])

    # Check for collision with food
    if x1 == foodx and y1 == foody:
        foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
        snake_length += 1

    # Update the snake's length
    snake_head = []
    snake_head.append(x1)
    snake_head.append(y1)
    snake_list.append(snake_head)
    if len(snake_list) > snake_length:
        del snake_list[0]

    our_snake(snake_block, snake_list)
    pygame.display.update()

# Collision detection
if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
    running = False

# Check for collision with itself
for x in snake_list[:-1]:
    if x == snake_head:
        running = False

# End the game
pygame.quit()

# Game over function
def message(msg):
    font_style = pygame.font.SysFont(None, 50)
    mesg = font_style.render(msg, True, red)
    screen.blit(mesg, [width / 6, height / 3])

# Main game loop (continued)
while running:
    # ... (previous code)
    if not running:
        message('Game Over! Press C to Play Again or Q to Quit')
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()
                    if event.key == pygame.K_c:
                        # Restart the game logic here
                        running = True
                        break

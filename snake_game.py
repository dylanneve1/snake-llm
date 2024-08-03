import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with black color
    screen.fill((0, 0, 0))

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()

# Define game constants and variables
screen_width = 800
screen_height = 600
snake_color = (0, 255, 0)
food_color = (255, 0, 0)
background_color = (0, 0, 0)
snake_speed = 15

# Initialize variables for the snake's position, direction, and length
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_direction = 'RIGHT'
change_to = snake_direction

# Initialize variables for the food's position
food_pos = [random.randrange(1, (screen_width//10)) * 10, random.randrange(1, (screen_height//10)) * 10]
food_spawn = True

# Set the game clock
clock = pygame.time.Clock()

# Function to draw the snake on the screen
def draw_snake(snake_body):
    for pos in snake_body:
        pygame.draw.rect(screen, snake_color, pygame.Rect(pos[0], pos[1], 10, 10))

# Function to draw the food on the screen
def draw_food(food_pos):
    pygame.draw.rect(screen, food_color, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

# Function to randomly place the food on the screen
def place_food():
    return [random.randrange(1, (screen_width//10)) * 10, random.randrange(1, (screen_height//10)) * 10]

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

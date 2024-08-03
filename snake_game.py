
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

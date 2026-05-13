import pygame
import sys
from game import SnakeGame

# Initialize Pygame
pygame.init()


# variables:
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
CELL_SIZE = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)


def draw_grid():
    """Draw grid lines to visualize the 10x10 board"""
    for x in range(0, WINDOW_WIDTH, CELL_SIZE):
        pygame.draw.line(screen, GRAY, (x, 0), (x, WINDOW_HEIGHT))
    for y in range(0, WINDOW_HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, GRAY, (0, y), (WINDOW_WIDTH, y))

def draw_cell(row, col, color):
    """Draw a colored cell at the specified grid position"""
    x = col * CELL_SIZE
    y = row * CELL_SIZE
    pygame.draw.rect(screen, color, (x, y, CELL_SIZE, CELL_SIZE))
    # Draw border around cell (optional, for better visibility)
    pygame.draw.rect(screen, BLACK, (x, y, CELL_SIZE, CELL_SIZE), 1)

# Set up the display window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("RL snake")

# Game loop control variable
running = True


game = SnakeGame(10, 10)




# Main game loop
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_LEFT:
                game.update_game([1,0,0])
            elif event.key == pygame.K_UP:
                game.update_game([0,1,0])
            elif event.key == pygame.K_RIGHT:
                game.update_game([0,0,1])

    # Fill the screen with a color (RGB: 0-255)
    screen.fill((0, 0, 0))  # Black background


    # drawing the snake body:
    for i in range(10):
        for j in range(10):
            if game.snake_body[i][j] == 1:
                draw_cell(i, j, BLUE)


    # drawing the snake head:
    for i in range(10):
        for j in range(10):
            if game.head[i][j] == 1:
                draw_cell(i, j, BLUE)


    # drawing the food:
    for i in range(10):
        for j in range(10):
            if game.food[i][j] == 1:
                draw_cell(i, j, RED)


    # Update the display
    draw_grid()  # Overlay grid lines
    pygame.display.flip()

# Clean up and exit
pygame.quit()
sys.exit()


import pygame
import random
import time
import sys

# Initialize Pygame
pygame.init()

# Set the size of the game window
window_width = 800
window_height = 600
game_window = pygame.display.set_mode((window_width, window_height))

# Set the title of the window
pygame.display.set_caption('Snake Game')

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Snake properties
snake_size = 10
snake_speed = 15
snake_segments = []
snake_length = 1

# Initial snake position
snake_x = window_width / 2
snake_y = window_height / 2
snake_x_change = 0
snake_y_change = 0

# Food initial position
food_x = round(random.randrange(0, window_width - snake_size) / 10.0) * 10.0
food_y = round(random.randrange(0, window_height - snake_size) / 10.0) * 10.0

# Score
score = 0

# Clock to control the game's frame rate
clock = pygame.time.Clock()

# Function to display the score
def show_score():
    font = pygame.font.SysFont(None, 35)
    score_text = font.render("Score: " + str(score), True, white)
    game_window.blit(score_text, [0, 0])

# Function to show game over message
def game_over_message():
    font = pygame.font.SysFont('times new roman', 50)
    game_over_text = font.render("Game Over", True, white)
    final_score_text = font.render("Final Score: " + str(score), True, white)
    game_window.fill(black)
    game_window.blit(game_over_text, [window_width / 4, window_height / 3])
    game_window.blit(final_score_text, [window_width / 4, window_height / 2])
    pygame.display.update()
    time.sleep(3)
    pygame.quit()
    sys.exit()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake_x_change == 0:
                snake_x_change = -snake_size
                snake_y_change = 0
            elif event.key == pygame.K_RIGHT and snake_x_change == 0:
                snake_x_change = snake_size
                snake_y_change = 0
            elif event.key == pygame.K_UP and snake_y_change == 0:
                snake_y_change = -snake_size
                snake_x_change = 0
            elif event.key == pygame.K_DOWN and snake_y_change == 0:
                snake_y_change = snake_size
                snake_x_change = 0

    # Update snake position
    snake_x += snake_x_change
    snake_y += snake_y_change

    # Snake growth
    snake_head = [snake_x, snake_y]
    snake_segments.append(snake_head)
    if len(snake_segments) > snake_length:
        del snake_segments[0]

    # Collision with boundaries
    if snake_x >= window_width or snake_x < 0 or snake_y >= window_height or snake_y < 0:
        game_over_message()

    # Collision with self
    for segment in snake_segments[:-1]:
        if segment == snake_head:
            game_over_message()

    # Eat food
    if snake_x == food_x and snake_y == food_y:
        score += 1
        snake_length += 1
        food_x = round(random.randrange(0, window_width - snake_size) / 10.0) * 10.0
        food_y = round(random.randrange(0, window_height - snake_size) / 10.0) * 10.0

    # Fill the background
    game_window.fill(black)

    # Draw the food
    pygame.draw.rect(game_window, white, [food_x, food_y, snake_size, snake_size])

    # Draw the snake
    for segment in snake_segments:
        pygame.draw.rect(game_window, white, [segment[0], segment[1], snake_size, snake_size])

    # Display the score
    show_score()

    # Update the display
    pygame.display.update()

    # Control the frame rate
    clock.tick(snake_speed)

# Quit the game
pygame.quit()

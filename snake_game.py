#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pygame
import random

# Initialize Pygame
pygame.init()
pygame.mixer.init()  # Initialize the mixer module


# Constants
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Font
font = pygame.font.Font(None, 36)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

lives = 3
heart_emoji = "❤️"

# Display lives left
lives_text = font.render("Lives: " + heart_emoji * lives, True, WHITE)
screen.blit(lives_text, (10, 130))

# Load the eating sound effect
eating_sound = pygame.mixer.Sound("https://github.com/Saumyadeepm/The-Snake-Game-Using-Pygame-Lib/raw/main/sounds/food_eating.mp3")
# Load the game over sound effect
game_over_sound = pygame.mixer.Sound("https://github.com/Saumyadeepm/The-Snake-Game-Using-Pygame-Lib/raw/main/sounds/game_over.mp3")


# Initialize Snake and food
snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

# Initial direction
direction = (1, 0)

# Difficulty levels
DIFFICULTY_LEVELS = {
    "Normal": 150,
    "Medium": 100,
    "Epic": 50,
}
current_difficulty = None

# Snake colors
SNAKE_COLORS = {
    "Green": GREEN,
    "Red": (255, 0, 0),
    "Blue": (0, 0, 255),
    "Yellow": (255, 255, 0),
}
current_snake_color = None

# Font
font = pygame.font.Font(None, 36)

# Player's name input box
player_name = ""

# Game over flag
game_over = False

# Text input box
text_input_rect = pygame.Rect(250, 300, 300, 40)
text_input_color = WHITE
text_input_active = False
text_input_font = pygame.font.Font(None, 36)
text_input_text = ""

# Function to draw the text input box
def draw_text_input_box():
    pygame.draw.rect(screen, text_input_color, text_input_rect, 2)
    text_surface = text_input_font.render(text_input_text, True, text_input_color)
    screen.blit(text_surface, (text_input_rect.x + 5, text_input_rect.y + 5))

# Difficulty selection loop
difficulty_selected = False
while not difficulty_selected:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                current_difficulty = "Normal"
                difficulty_selected = True
            elif event.key == pygame.K_m:
                current_difficulty = "Medium"
                difficulty_selected = True
            elif event.key == pygame.K_e:
                current_difficulty = "Epic"
                difficulty_selected = True

    # Display difficulty selection text centered
    screen.fill(BLACK)
    difficulty_text = font.render("Select Difficulty (N: Normal, M: Medium, E: Epic)", True, WHITE)
    text_rect = difficulty_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(difficulty_text, text_rect)
    pygame.display.flip()

# Snake color selection loop
color_selected = False
while not color_selected:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_g:
                current_snake_color = "Green"
                color_selected = True
            elif event.key == pygame.K_r:
                current_snake_color = "Red"
                color_selected = True
            elif event.key == pygame.K_b:
                current_snake_color = "Blue"
                color_selected = True
            elif event.key == pygame.K_y:
                current_snake_color = "Yellow"
                color_selected = True

    # Display color selection text centered
    screen.fill(BLACK)
    color_text = font.render("Select Snake Color (G: Green, R: Red, B: Blue, Y: Yellow)", True, WHITE)
    text_rect = color_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(color_text, text_rect)
    pygame.display.flip()

# Player's name input loop
name_input_selected = False
while not name_input_selected:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if text_input_rect.collidepoint(event.pos):
                text_input_active = not text_input_active
            else:
                text_input_active = False
            text_input_color = WHITE if text_input_active else BLACK
        if event.type == pygame.KEYDOWN:
            if text_input_active:
                if event.key == pygame.K_RETURN:
                    name_input_selected = True
                    player_name = text_input_text
                    text_input_text = ""
                elif event.key == pygame.K_BACKSPACE:
                    text_input_text = text_input_text[:-1]
                else:
                    text_input_text += event.unicode

    screen.fill(BLACK)
    draw_text_input_box()
    name_prompt = font.render("Enter Your Name and Press Enter:", True, WHITE)
    screen.blit(name_prompt, (200, 250))
    pygame.display.flip()

# Game variables after difficulty, color, and name selection
score = 0

# Reset the game
snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
direction = (1, 0)
score = 0
game_over = False
lives = 3  # Reset the number of lives


# Load a welcome image
#welcome_image = pygame.image.load("we)  # Replace with the path to your welcome image
#welcome_image = pygame.transform.scale(welcome_image, (WIDTH, HEIGHT))

# Welcome text
welcome_font = pygame.font.Font(None, 72)
welcome_text = welcome_font.render("Welcome to Snake Game", True, WHITE)

# Show welcome screen
show_welcome = True


# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if not game_over:
                if event.key == pygame.K_UP and direction != (0, 1):
                    direction = (0, -1)
                elif event.key == pygame.K_DOWN and direction != (0, -1):
                    direction = (0, 1)
                elif event.key == pygame.K_LEFT and direction != (1, 0):
                    direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                    direction = (1, 0)
            else:
                if event.key == pygame.K_SPACE:
                    # Reset the game
                    snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
                    food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
                    direction = (1, 0)
                    score = 0
                    game_over = False

    if not game_over:
        # Update Snake position
        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

        # Wrap around the edges
        new_head = (new_head[0] % GRID_WIDTH, new_head[1] % GRID_HEIGHT)

        snake.insert(0, new_head)

        # Check for collision with food
        if snake[0] == food:
            score += 10
            eating_sound.play()  # Play the eating sound
            food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        else:
            snake.pop()  # Remove the tail segment to maintain the same length

        # Check for collision with itself
        if snake[0] in snake[1:]:
            lives -= 1
            if lives == 0:
                game_over = True
                game_over_sound.play()  # Play the game over sound

        # Clear the screen
        screen.fill(BLACK)

        # Draw Snake
        for segment in snake:
            pygame.draw.rect(screen, SNAKE_COLORS[current_snake_color], (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

        # Draw food
        pygame.draw.rect(screen, WHITE, (food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

        # Display score
        score_text = font.render("Score: " + str(score), True, WHITE)
        screen.blit(score_text, (10, 10))

        # Display current difficulty
        difficulty_text = font.render("Difficulty: " + current_difficulty, True, WHITE)
        screen.blit(difficulty_text, (10, 40))

        # Display current snake color
        color_text = font.render("Snake Color: " + current_snake_color, True, WHITE)
        screen.blit(color_text, (10, 70))

        # Display player's name
        name_text = font.render("Player: " + player_name, True, WHITE)
        screen.blit(name_text, (10, 100))

        # Display lives left
        lives_text = font.render("Lives: " + heart_emoji * lives, True, WHITE)
        screen.blit(lives_text, (10, 130))

        # Update the display
        pygame.display.flip()

        # Control the game speed based on difficulty
        pygame.time.delay(DIFFICULTY_LEVELS[current_difficulty])
    else:
        # Display game over text
        game_over_text = font.render("Game Over! Press SPACE to play again.", True, WHITE)
        screen.blit(game_over_text, (50, HEIGHT // 2 - 18))

        # Display final score
        final_score_text = font.render("Final Score: " + str(score), True, WHITE)
        screen.blit(final_score_text, (50, HEIGHT // 2 + 18))

        # Display difficulty and color change instructions
        change_instructions_text = font.render("Change Difficulty (N: Normal, M: Medium, E: Epic)", True, WHITE)
        screen.blit(change_instructions_text, (50, HEIGHT // 2 + 72))
        color_change_instructions_text = font.render("Change Snake Color (G: Green, R: Red, B: Blue, Y: Yellow)", True, WHITE)
        screen.blit(color_change_instructions_text, (50, HEIGHT // 2 + 102))

        # Update the display
        pygame.display.flip()

# Quit Pygame
pygame.quit()


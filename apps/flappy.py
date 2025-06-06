import pygame
import random

# Initialize pygame
pygame.init()

# Define constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
BIRD_WIDTH = 50
BIRD_HEIGHT = 50
OBSTACLE_WIDTH = 60
OBSTACLE_HEIGHT = random.randint(150, 400)
OBSTACLE_GAP = 150
GRAVITY = 0.5
FLAP_STRENGTH = -7
GAME_SPEED = 3
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BIRD_COLOR = (255, 255, 0)
OBSTACLE_COLOR = (0, 255, 0)
BUTTON_COLOR = (0, 0, 255)
BUTTON_HOVER_COLOR = (0, 0, 200)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Load font for score and buttons
font = pygame.font.SysFont("Arial", 30)

# Bird class
class Bird:
    def __init__(self):
        self.x = 100
        self.y = SCREEN_HEIGHT // 2
        self.velocity = 0

    def flap(self):
        self.velocity = FLAP_STRENGTH

    def move(self):
        self.velocity += GRAVITY
        self.y += self.velocity

    def draw(self):
        pygame.draw.rect(screen, BIRD_COLOR, (self.x, self.y, BIRD_WIDTH, BIRD_HEIGHT))

# Obstacle class
class Obstacle:
    def __init__(self):
        self.x = SCREEN_WIDTH
        self.height = random.randint(150, 400)
        self.y = self.height - OBSTACLE_HEIGHT
        self.passed = False

    def move(self):
        self.x -= GAME_SPEED

    def draw(self):
        pygame.draw.rect(screen, OBSTACLE_COLOR, (self.x, 0, OBSTACLE_WIDTH, self.height))
        pygame.draw.rect(screen, OBSTACLE_COLOR, (self.x, self.height + OBSTACLE_GAP, OBSTACLE_WIDTH, SCREEN_HEIGHT))

# Function to display the score
def display_score(score):
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 4))

# Function to display a button
def draw_button(text, x, y, width, height, hover=False):
    button_color = BUTTON_HOVER_COLOR if hover else BUTTON_COLOR
    pygame.draw.rect(screen, button_color, (x, y, width, height))
    label = font.render(text, True, WHITE)
    screen.blit(label, (x + (width - label.get_width()) // 2, y + (height - label.get_height()) // 2))

# Main game loop
def game():
    bird = Bird()
    obstacles = [Obstacle()]
    clock = pygame.time.Clock()
    score = 0
    running = True
    game_over = False

    while running:
        screen.fill(WHITE)

        if not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:  # Flap on touch
                    bird.flap()

            bird.move()

            # Create new obstacles
            if obstacles[-1].x < SCREEN_WIDTH - 200:
                obstacles.append(Obstacle())

            # Move and draw obstacles
            for obstacle in obstacles:
                obstacle.move()
                obstacle.draw()

                # Check for collision with obstacles
                if bird.x + BIRD_WIDTH > obstacle.x and bird.x < obstacle.x + OBSTACLE_WIDTH:
                    if bird.y < obstacle.height or bird.y + BIRD_HEIGHT > obstacle.height + OBSTACLE_GAP:
                        game_over = True

                # Check if the bird passes an obstacle
                if obstacle.x + OBSTACLE_WIDTH < bird.x and not obstacle.passed:
                    obstacle.passed = True
                    score += 1

            # Remove obstacles that are off-screen
            if obstacles[0].x + OBSTACLE_WIDTH < 0:
                obstacles.pop(0)

            # Draw the bird
            bird.draw()

            # Check if bird hits the ground
            if bird.y + BIRD_HEIGHT > SCREEN_HEIGHT:
                game_over = True

        else:
            # Display game over screen and score
            display_score(score)

            # Draw Retry and Quit buttons
            mouse_x, mouse_y = pygame.mouse.get_pos()
            retry_button_hover = 200 <= mouse_x <= 300 and 400 <= mouse_y <= 450
            quit_button_hover = 100 <= mouse_x <= 300 and 500 <= mouse_y <= 550

            draw_button("Retry", 200, 400, 100, 50, retry_button_hover)
            draw_button("Quit", 100, 500, 200, 50, quit_button_hover)

            # Check button clicks
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if retry_button_hover:
                        running = True
                       	game()  # Restart the game
                    elif quit_button_hover:
                        running = False  # Quit the game

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

# Run the game
game()

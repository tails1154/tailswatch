import pygame
import sys
import pytz #import 
import subprocess
from datetime import datetime
import subprocess
import os

# Firmware Update Function
def run_firmware_update():
    try:
        # Run the firmware update script
        subprocess.run(['bash', 'fwupdate.sh'], check=True)

        # Restart the firmware after update
        python_exec = sys.executable
        firmware_script = os.path.abspath(__file__)
        # Exit the current process and start the updated firmware
        os.execv(python_exec, [python_exec, firmware_script])

    except subprocess.CalledProcessError:
        print("Firmware update failed.")
        # Optionally display an error message on the screen here

# Initialize Pygame
pygame.init()

# Screen Setup
WIDTH, HEIGHT = 480, 480  # Adjust for TailsWatch display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TailsWatch Firmware")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
TAILS_BLUE = (70, 130, 180)
STATIC_BLUE = (173, 216, 230)  # Light blue for static background
SLIDE_COLOR = (30, 30, 30)

# Fonts
font = pygame.font.SysFont("Arial", 18)
big_font = pygame.font.SysFont("Arial", 24)

# Time Zone Setup (America/Chicago)
timezone = pytz.timezone('America/Chicago')

# Get current time in 12-hour format
def get_time():
    now = datetime.now(timezone)
    return now.strftime("%I:%M:%S %p")

# Run Firmware Update Bash Script and Exit
# def run_firmware_update():
#     try:
#         subprocess.run(["bash", "fwupdate.sh"], check=True)
#     except subprocess.CalledProcessError as e:
#         print(f"Error running firmware update: {e}")
#     sys.exit()  # Stop the Python process

# Intro Static Background Function
def intro_static_background():
    screen.fill(STATIC_BLUE)
    title = big_font.render("Tails1154", True, WHITE)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 2))
    pygame.display.update()

    # Display for 3 seconds or skip with key press
    start_time = pygame.time.get_ticks()
    while pygame.time.get_ticks() - start_time < 3000:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                return

# Sliding Menu Function (Non-looping, stays open until closed)
def slide_menu(opening=True):
    menu_width = 150
    speed = 10
    menu_x = WIDTH if opening else WIDTH - menu_width  # Start off-screen (opening) or fully visible (closing)

    while (opening and menu_x > WIDTH - menu_width) or (not opening and menu_x < WIDTH):
        screen.fill(TAILS_BLUE)

        # Draw the sliding menu
        pygame.draw.rect(screen, SLIDE_COLOR, (menu_x, 0, menu_width, HEIGHT))
        # options = ["Options", "Firmware update"]
        options = ["Options", "Firmware update", "Screen Blackout", "Quit", "Music", "Reboot"]

        for i, option in enumerate(options):
            option_text = font.render(option, True, WHITE)
            screen.blit(option_text, (menu_x + 20, 20 + i * 30))

        # Display current time
        time_text = big_font.render(get_time(), True, WHITE)
        screen.blit(time_text, (menu_x + 20, 90))

        pygame.display.update()

        # Sliding effect
        menu_x -= speed if opening else -speed
        pygame.time.delay(10)

    return WIDTH - menu_width if opening else WIDTH  # Final position

# Sliding Menu Reboot Function (Non-looping, stays open until closed)
def slide_menu_reboot_confirm(opening=True):
    menu_width = 150
    speed = 10
    menu_x = WIDTH if opening else WIDTH - menu_width  # Start off-screen (opening) or fully visible (closing)

    while (opening and menu_x > WIDTH - menu_width) or (not opening and menu_x < WIDTH):
        screen.fill(TAILS_BLUE)

        # Draw the sliding menu
        pygame.draw.rect(screen, SLIDE_COLOR, (menu_x, 0, menu_width, HEIGHT))
        # options = ["Options", "Firmware update"]
        options = ["Reboot", "Yes", "No"]

        for i, option in enumerate(options):
            option_text = font.render(option, True, WHITE)
            screen.blit(option_text, (menu_x + 20, 20 + i * 30))

        # Display current time
        time_text = big_font.render(get_time(), True, WHITE)
        screen.blit(time_text, (menu_x + 20, 90))

        pygame.display.update()

        # Sliding effect
        menu_x -= speed if opening else -speed
        pygame.time.delay(10)

    return WIDTH - menu_width if opening else WIDTH  # Final position

# Blackout Mode Function
def blackout_mode():
    screen.fill(BLACK)
    pygame.display.update()

    blackout = True
    while blackout:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Exit blackout mode when the screen is touched/clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                blackout = False

# Main Firmware Loop
def main():
    intro_static_background()
    intro_screen()
    pygame.mixer.init()
    running = True
    menu_visible = False
    menu_visible_reboot = False
    menu_x = WIDTH  # Menu starts off-screen
    music_playing = False

    while running:
        screen.fill(TAILS_BLUE)

        # Draw the clock
        time_text = big_font.render(get_time(), True, WHITE)
        screen.blit(time_text, (WIDTH // 2 - time_text.get_width() // 2, HEIGHT // 2))



        # Keep the reboot menu visible if open
        if menu_visible_reboot:
            pygame.draw.rect(screen, SLIDE_COLOR, (WIDTH - 150, 0, 150, HEIGHT))
            # options = ["Options", "Firmware update"]
            options = ["Reboot", "Yes", "No"]
            for i, option in enumerate(options):
                option_text = font.render(option, True, WHITE)
                screen.blit(option_text, (WIDTH - 130, 20 + i * 30))




        # Keep the menu visible if open
        if menu_visible:
            pygame.draw.rect(screen, SLIDE_COLOR, (WIDTH - 150, 0, 150, HEIGHT))
            # options = ["Options", "Firmware update"]
            options = ["Options", "Firmware update", "Screen Blackout", "Quit", "Music", "Reboot"]
            for i, option in enumerate(options):
                option_text = font.render(option, True, WHITE)
                screen.blit(option_text, (WIDTH - 130, 20 + i * 30))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False

            # Tap detection for opening/closing menu
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if not menu_visible and x > WIDTH * 0.75:
                    slide_menu(opening=True)
                    menu_visible = True
                elif menu_visible and x < WIDTH - 150:
                    slide_menu(opening=False)
                    menu_visible = False
                elif menu_visible and WIDTH - 150 < x < WIDTH and 90 < y < 120:
                    blackout_mode()

                # Firmware update trigger
                if menu_visible and (WIDTH - 150 < x < WIDTH) and (50 < y < 80):
                    slide_menu(opening=False)
                    menu_visible = False
                    screen.fill(TAILS_BLUE)
                    update_text = big_font.render("Updating", True, BLACK)
                    screen.blit(update_text, (50, 50))
                    pygame.display.flip()
                    run_firmware_update()
                # Quit Button
                if menu_visible and (WIDTH - 150 < x < WIDTH) and (120 < y < 150):
                    slide_menu(opening=False)
                    menu_visible = False
                    #subprocess.run(["kodi"])
                    running = False
                if menu_visible and (WIDTH - 150 < x < WIDTH) and (150 < y < 180):
                    slide_menu(opening=False)
                    menu_visible = False
                    subprocess.run(["bash", "reboot.sh"])
                # Reboot menu yes
                if menu_visible_reboot and (WIDTH - 150 < x < WIDTH) and (90 < y < 120):
                    slide_menu_reboot_confirm(opening=False)
                    menu_visible_reboot = False
                    subprocess.run(["sudo", "reboot", "now"])
                # Reboot menu no
                if menu_visible_reboot and (WIDTH - 150 < x < WIDTH) and (130 < y < 160):
                    slide_menu_reboot_confirm(opening=False)
                    menu_visible_reboot = False
                if menu_visible and (WIDTH - 150 < x < WIDTH) and (150 < y < 180):
                    # slide_menu(opening=False)
                    # menu_visible_reboot = False
                    #pygame.mixer.music.init()
                    if music_playing == False:
                       pygame.mixer.music.load("music.mp3")
                       pygame.mixer.music.play()
                     #  subprocess.run(["cvlc", "music.mp3"])
                    else:
                       pygame.mixer.music.stop()
  #                #    subprocess.run(["killall", "cvlc"])

        pygame.display.update()

    pygame.quit()
    sys.exit()

# Intro Function (TailsWatch Animation)
def intro_screen():
    screen.fill(BLACK)
    title = font.render("Welcome to", True, WHITE)
    subtitle = font.render("TailsWatch", True, TAILS_BLUE)

    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 3))
    screen.blit(subtitle, (WIDTH // 2 - subtitle.get_width() // 2, HEIGHT // 2))
    pygame.display.update()

    start_time = pygame.time.get_ticks()
    while pygame.time.get_ticks() - start_time < 3000:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                return

if __name__ == "__main__":
    main()

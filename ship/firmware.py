import pygame
import sys
import pytz
import subprocess
from datetime import datetime
import subprocess
import os
# Firmware Update Function
def run_firmware_update():
    try:
        # Run the firmware update script
        subprocess.run(['bash', 'initial.sh'], check=True)

        # Restart the firmware after update
        python_exec = sys.executable
        firmware_script = os.path.abspath(__file__)

        # Exit the current process and start the updated firmware
        os.execv(python_exec, [python_exec, firmware_script])

    except subprocess.CalledProcessError:
        print("Firmware update failed.")
        # Optionally display an error message on the screen here
pygame.init();
WIDTH, HEIGHT = 240, 240
screen = pygame.display.set_mode((WIDTH, HEIGHT));
pygame.display.set_caption("TailsWatch First Time Setup");

font = pygame.font.SysFont("Arial", 18)


screen.fill((0, 0, 0))
title = font.render("Downloading Firmware", True, (255, 255, 255))
screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 2))
pygame.display.update();
pygame.display.flip();
run_firmware_update();

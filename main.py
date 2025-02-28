#Shay VanLandschoot
#2/28/25#
# Pygame game template

import pygame
import sys; sys.path
import config 

def init_game():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH,
    config.WINDOW_HEIGHT))
    pygame.display.set_caption("Draw Lines Without a Function")
    return screen

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
    return True


def main(screen):
# Argument 1
    start_pos1 = [30, 25]
    end_pos1 = [250, 400]
    line_color1 = config.GREEN
    line_thickness1 = 8 

 # Argument 2
    start_pos2 = [200, 350]
    end_pos2 = [550, 395]
    line_color2 = config.BLUE
    line_thickness2 = 2

# Argument 3
    start_pos3 = [125, 480]
    end_pos3 = [80, 425]
    line_color3 = config.RED
    line_thickness3 = 7

# Argument 4
    start_pos4 = [225, 590]
    end_pos4 = [25, 410]
    line_color4 = config.BLACK

    line_thickness4 = 12
    
    # Argument5
    start_pos5 = [370, 450]
    end_pos5 = [35, 425]
    line_color5 = config.PURPLE
    line_thickness5 = 3

# Main game loop
    running = True
    while running:
        running = handle_events()


        screen.fill(config.WHITE)


        pygame.draw.line(screen, line_color1, start_pos1, end_pos1,
line_thickness1)
        pygame.draw.line(screen, line_color2, start_pos2, end_pos2,
line_thickness2)
        pygame.draw.line(screen, line_color3, start_pos3, end_pos3,
line_thickness3)
        pygame.draw.line(screen, line_color4, start_pos4, end_pos4,
line_thickness4)
        pygame.draw.line(screen, line_color5, start_pos5, end_pos5,
line_thickness5)

        pygame.display.flip() # Update the display

    pygame.quit() # Quit Pygame
    sys.exit() # Exit the program

if __name__ == "__main__":
    screen = init_game() # Initialize the game and get the screen
    main(screen) # Pass the screen to the main
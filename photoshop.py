"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PURPLE = (255, 0, 255)

pygame.init()
WIDTH = 500
HEIGHT = WIDTH + 50
# Set the width and height of the screen [width, height]
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
image_url = ""
pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if pos[0] < WIDTH/5 and pos[1] > HEIGHT-50:
                image_url = input("name of image file location: ")


    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)

    pygame.draw.rect(screen, PURPLE, [0,HEIGHT-50,WIDTH/5,50])
    pygame.draw.rect(screen, BLUE, [WIDTH/5,HEIGHT-50,WIDTH/5,50])
    pygame.draw.rect(screen, BLACK, [2*WIDTH/5,HEIGHT-50,WIDTH/5,50])
    pygame.draw.rect(screen, GREEN, [3*WIDTH/5,HEIGHT-50,WIDTH/5,50])
    pygame.draw.rect(screen, RED, [4*WIDTH/5,HEIGHT-50,WIDTH/5,50])
    if image_url != "":
        screen.blit(pygame.image.load(image_url).convert(),[0,0])






    # --- Drawing code should go here

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()

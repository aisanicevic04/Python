# def func1(arg1):
#     print("Hello world fucn1")
#     print("arg1: ", arg1)


# mojaVar = "Moja vrednost"
# func1(mojaVar)


# Simple pygame program

# Import and initialize the pygame library
import pygame

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()


# import pygame

# pygame.init()
# window = pygame.display.set_mode((600, 600))
# window.fill((255, 255, 255))
# pygame.draw.circle(window, (0, 255, 0), [300, 300], 170, 3)

# pygame.display.update()

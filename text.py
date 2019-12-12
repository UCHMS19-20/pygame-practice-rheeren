import sys
import pygame

# Initialize pygame so it runs in the background and manages things
pygame.init()

# Create a display. Size must be a tuple, which is why it's in parentheses
red = pygame.Color(255,0,0)
orange = pygame.Color(255,128,0)
yellow = pygame.Color(255,255,0)
green = pygame.Color(0,255,0)
blue =  pygame.Color(0,0,255)
purple =  pygame.Color(255,0,255)
colors = [red, orange, yellow, green, blue, purple]
color_index = 0

screen = pygame.display.set_mode( (400, 300) )
x = 0
y = 0
font = pygame.font.SysFont("Arial", 100)
text = font.render("abc", True, (100,200,255))
# Main loop. Your game would go inside this loop
while True:
    # do something for each event in the event queue (list of things that happen)
    for event in pygame.event.get():
        print(event)
        # Check to see if the current event is a QUIT event
        if event.type == pygame.QUIT:
            # If so, exit the program
            sys.exit()
        if event.type == 4:
            color_index += 1
            if color_index >= len(colors):
                color_index = 0
    screen.fill(colors[color_index])
    screen.blit(text, pygame.mouse.get_pos())
    pygame.display.flip()

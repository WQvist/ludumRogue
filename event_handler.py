import pygame, sys, controllers


def check_events(keyboard_controller):
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # Check for keypresses
        elif event.type == pygame.KEYDOWN:
            keyboard_controller.keyDown(event)
        elif event.type == pygame.KEYUP:
            keyboard_controller.keyUp(event)

"""Listens for events and sends them to the appropriate controller"""
import sys
import pygame

def check_events(keyboard_controller):
    """Routes events to the correct controller"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # Check for keypresses
        elif event.type == pygame.KEYDOWN:
            keyboard_controller.key_down(event)
        elif event.type == pygame.KEYUP:
            keyboard_controller.key_up(event)

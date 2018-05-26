#imports
import pygame, sys
from controller import keyboard_controller

# Setup
pygame.init()
screensize = width, height = 640, 480
black = 0, 0, 0
white = 255, 255, 255
screen = pygame.display.set_mode(screensize)
key_controller = keyboard_controller()

def render(sprites):
    for sprite in sprites:
        screen.blit(sprite[0], sprite[1])
    pygame.display.flip()

def ticks_per_second(tps):
    return 1000/tps

def main():
    # Gameloop
    background = pygame.image.load("assets/background.jpg"), (0,0)
    nonja = pygame.image.load("assets/nonja.png")
    nonja_rect = nonja.get_rect()
    nonja_rect = nonja_rect.move([320,240])
    nonjaen = [nonja, nonja_rect]
    direction = [0,0]
    time = 0
    game_ticks = ticks_per_second(64)
    delta = time+game_ticks
    while 1:
        if time > delta:
            delta = time + game_ticks
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                # Check for keypresses
                elif event.type == pygame.KEYDOWN:
                    direction = key_controller.keyDown(event, direction)
                elif event.type == pygame.KEYUP:
                    direction = key_controller.keyUp(event, direction)
            nonja_rect = nonja_rect.move(direction)
            nonjaen = [nonja, nonja_rect]
            sprites = [background, nonjaen]
            render(sprites)
        time = pygame.time.get_ticks()

main()
#imports
import pygame, sys, event_handler
from controller import keyboard_controller
from nonja_char import Nonja

# Setup
pygame.init()
screensize = width, height = 640, 480
black = 0, 0, 0
white = 255, 255, 255
background = pygame.image.load("assets/background.jpg"), (0,0)
screen = pygame.display.set_mode(screensize)
nonja = Nonja(screen)
key_controller = keyboard_controller(nonja)


def render():
    screen.blit(background[0],background[1])
    nonja.blitme()
    pygame.display.flip()

def ticks_per_second(tps):
    return 1000/tps

def main():
    # Gameloop
    time = 0
    game_ticks = ticks_per_second(64)
    delta = time+game_ticks
    while 1:
        if time > delta:
            delta = time + game_ticks
            event_handler.check_events(key_controller)
            nonja.move()
            render()
        time = pygame.time.get_ticks()


main()
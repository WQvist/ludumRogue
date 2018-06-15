"""Main setup for the game. This module also contains
   the main gameloop"""
#imports
import sys
import pygame
import event_handler
import settings
from controller import KeyboardController
from nonja_char import Nonja


# Setup
pygame.init()
SETTINGS = settings.Settings()

BACKGROUND = pygame.image.load("assets/background.jpg"), (0, 0)
SCREEN = pygame.display.set_mode(
    (SETTINGS.screen_width, SETTINGS.screen_height)
    )
NONJA = Nonja(SCREEN, SETTINGS)
KEY_CONTROLLER = KeyboardController(NONJA)


def render():
	"""Renderes the world and all objects"""
	SCREEN.blit(BACKGROUND[0], BACKGROUND[1])
	NONJA.blitme()
	pygame.display.flip()

def ticks_per_second(tps):
	"""Returns the amount of miliseconds to achieve
	   the desired Tickrate"""
	return 1000/tps

def main():
	"""Main gameloop"""
	# Gameloop
	pygame.mixer.music.load('assets/theme.wav')
	pygame.mixer.music.play(-1)
	time = 0
	game_ticks = ticks_per_second(64)
	delta = time+game_ticks
	while 1:
		if time > delta:
			delta = time + game_ticks
			event_handler.check_events(KEY_CONTROLLER)
			NONJA.move()
			render()
		time = pygame.time.get_ticks()


main()

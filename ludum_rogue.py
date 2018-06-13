#imports
import pygame, sys, event_handler, settings, controllers
from nonja_char import Nonja


# Setup
pygame.init()
settings = settings.Settings()

#screen and background
background = pygame.image.load("assets/background.jpg"), (0,0)
screen = pygame.display.set_mode(
    (settings.screen_width,settings.screen_height)
    )
nonja = Nonja(screen, settings)

#controllers
key_controller = controllers.keyboard_controller(nonja)
mixer =	controllers.sound_controller()
mixer.play_themesong()


def render():
    screen.blit(background[0],background[1])
    nonja.blitme()
    pygame.display.flip()

def ticks_per_second(tps):
    return 1000/tps

def main():
	# Gameloop
	time, delta = 0, 0
	while 1:
		if time > delta:
			delta = time + ticks_per_second(64)
			event_handler.check_events(key_controller)
			nonja.move()
			render()
		time = pygame.time.get_ticks()


main()

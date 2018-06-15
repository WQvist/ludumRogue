"""Controllermodule including keyboard/Sound/etc controllers"""
import sys
import pygame

class KeyboardController():
	"""Handles all keyboard presses"""
	def __init__(self, char):
		self.char = char

	def key_down(self, event):
		"""Decides what happens when a key is pushed"""
		if event.key == pygame.K_RIGHT:
			self.char.move_right = True
		elif event.key == pygame.K_LEFT:
			self.char.move_left = True
		elif event.key == pygame.K_UP:
			if not self.char.jump:
				self.char.jump = True
			elif event.key == pygame.K_ESCAPE:
				sys.exit()


	def key_up(self, event):
		"""Decides what happens when a key is released"""
		if event.key == pygame.K_RIGHT:
			self.char.move_right = False
		elif event.key == pygame.K_LEFT:
			self.char.move_left = False

import pygame, sys

class keyboard_controller():
    def __init__(self, char):
        self.char = char
         
    def keyDown(self,event):
        if event.key == pygame.K_RIGHT:
            self.char.move_right = True
        elif event.key == pygame.K_LEFT:
            self.char.move_left = True
        elif event.key == pygame.K_UP:
            if not self.char.jump:
                self.char.jump = True
                self.falling = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()


    def keyUp(self,event):
        if event.key == pygame.K_RIGHT:
            self.char.move_right = False
        elif event.key == pygame.K_LEFT:
            self.char.move_left = False
            
class sound_controller():
	
	def play_themesong(self):
		pygame.mixer.music.load('assets/theme.wav')
		pygame.mixer.music.play(-1)

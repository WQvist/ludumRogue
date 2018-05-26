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
        """elif event.key == pygame.K_UP:
            if self.char.jump:
                self.char.jump = False
                self.char.falling = True"""

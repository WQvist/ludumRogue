import pygame, sys

class keyboard_controller():
    def __init__(self, char):
        self.char = char
         
    def keyDown(self,event):
        if event.key == pygame.K_RIGHT:
            self.char.speed[0] +=1
        elif event.key == pygame.K_DOWN:
            self.char.speed[1] +=1
        elif event.key == pygame.K_LEFT:
            self.char.speed[0] -= 1
        elif event.key == pygame.K_UP:
            self.char.speed[1] -= 1
        elif event.key == pygame.K_ESCAPE:
            sys.exit()


    def keyUp(self,event):
        if event.key == pygame.K_RIGHT:
            self.char.speed[0] -= 1
        elif event.key == pygame.K_DOWN:
            self.char.speed[1] -=1
        elif event.key == pygame.K_LEFT:
            self.char.speed[0] += 1
        elif event.key == pygame.K_UP:
            self.char.speed[1] += 1

import pygame

class keyboard_controller():
    def keyDown(self,event, current_speed):
        if event.key == pygame.K_RIGHT:
            current_speed[0] += 1
            return current_speed
        elif event.key == pygame.K_DOWN:
            current_speed[1] +=1
            return current_speed
        elif event.key == pygame.K_LEFT:
            current_speed[0] -= 1
            return current_speed
        elif event.key == pygame.K_UP:
            current_speed[1] -= 1
            return current_speed
        else:
            return current_speed


    def keyUp(self,event, current_speed):
        if event.key == pygame.K_RIGHT:
            current_speed[0] -= 1
            return current_speed
        elif event.key == pygame.K_DOWN:
            current_speed[1] -=1
            return current_speed
        elif event.key == pygame.K_LEFT:
            current_speed[0] += 1
            return current_speed
        elif event.key == pygame.K_UP:
            current_speed[1] += 1
            return current_speed
        else:
            return current_speed

#imports
import pygame, sys

# Setup
pygame.init()
screensize = width, height = 640, 480
black = 0, 0, 0
white = 255, 255, 255
screen = pygame.display.set_mode(screensize)
global swap
global boll
global boll_rect

def render(boll_info):
    screen.fill(black)
    screen.blit(boll_info[0], boll_info[1])
    pygame.display.flip()

def controll_keyDown(event, current_speed):
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


def controll_keyUp(event, current_speed):
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

def ticks_per_second(tps):
    return 1000/tps

def main():
    # Gameloop
    boll = pygame.image.load("boll.png")
    boll_rect = boll.get_rect()
    boll_rect = boll_rect.move([320,240])
    bollen = [boll, boll_rect]
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
                    direction = controll_keyDown(event,direction)
                elif event.type == pygame.KEYUP:
                    direction = controll_keyUp(event, direction)
            boll_rect = boll_rect.move(direction)
            bollen = [boll, boll_rect]
            render(bollen)
        time = pygame.time.get_ticks()

main()
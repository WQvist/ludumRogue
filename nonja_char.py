import pygame

class Nonja():
    def __init__(self, screen, settings):
        self.screen = screen
        self.speed = [0,0]
        self.speed_factor = settings.speed_factor
        self.image = pygame.image.load("assets/nonja.png")
        self.rect = self.image.get_rect()
        self.move_right = False
        self.move_left = False
        self.jump = False
        self.falling = True
        self.settings = settings

    def move(self):
        if self.move_left:
            self.speed[0] = -self.speed_factor
        if self.move_right:
            self.speed[0] = self.speed_factor
        if self.move_right and self.move_left:
            self.speed[0] = 0
        if not self.move_left and not self.move_right:
            self.speed[0] = 0
        if self.falling:
            self.speed[1] += self.settings.gravity
        if self.rect.bottom+self.speed[1] > self.settings.screen_height:
            self.rect.bottom = self.settings.screen_height
            self.speed[1] = 0
            self.falling = False
            self.jump = False
        if self.jump and not self.falling:
            self.speed[1] = self.settings.jump_factor
            self.falling = True
        self.rect = self.rect.move(self.speed)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

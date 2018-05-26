import pygame

class Nonja():
    def __init__(self, screen):
        self.screen = screen
        self.speed = [0,0]
        self.speed_factor = 1
        self.image = pygame.image.load("assets/nonja.png")
        self.rect = self.image.get_rect()

    def move(self):
        self.speed[0] *= self.speed_factor
        self.speed[1] *= self.speed_factor
        self.rect = self.rect.move(self.speed)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

import pygame

class Ship:

    def __init__(self,ai_game):
        #init ship set starting point
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        #load ship image
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        #start each new ship in bottom center
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        #movement
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #update rect object
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)

        
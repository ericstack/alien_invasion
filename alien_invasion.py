import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((800,600))
        self.settings.screen_height = self.screen.get_rect().width
        self.settings.screen_width = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        #set bg color
        self.bg_color = self.settings.bg_color

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
          
    def _check_events(self):
        #respond to key and mouse event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                 self._check_keyup_events(event)
                
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bulltes_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <=0:
                self.bullets.remove(bullet)
                print(len(self.bullets))

    def _create_fleet(self):
        #make an alien.

        alien=Alien(self)
        alien_width, alien_height = alien.rect.size
        # available_space_x = self.settings.screen_width - (2 * alien_width)
        # number_aliens_x = available_space_x // (2 * alien_width)
        # alien_width, alien_height = alien.rect.size
        # available_space_x = self.settings.screen_width - (2 * alien_width)
        # number_aliens_x = available_space_x // (2 * alien_width)
        
        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x,current_y)
                current_x +=2 * alien_width

        # ship_height = self.ship.rect.height
        # available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        # number_rows = available_space_y // (2 * alien_height)
      
        # for alien_number in range(number_aliens_x):
        #     alien = Alien(self)
        #     alien.x = alien_width + 2 * alien_width * alien_number
        #     alien.rect.x = alien.x
        #     self.aliens.add(alien)

        # for row_number in range(number_rows):
        #     for alien_number in range(number_aliens_x):
        #         self._create_alien(alien_number, row_number)

    # def _create_alien(self, x_postion, y_position):

    #     new_alien= Alien(self)
    #     new_alien.x= x_postion
    #     new_alien.rect.x = x_postion
    #     new_alien.rect.y = y_position
    #     self.aliens.add(new_alien)

    #     alien_width, alien_height = alien.rect.size
    #     alien.x = alien_width + 2 * alien_width * alien_number
    #     alien.rect.x = alien.x
    #     alien.rect.y = alien_height + 2 * alien.rect.height * row_number
    #     self.aliens.add(alien)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        pygame.display.flip()

if __name__ == '__main__':
    ai=AlienInvasion()
    ai.run_game()
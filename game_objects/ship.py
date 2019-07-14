import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """A class of ship object"""

    def __init__(self, screen, settings):
        """Initialize the ship and set its starting position"""
        super().__init__()
        self.screen = screen
        self.settings = settings

        # Load ship image and its rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        # Store decimal value for the ship's center
        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_down = False
        self.moving_up = False

    def center_ship(self):
        """Set ship to it's starting position"""
        self.center_x = self.screen_rect.centerx
        self.center_y = self.screen_rect.centery

    def update_position(self):
        """Update the ship's position based off it's movement"""

        # Update the ship's center values, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center_x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.center_x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.center_y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center_y += self.settings.ship_speed

        # Update ship's rect
        self.rect.centerx = self.center_x
        self.rect.centery = self.center_y

    def blit_me(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

import pygame


class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its  starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Load the ship.bmp and get its rect.
        self.image = pygame.image.load("alien_invasion/images/ship_center.bmp")

        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a float for the ship's exact horizontal position.
        self.x = float(self.rect.x)

        # Movement flag; star with the shit that's not moving
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag"""
        """Update the ship's x value not the rect."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
            self.image = pygame.image.load("alien_invasion/images/ship_right.bmp")
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
            self.image = pygame.image.load("alien_invasion/images/ship_left.bmp")
        if not self.moving_left and not self.moving_right:
            self.image = pygame.image.load("alien_invasion/images/ship_center.bmp")

        self.rect.x = int(self.x)

    def blitme(self):
        """Draw the ship at the current locations."""
        self.screen.blit(self.image, self.rect)

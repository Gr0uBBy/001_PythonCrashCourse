import pygame


class Settings:
    def __init__(self):
        """General game settings"""

        # Display settings
        self.screen_width = 1200
        self.screen_height = 800

        # --- Background
        self.bg_color = (230, 230, 230)
        self.bg_image = pygame.image.load(
            "exercises/exercise_alien_invasion/images/background/nightskyemission.png"
        )
        self.bg_x = 0

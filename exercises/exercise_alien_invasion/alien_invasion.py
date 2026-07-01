import sys

import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    def __init__(self):
        pygame.init()

        self.settings = Settings()

        self.clock = pygame.time.Clock()

        # Prepare the Display
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("The best Alien Invasion GAME EVER!")
        self.bg_image = pygame.transform.scale(
            self.settings.bg_image,
            (self.settings.screen_width, self.settings.screen_height),
        )

        self.ship = Ship(self)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Moving the background
            self.settings.bg_x -= 1
            if self.settings.bg_x <= -self.settings.screen_width:
                self.settings.bg_x = 0

            # Draw the background
            # self.screen.fill(self.settings.bg_color)
            self.screen.blit(self.bg_image, (self.settings.bg_x, 0))
            self.screen.blit(
                self.bg_image, (self.settings.bg_x + self.settings.screen_width, 0)
            )

            # Draw the ship image
            self.ship.blitme()

            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()

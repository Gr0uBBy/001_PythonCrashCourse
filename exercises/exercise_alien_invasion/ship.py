import pygame


class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load(
            "exercises/exercise_alien_invasion/images/ships/13B.png"
        )
        org_hight = self.image.get_height()
        org_width = self.image.get_width()

        self.image = pygame.transform.scale(
            self.image, (org_width // 2, org_hight // 2)
        )

        self.rect = self.image.get_rect()

        self.rect.midleft = self.screen_rect.midleft

    def blitme(self):
        self.screen.blit(self.image, self.rect)

import sys
import pygame
from settings import Settings
from stars import Star

class StarGame:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Stars")
        self.stars = pygame.sprite.Group()
        
        self._create_fleet()

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_q:
            sys.exit()

    def _create_fleet(self):
        star = Star(self)
        star_width, star_height = star.rect.size

        current_y = star_height
        while current_y < (self.settings.screen_height - 3 * star_height):
            current_x = star_width
            while current_x < (self.settings.screen_width - 2 * star_width):
                self._create_star(current_x, current_y)
                current_x += 2 * star_width
            current_y += 2 * star_height

    def _create_star(self, x_position, y_position):
        new_star = Star(self)
        new_star.x = x_position
        new_star.rect.x = x_position
        new_star.rect.y = y_position
        self.stars.add(new_star)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)
        pygame.display.flip()

if __name__ == '__main__':
    sg = StarGame()
    sg.run_game()

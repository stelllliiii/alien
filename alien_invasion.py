import sys
import pygame
from settings import Settings

class  AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.bg_color = (230,230,230)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            #重绘屏幕
            self.screen.fill(self.settings.bg_color)
            pygame.display.filp()

if __name__== ' __main__':
    ai = AlienInvasion()
    ai.run_game()

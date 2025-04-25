import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """A class to represent stars."""
    
    def __init__(self, sg):
        super().__init__()
        self.screen = sg.screen
        
        # Load the star image and set its rect attribute.
        self.image = pygame.image.load('images/star.png')
        self.rect = self.image.get_rect()
        
        # Start each star near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        self.x = float(self.rect.x)
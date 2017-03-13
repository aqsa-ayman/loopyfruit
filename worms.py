import pygame
import random

class Worm(pygame.sprite.Sprite):
    # constructor
    def __init__(self):
        # get superclass functionality
        super(Worm, self).__init__()

        # load sprite image
        self.image = pygame.image.load('worm2.png')

        # change size of image
        worm_height = 100
        worm_width = 90
        self.image = pygame.transform.scale(self.image, (worm_width, worm_height))

        # fetch rectangle object that has dimensions of the image
        self.rect = self.image.get_rect()

        # speed of worms i.e. what we increase position by in each loop
        self.dy = 5

    def update(self):
        # if worms fall beyond bottom of screen
        if self.rect.centery > 600:
            # reset their y positions
            self.rect.centery = random.randrange(-800, -50)
            # reset their x positions
            self.rect.centerx = random.randrange(10, 790)

        # make them fall
        self.rect.centery += self.dy


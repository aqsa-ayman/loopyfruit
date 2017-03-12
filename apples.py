import pygame
import random

class Apple(pygame.sprite.Sprite):
    # constructor
    def __init__(self):
        # get superclass functionality
        super(Apple, self).__init__()

        # load sprite image
        self.image = pygame.image.load('apple4.png')

        # change size of image
        apple_width = 60
        apple_height = 75
        self.image = pygame.transform.scale(self.image, (apple_width, apple_height))

        # fetch rectangle object that has dimensions of the image
        self.rect = self.image.get_rect()

        # speed of apples i.e. what we increase position by in each loop
        self.dy = 5

    def update(self):

        # if apples fall beyond bottom of screen
        if self.rect.centery > 600:
            # reset their y positions
            self.rect.centery = random.randrange(-800, -50)
            # reset their x positions
            self.rect.centerx = random.randrange(0, 800)

        # make them fall
        self.rect.centery += self.dy

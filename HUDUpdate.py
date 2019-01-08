## HUDUpdate.py
## Onyx Games group project
## EAE 1410 Spring '17

import pygame
from pygame.locals import *

class updateHUD(object):

    def __init__(self):

        self.image = pygame.image.load('Sprites/items/heart.png')

    def update(self, numHearts, surf):

        xPos = 25

        for index in range(numHearts):

            surf.blit(self.image, (xPos,20))
            xPos += 65
                      

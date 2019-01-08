## projectile_class.py
## Onyx Games Group Project
## EAE 1410 Spring '17

import pygame, pyganim

class Projectile(pygame.sprite.Sprite):


    def __init__(self, POS, DIR, size):

        super().__init__()

    
        self.size = size
        self.color = (244,203,  0)
        if DIR == True:
            self.dir = 'right'
        else:
            self.dir = 'left'

        self.image = pygame.Surface(self.size)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        self.velocity= 12

        self.rect.x = POS[0]
        self.rect.y = POS[1]
      

    def update(self):
        if self.dir == 'right':
            self.rect.x += self.velocity
        elif self.dir =='left':
            self.rect.x -= self.velocity

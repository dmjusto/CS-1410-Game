## item_class.py
## Onyx Games group project
## EAE 1410 Spring '17

import pygame, pyganim

class item(pygame.sprite.Sprite):

    def __init__(self,SIZE,POS,surf):
        
        super().__init__()

        self.SIZE = SIZE
        self.POS = POS

        self.Vspeed = 0
        self.grav = .4
        self.active = True
        self.surf = surf

        self.blank = pygame.image.load('Sprites/invis_char.png')
        self.image = pygame.Surface(self.SIZE)
        self.image = self.blank
        self.rect = self.image.get_rect()

        self.rect.x = POS[0]
        self.rect.y = POS[1]

        self.itemAnim = pyganim.PygAnimation([('Sprites/items/health_pickup0.png', 2.0),
                                         ('Sprites/items/health_pickup1.png', 0.05),
                                         ('Sprites/items/health_pickup2.png', 0.05),
                                         ('Sprites/items/health_pickup3.png', 0.05)])

        self.itemAnim.play()

    def draw(self):
        
        if self.active:

            self.surf.blit(self.image,self.rect)
            self.itemAnim.blit(self.surf,self.rect)

        else:
            self.itemAnim.stop()


    def update(self, collidables, fadedCollide):

        self.Vspeed += self.grav
        self.rect.y += self.Vspeed
        
        block_hit_list = pygame.sprite.spritecollide(self, collidables, False)
        for block in block_hit_list:
            
            if self.Vspeed > 0:
                self.rect.bottom = block.rect.top
                self.Vspeed = 0                               
                
            elif self.Vspeed < 0:
                self.rect.top = block.rect.bottom

        block_hit_list = pygame.sprite.spritecollide(self, fadedCollide, False)
        for block in block_hit_list:
            
            if self.Vspeed > 0:
                self.rect.bottom = block.rect.top
                self.Vspeed = 0                               
                
            elif self.Vspeed < 0:
                self.rect.top = block.rect.bottom

        self.draw()

            
        

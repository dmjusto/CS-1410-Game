## level_class.py
## Onyx Games Group project
## EAE 1410 Spring '17

import pygame
from pygame.locals import *

class LEVEL(object):

    def __init__(self,T_SIZE, L_SIZE, L_POS):

        

        self.t_size = T_SIZE
        self.pos = L_POS
        self.screenSize = (L_SIZE[0] * T_SIZE[0],L_SIZE[1] * T_SIZE[1])
        self.TRANS = (0,0,0,0)

        self.image = pygame.Surface(self.screenSize,flags=SRCALPHA,depth=32)
        self.image.fill(self.TRANS)
        self.image.convert()
        self.image.set_alpha(100)
        

        self.platform_group = pygame.sprite.Group()
        self.sprite_group = pygame.sprite.Group()
        
#####
    
        
#####

class TILE(pygame.sprite.Sprite):

    def __init__(self, LEVEL, T_POS, T_NAME, T_SIZE, L_POS):

        super().__init__()

        self.t_size = T_SIZE
        self.level = LEVEL
        self.t_pos = T_POS
        
        self.T_Surf = pygame.image.load(T_NAME)
        self.T_Surf = pygame.transform.scale(self.T_Surf, self.t_size)


        self.rect = self.T_Surf.get_rect()
        self.rect.x = self.t_pos[0] * self.t_size[0] + (L_POS[0] * T_SIZE[0])
        self.rect.y = self.t_pos[1] * self.t_size[1] + (L_POS[1] * T_SIZE[1])

        self.Hspeed = 0
        self.Vspeed = 0
        self.grav = .4
        self.jump_speed = -10
        self.speed = 5
        self.run = 1
        self.run_const = 1.8

        self.level.image.blit(self.T_Surf,(self.rect.x,self.rect.y))


class FADE_BLOCK(pygame.sprite.Sprite):

    def __init__(self, LEVEL, T_POS, T_NAME, T_SIZE, L_POS):

        super().__init__()

        self.t_size = T_SIZE
        self.level = LEVEL
        self.t_pos = T_POS

        self.solid = False # whether or not block is solid to player
        self.delayF = 0 # Number of frames before first fade begins
        self.alpha = 254 # block tile's alpha
        self.alpha_dir = -1 # how quickly block fades
        self.time = 0

        
        
        self.image = pygame.image.load(T_NAME)
        self.image = pygame.transform.scale(self.image, self.t_size)
###
        self.image = self.image.convert()

        self.image.set_alpha(self.alpha)
        
###

        self.rect = self.image.get_rect()
        self.rect.x = self.t_pos[0] * self.t_size[0] + (L_POS[0] * T_SIZE[0])
        self.rect.y = self.t_pos[1] * self.t_size[1] + (L_POS[1] * T_SIZE[1])

        self.level.image.blit(self.image,(self.rect.x,self.rect.y))

##    def update(self):
##        
##        if pygame.time.get_ticks() - self.time >= 20:
##            self.alpha -= self.alpha_dif
##            if self.alpha <= 0:
##                self.alpha = 255
##            self.image.set_alpha(self.alpha)
##            self.time = pygame.time.get_ticks()
##            self.level.Surf.blit(self.image,(self.rect.x,self.rect.y))
        
    

        
## Level Scrolling ##################################

    def move_left(self):
        self.Hspeed = -self.speed            

    def move_right(self):
        self.Hspeed = self.speed            

    def stop_move(self):
        self.Hspeed = 0

    def player_run(self):
        self.run = self.run_const

    def stop_run(self):
        self.run = 1

    def level_update(self):

        self.rect.x += self.Hspeed * self.run
        self.level.Surf.blit(self.T_Surf,(self.rect.x,self.rect.y))
        



#####################################################
        





        

## Enemies.py
## Onyx Games group project
## EAE 1410 Spring '17


import pygame, pyganim
from math import *

class SKULL(pygame.sprite.Sprite):

    def __init__(self, POS):

        super().__init__()

##        self.position = vector2(POS)
##        self.heading = vector2()
        self.hSpeed = -6
        self.frame_sp = 0.1
        self.size = (64,64)
        self.image = pygame.Surface(self.size)
        self.rect = self.image.get_rect()
        self.theta = 0
        self.angle_diff = 5 ## amount that theta is increased each frame;
        ## affects how smooth the sine wave is
        
        self.mult = 50 ## sine function multiplyer; affects max and min
        ## of sine wave
        
        self.radian_diff = 0
        self.POS = POS
        self.startX = POS[0]
        self.startY = POS[1]
        self.LEFT = True
        self.i = 1

        self.following = False # whether skull is tracking player
        self.min_dist = 350 # if closer than this then following is True
        self.speed = (0,0) # x and y components of Speed

        self.health = 3
        

        
        self.skullAnim_up = pyganim.PygAnimation([('Sprites/enemy/skull/skull_acend_0.png',self.frame_sp),
                                                  ('Sprites/enemy/skull/skull_acend_1.png',self.frame_sp),
                                                  ('Sprites/enemy/skull/skull_acend_2.png',self.frame_sp)])
        
        self.skullAnim_down = pyganim.PygAnimation([('Sprites/enemy/skull/skull_decend_0.png',self.frame_sp),
                                                  ('Sprites/enemy/skull/skull_decend_1.png',self.frame_sp),
                                                  ('Sprites/enemy/skull/skull_decend_2.png',self.frame_sp)])
        
        self.skullAnim_lvl = pyganim.PygAnimation([('Sprites/enemy/skull/skull_level_0.png',self.frame_sp),
                                                  ('Sprites/enemy/skull/skull_level_1.png',self.frame_sp),
                                                  ('Sprites/enemy/skull/skull_level_2.png',self.frame_sp)])

        self.skullAnim_lvl_R = self.skullAnim_lvl.getCopy()
        self.skullAnim_lvl_R.flip(True,False)
        self.skullAnim_lvl_R.makeTransformsPermanent()
        
        self.skullAnim_up.play()
        self.skullAnim_down.play()
        self.skullAnim_lvl.play()
        
        self.rect.x = POS[0]
        self.rect.y = POS[1]

##    def get_player_dis(self,P_POS):
##        return sqrt(pow((P_POS[0]-(self.rect.x + 32)),2) + pow((P_POS[1] - (self.rect.y +32)),2))

##    def get_sp_comps(self, P_POS):
##        pass
##    def get_angle(self, P_POS):
##        adj = abs(P_POS[0]-(self.rect.x +32))
##        hyp = abs(P_POS[1] -(self.rect.y + 32))
##        return acos(adj/hyp)

    def update(self,SURF, P_POS, bullets, SCROLL_SPD, SCROLLING):

        if SCROLLING:
            self.scroll_spd = SCROLL_SPD
        else:
            self.scroll_spd = 0
        
        collidables = bullets           

##        if self.rect.x <= (self.startX - 800) or self.rect.x >= (self.startX + 200):
        if self.i >= 125:
            self.hSpeed *= -1            
            self.skullAnim_lvl.flip(True,False)            
            self.i = 1
        self.i += 1
       
        self.radian_diff = self.mult * sin(radians(self.theta))
        self.rect.y = self.POS[1] + self.radian_diff
        self.rect.x += self.hSpeed #- self.scroll_spd

        self.skullAnim_lvl.blit(SURF,(self.rect.x,self.rect.y-32))

        if self.theta >= 360:
            self.theta = 0
        else:
            self.theta += self.angle_diff

        block_hit_list = pygame.sprite.spritecollide(self, collidables, False)
        for b in block_hit_list:
            self.health -=1

                 

class SNAKE(pygame.sprite.Sprite):

    def __init__(self,POS):

        super().__init__()
        
        self.size = (44,64)
        self.image = pygame.Surface(self.size)
        self.rect = self.image.get_rect()
        self.health = 2

        self.rect.x = POS[0]
        self.rect.y = POS[1]

        self.frame_sp = 0.1
        self.animObjs = {}

        imagesAndDurations = [('Sprites/enemy/snake/snake0.png',self.frame_sp),
                              ('Sprites/enemy/snake/snake1.png',0.3),
                              ('Sprites/enemy/snake/snake2.png',self.frame_sp)]

        self.animObjs['attack'] = pyganim.PygAnimation(imagesAndDurations)

        imagesAndDurations = [('Sprites/enemy/snake/snake0.png',self.frame_sp)]

        self.animObjs['idle'] = pyganim.PygAnimation(imagesAndDurations)

        self.animObjs['right_attack'] = self.animObjs['attack'].getCopy()
        self.animObjs['right_attack'].flip(True, False)
        self.animObjs['right_attack'].makeTransformsPermanent()

        self.animObjs['right_idle'] = self.animObjs['idle'].getCopy()
        self.animObjs['right_idle'].flip(True, False)
        self.animObjs['right_idle'].makeTransformsPermanent()

        self.snakeConductor = pyganim.PygConductor(self.animObjs)
        
        self.snakeConductor.play()
        
    def update(self,SURF, P_POS, bullets, SCROLL_SPD, SCROLLING):

        if (P_POS[0] < (self.rect.x - 300) or P_POS[0] > (self.rect.x + 300)) and ( P_POS[1] < (self.rect.y - 100) or P_POS[1] > (self.rect.y + 100) ):
            
            if P_POS[0] < self.rect.x: #left of snake 
                self.animObjs['idle'].blit(SURF, ((self.rect.x-4), self.rect.y))
            else:
                self.animObjs['right_idle'].blit(SURF, ((self.rect.x-4), self.rect.y))

        else:
            
            if P_POS[0] < self.rect.x: #right of snake 
                self.animObjs['attack'].blit(SURF, ((self.rect.x-4), self.rect.y))
            else:
                self.animObjs['right_attack'].blit(SURF, ((self.rect.x-4), self.rect.y))

        collidables = bullets
        block_hit_list = pygame.sprite.spritecollide(self, collidables, False)
        for b in block_hit_list:
            self.health -=1

        

        

        
        

            

        

## player_class.py
## Onyx Games Group Project
## EAE 1410 Spring '17

import pygame, pyganim

class PLAYER(pygame.sprite.Sprite):

    def __init__(self,SIZE,POS,S_SIZE):

        super().__init__()

        self.size = SIZE
        self.s_size = S_SIZE       
        self.image = pygame.Surface(self.size)
        self.image.fill((0,0,0,0))
        self.rect = self.image.get_rect()

        self.Hspeed = 0
        self.Vspeed = 0
        self.speed = 5 # walk speed
        self.run_const = 1.6
        self.run = 1
        self.grav = .4 # effect of gravity
        self.jump_speed = -10
        self.num_jumps = 2 #number of jumps allowed before touching ground
        self.jumps = self.num_jumps
        self.grounded = False # whether or not we are touching the ground
        self.running = False
        self.right = True
        self.left = False
        self.active = True

        self.rect.x = POS[0]
        self.rect.y = POS[1]

    def getPos(self):
        return (self.rect.x - 20, self.rect.y - 2)

    def itemGet(self, collectables):
        
        points = 0
        collectables_list = pygame.sprite.spritecollide(self, collectables, True)
        for collect in collectables_list:
            points += 1

        return points

    def change_speed(self, Hspeed, Vspeed):

        self.Hspeed += Hspeed
        self.Vspeed += Vspeed

    def move_left(self):
        self.Hspeed = -self.speed            

    def move_right(self):
        self.Hspeed = self.speed            

    def stop_move(self):
        self.Hspeed = 0

    def player_run(self):
        if self.grounded:
            
            self.run = self.run_const

    def stop_run(self):
        self.run = 1

    def jump(self):           
            
        if self.jumps > 0:            
            self.jumps -= 1
            self.Vspeed = self.jump_speed
            self.grounded = False
            

    def getGrounded(self):
        return self.grounded

    def getVSpeed(self):
        return self.Vspeed

    
    def update(self,collidables,collidables2, SCREEN_SIZE, L_SCROLL_X, LEVEL):

        self.Vspeed += self.grav

##        self.image = self.playerIdle

        if self.run == 1 and self.running:
            self.player_run()

        
        if (self.rect.x < self.s_size[0] - self.s_size[0]//3 and self.right) or (self.rect.x >= self.s_size[0] - self.s_size[0]//3 and self.right) and L_SCROLL_X <= -1 * (LEVEL.screenSize[0] - self.s_size[0]):
            
            self.rect.x += self.Hspeed * self.run
            
        elif (self.rect.x > self.s_size[0]//3 and self.left) or (self.rect.x <= self.s_size[0]//3 and self.left) and L_SCROLL_X >= 0:

            self.rect.x += self.Hspeed * self.run

            
        
        block_hit_list = pygame.sprite.spritecollide(self, collidables, False)
        for block in block_hit_list:
            
            if self.Hspeed > 0:
                self.rect.right = block.rect.left
                
            elif self.Hspeed < 0:
                self.rect.left = block.rect.right


## horizontal collisions with Fade blocks
        block_hit_list = pygame.sprite.spritecollide(self, collidables2, False)
        for block in block_hit_list:
            if block.solid == True:
                if self.Hspeed > 0:
                    self.rect.right = block.rect.left
                    
                elif self.Hspeed < 0:
                    self.rect.left = block.rect.right

##        if self.rect.y > self.s_size[1] - self.s_size[1]//3:        
        self.rect.y += self.Vspeed        


        block_hit_list = pygame.sprite.spritecollide(self, collidables, False)
        for block in block_hit_list:
            
            if self.Vspeed > 0:
                self.rect.bottom = block.rect.top
                self.Vspeed = 0
                self.jumps = self.num_jumps
                self.grounded = True                                   
                
            elif self.Vspeed < 0:
                self.rect.top = block.rect.bottom
                self.grounded = False

            if self.rect.top == block.rect.bottom:
                self.Vspeed = -0.1
                self.rect.top = block.rect.bottom

## vertical collisions with fade blocks
        block_hit_list = pygame.sprite.spritecollide(self, collidables2, False)
        for block in block_hit_list:

            if block.solid == True:
            
                if self.Vspeed > 0:
                    self.rect.bottom = block.rect.top
                    self.Vspeed = 0
                    self.jumps = self.num_jumps
                    self.grounded = True                                   
                    
                elif self.Vspeed < 0:
                    self.rect.top = block.rect.bottom
                    self.grounded = False

                if self.rect.top == block.rect.bottom:
                    self.Vspeed = -0.1
                    self.rect.top = block.rect.bottom
                
                
                



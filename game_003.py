## game.py
## Onyx Games group project
## EAE 1410 Spring '17

import pygame, sys, pyganim, random
from level_1 import *

from pygame.locals import *
from level_class_002 import LEVEL, TILE, FADE_BLOCK
from player_class import PLAYER
from projectile_class import Projectile
from playerAnimation import playerAnimate
from HUDUpdate import updateHUD
from item_class import item
from Enemies import SKULL,SNAKE

pygame.mixer.pre_init(44100,-16,2,2048)
pygame.init()

BG_COLOR = (0,13,38)
SCREEN_SIZE = (1088, 768)

##player info ###################################
PLAYER_SIZE = (47, 88)
PLAYER_POS = (SCREEN_SIZE[0]//2, SCREEN_SIZE[1]//2)

######################################################

DISPLAYSURF = pygame.display.set_mode(SCREEN_SIZE, HWSURFACE | DOUBLEBUF)
pygame.display.set_caption('Onyx Games Platformer')
DISPLAYSURF.fill(BG_COLOR)


## Level Creation ###################################

TILE_SET_LIST = ['Tiles/block1.png','Tiles/block2.png','Tiles/block3.png',
                 'Tiles/f_column3.png','Tiles/f_column2.png','Tiles/f_column1.png',
                 'Tiles/flag2.png','Tiles/flag1.png',
                 'Tiles/b_column3.png','Tiles/b_column2.png','Tiles/b_column1.png']

level1 = LEVEL(T_SIZE,L_SIZE, L_POS)
i = 0
for LIST in L1_LOL:

    for  t in LIST:        
        level1.platform_group.add(TILE(level1,t,TILE_SET_LIST[i],T_SIZE, L_POS))
    i += 1

level_1_fore = LEVEL(T_SIZE,L_SIZE, L_POS)
for LIST in L1_LOL2:

    for t in LIST:
        level_1_fore.platform_group.add(TILE(level_1_fore,t,TILE_SET_LIST[i],T_SIZE, L_POS))
    i += 1

level_1_back = LEVEL(T_SIZE,L_SIZE, L_POS)
for LIST in L1_LOL3:

    for t in LIST:
        level_1_back.platform_group.add(TILE(level_1_back,t,TILE_SET_LIST[i],T_SIZE, L_POS))
    i += 1
#### Fading Blocks ##################################


level_fade = LEVEL(T_SIZE,L_SIZE, L_POS)
##for LIST in L1_LOL4:
for t in fadeBlockList1:
    level_fade.platform_group.add(FADE_BLOCK(level_fade,t,TILE_SET_LIST[0],T_SIZE, L_POS, 10))
for t in fadeBlockList2:
    level_fade.platform_group.add(FADE_BLOCK(level_fade,t,TILE_SET_LIST[0],T_SIZE, L_POS, 70))
for t in fadeBlockList3:
    level_fade.platform_group.add(FADE_BLOCK(level_fade,t,TILE_SET_LIST[0],T_SIZE, L_POS, 175))
######################################################


## Enemies ##########################################
skull_list = [(2500,200), (5000, 500), (5500, 200),(7500,300),(6800,500)]

enemy_group = pygame.sprite.Group()

for skull in skull_list:
    enemy_group.add(SKULL(skull))

snake_list = [(4608,640),(4608,384),(5440,640),(5376,192)]

for snake in snake_list:
    enemy_group.add(SNAKE(snake))

    
### ITEM CREATION ###################################

item_group = pygame.sprite.Group()
def make_healthItem(x,y):
    global item_group
    item_group.add(item((24,24),(x,y),DISPLAYSURF))
    
    for x in item_group:
        x.draw()    

## projectile code################################

fireAnim = pyganim.PygAnimation([('Sprites/projectile/fireball1.png',0.2),
                                  ('Sprites/projectile/fireball2.png',0.2)])

leftFireAnim = fireAnim.getCopy()
leftFireAnim.flip(True,False)
leftFireAnim.makeTransformsPermanent()

fireAnim.play()
leftFireAnim.play()

bullet_group = pygame.sprite.Group()
def make_bullet(player,RIGHT):
    if RIGHT == True:
        POS = (player.rect.x + 24, player.rect.y + 35)
    else:
        POS = (player.rect.x - 24, player.rect.y + 35)
    bullet_group.add(Projectile(POS,RIGHT,(40,24)))


def draw_bullets(RIGHT):
    hitsList = pygame.sprite.groupcollide(bullet_group, level1.platform_group, True, False)
    for b in bullet_group:
           
        if b.rect.x > 0 and b.rect.y > -30 and b.rect.x < SCREEN_SIZE[0] and b.rect.y < SCREEN_SIZE[1]:
            b.update()
            if b.dir == 'right':
                fireAnim.blit(DISPLAYSURF,(b.rect.x,b.rect.y))
            else:
                leftFireAnim.blit(DISPLAYSURF,(b.rect.x,b.rect.y))
            
        else:
            bullet_group.remove(b)

#sound code#################################################
pygame.mixer.music.load('Sounds/02_Underclocked_underunderclocked_mix.wav')
pygame.mixer.music.play(-1)

jump_sound = pygame.mixer.Sound('Sounds/Character_Jump.wav')
attack_sound = pygame.mixer.Sound('Sounds/player_attack.wav')
playerHit_sound = pygame.mixer.Sound('Sounds/Hit_Hurt_001.wav')
Death_sound = pygame.mixer.Sound('Sounds/Death_Song.wav')
enemyHit_sound = pygame.mixer.Sound('Sounds/Explosion_001.wav')
itemGet_sound = pygame.mixer.Sound('Sounds/Pickup_Coin.wav')

def jump():
    pygame.mixer.Sound.play(jump_sound)

def attack():
    pygame.mixer.Sound.play(attack_sound)            
##################################################
    
def main():

    global item_global

    clock = pygame.time.Clock()
    L_SCROLL_X = 0
    L_SCROLL_Y = 0

    player = PLAYER(PLAYER_SIZE, PLAYER_POS, SCREEN_SIZE)
    last_hit = 0
    
    LEFT = False
    RIGHT = True
    MOVING = False
    ATTACK = False
    hit = False
    SCROLLING = False
    
    playerAnim = playerAnimate()
    healthUpdate = updateHUD()
    playerHearts = 3

## Detects and initializes external controllers
    
    joystick_count = pygame.joystick.get_count()

    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
        
##############################################
        
    while True:
        
        if player.active:
            player.update(level1.platform_group,level_fade.platform_group,
                          SCREEN_SIZE, L_SCROLL_X, level1)
            playerPos = player.getPos()
            
        DISPLAYSURF.fill(BG_COLOR)

## LEVEL scrolling ###########################

        if player.rect.x >= SCREEN_SIZE[0]- SCREEN_SIZE[0]//3:
            if L_SCROLL_X <= -1 * (level1.screenSize[0] - SCREEN_SIZE[0]):
                L_SCROLL_X = -1 * (level1.screenSize[0] - SCREEN_SIZE[0])
                SCROLLING = False
            else:                
                L_SCROLL_X -= player.Hspeed * player.run
                SCROLLING = True
                for t in level1.platform_group:
                    t.rect.x -= player.Hspeed * player.run
                for t in level_fade.platform_group:
                    t.rect.x -= player.Hspeed * player.run
                for t in level_1_fore.platform_group:
                    t.rect.x -= player.Hspeed * player.run
                for t in level_1_back.platform_group:
                    t.rect.x -= player.Hspeed * player.run
                for t in enemy_group:
                    t.rect.x -= player.Hspeed * player.run

            for i in item_group:        
                i.rect.x -= player.Hspeed * player.run

        elif player.rect.x <= SCREEN_SIZE[0]//3:
            if L_SCROLL_X >= 0:
                L_SCROLL_X = 0
                SCROLLING = False
            else:
                SCROLLING = True
                L_SCROLL_X -= player.Hspeed * player.run
                for t in level1.platform_group:
                    t.rect.x -= player.Hspeed * player.run
                    
                for t in level_fade.platform_group:
                    t.rect.x -= player.Hspeed * player.run
                    
                for t in level_1_fore.platform_group:
                    t.rect.x -= player.Hspeed * player.run
                    
                for t in level_1_back.platform_group:
                    t.rect.x -= player.Hspeed * player.run
                    
                for t in enemy_group:
                    t.rect.x -= player.Hspeed * player.run

                for i in item_group:        
                    i.rect.x -= player.Hspeed * player.run

##        if player.rect.y >= SCREEN_SIZE[1]- SCREEN_SIZE[1]//3 and player.Vspeed > 0:
##            if L_SCROLL_Y <= -1 * (level1.screenSize[1] - SCREEN_SIZE[1]):
##                L_SCROLL_Y = -1 * (level1.screenSize[1] - SCREEN_SIZE[1])
##            else:                
##                L_SCROLL_Y -= player.Vspeed
##                for t in level1.platform_group:
##                    t.rect.y -= player.Vspeed
##
##        elif player.rect.y <= SCREEN_SIZE[1]//3 and player.Vspeed < 0 :
##            if L_SCROLL_Y >= 0:
##                L_SCROLL_Y = 0
##            else:
##                L_SCROLL_Y -= player.Vspeed
##                for t in level1.platform_group:
##                    t.rect.y -= player.Vspeed

        
        level_1_back.platform_group.draw(DISPLAYSURF)
        

##############################################
        
        draw_bullets(RIGHT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

## joystick controls:
            if event.type == pygame.JOYHATMOTION:
                
                if joystick.get_hat(0)[0] == 1:
                    player.move_right()
                    MOVING = True
                    RIGHT = True
                    player.right = True
                    LEFT = False
                    player.left = False
                    
                elif joystick.get_hat(0)[0] == -1:
                    player.move_left()
                    MOVING = True
                    LEFT = True
                    player.left = True
                    RIGHT = False
                    player.right = False
                    
                elif joystick.get_hat(0)[0] == 0:
                    player.stop_move()
                    MOVING = False
                                    
            if event.type == pygame.JOYBUTTONDOWN:
                
                if event.button == 0:                    
                    if player.jumps > 0:
                        jump()
                    player.jump()
                    
                if event.button == 4:
                    player.player_run()
                    player.running = True
######
                if event.button == 2:# 1 B, 3 Y, 4 LB, 2 A
                    attack()
                    make_bullet(player,RIGHT)                    
                    ATTACK = True
######
                if event.button == 6: # 6 Back button
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.JOYBUTTONUP:
                
                if event.button == 4:
                    player.stop_run()
                    player.running = False
                if event.button == 2:
                    ATTACK = False
                
  
## keyboard controls:
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_LEFT:
                    player.move_left()
                    RIGHT = False
                    player.right = False
                    LEFT = True
                    player.left = True
                    MOVING = True

                if event.key == pygame.K_RIGHT:
                    player.move_right()                    
                    LEFT = False
                    player.left = False
                    RIGHT = True
                    player.right = True
                    MOVING = True

                if event.key == pygame.K_SPACE:                    
                    if player.jumps > 0:
                        jump()                    
                    player.jump()                    
                    
                if event.key == pygame.K_z:
                    attack()
                    make_bullet(player,RIGHT)                    
                    ATTACK = True                    

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                
                if event.key == pygame.K_x:
                    player.player_run()
                    player.running = True                

            if event.type == pygame.KEYUP:
                
                if event.key == pygame.K_LEFT and player.Hspeed < 0:
                    player.stop_move()
                    MOVING = False
                if event.key == pygame.K_RIGHT and player.Hspeed > 0:
                    player.stop_move()
                    MOVING = False

                if event.key == pygame.K_z:
                    ATTACK = False                
                    
                if event.key == pygame.K_x:
                    player.stop_run()
                    player.running = False
                    

###### player health pickup ####################
        if player.itemGet(item_group) > 0:
            if playerHearts < 3:
                playerHearts += 1
                item_group.active = False
            itemGet_sound.play()

        # Item Gravity
        for i in item_group:       
            i.update(level1.platform_group,level_fade.platform_group)
            if i.rect.top >= 800:
                item_group.remove(i)                
        
        ## Death check
        if playerHearts <= 0:
            player.active = False
            pygame.mixer.music.stop()
            Death_sound.play()           
        
        if player.rect.top >= 800:
            playerHearts = 0
        
            
## Player animation ##############################
        if player.active:
            playerAnim.playerAnim(DISPLAYSURF,playerPos,MOVING,hit,LEFT,RIGHT,ATTACK,player.getGrounded(),player.getVSpeed())
            hit = False


## Enemy hit detection ###########################
        p_hit_list = pygame.sprite.spritecollide(player, enemy_group, False)
        if len(p_hit_list) > 0 and last_hit == 0:
            playerHearts -= 1
            hit = True
            pygame.mixer.Sound.play(playerHit_sound)
            last_hit = 25
        last_hit -= 1
        if last_hit <=0:
            last_hit = 0
#######################################################################
        
        level_fade.platform_group.draw(DISPLAYSURF)
        level1.platform_group.draw(DISPLAYSURF)
        level_1_fore.platform_group.draw(DISPLAYSURF)
        DISPLAYSURF.blit(level_1_fore.Surf,(L_SCROLL_X,L_SCROLL_Y))

        for t in enemy_group:
            t.update(DISPLAYSURF, player.getPos(),bullet_group, (player.Hspeed * player.run),SCROLLING)
            if t.health <= 0:
                if random.randint(0,1) == 0:
                    make_healthItem(t.rect.x,t.rect.y)
                enemyHit_sound.play()
                enemy_group.remove(t)
                
        for t in level_fade.platform_group:
            t.update(bullet_group, level_fade.platform_group)

## Health HUD #####################################            
        healthUpdate.update(playerHearts,DISPLAYSURF)
        
        clock.tick(60)
        pygame.display.update()


if __name__ == "__main__": main()




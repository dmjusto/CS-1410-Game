## playerAnimation.py
## Onyx Games group project
## EAE 1410 Spring '17

import pygame, pyganim

class playerAnimate(object):

##    animTypes = 'run jump idle hurt run_shoot jump_shoot idle_shoot left_run left_jump left_idle left_idle_shoot left_run_shoot left_jump_shoot'.split()
##    animObjs = {}
##    imagesAndDurations = []

    def __init__(self):
        self.animTypes = 'run jump idle hurt run_shoot jump_shoot idle_shoot left_run left_jump left_idle left_idle_shoot left_run_shoot left_jump_shoot'.split()
        self.animObjs = {}
        for animType in self.animTypes:
            if animType[0:1] == 'j':
                imagesAndDurations = [('Sprites/player/player_%s.png' % (animType),1.0)]
                
            elif animType[0:1] == 'r':
                imagesAndDurations = [('Sprites/player/player_%s_%s.png' % (animType, str(num).rjust(1,'0')),
                                       0.1) for num in range(4)]
                
            elif animType == 'idle':
                imagesAndDurations = [('Sprites/player/player_idle0.png' ,4.5),
                                      ('Sprites/player/player_idle1.png' ,0.1)]
            elif animType[0:1] == 'i':
                imagesAndDurations = [('Sprites/player/player_idle_shoot.png' ,1.0)]

            elif animType[0:1] == 'hurt':
                imagesAndDurations = [('Sprites/player/player_hurt.png' ,1.0)]
                
                
            else:
                pass
                
            self.animObjs[animType] = pyganim.PygAnimation(imagesAndDurations)

        self.animObjs['left_run'] = self.animObjs['run'].getCopy()
        self.animObjs['left_run'].flip(True, False)
        self.animObjs['left_run'].makeTransformsPermanent()

        self.animObjs['left_hurt'] = self.animObjs['hurt'].getCopy()
        self.animObjs['left_hurt'].flip(True, False)
        self.animObjs['left_hurt'].makeTransformsPermanent()

        self.animObjs['left_idle'] = self.animObjs['idle'].getCopy()
        self.animObjs['left_idle'].flip(True, False)
        self.animObjs['left_idle'].makeTransformsPermanent()

        self.animObjs['left_jump'] = self.animObjs['jump'].getCopy()
        self.animObjs['left_jump'].flip(True, False)
        self.animObjs['left_jump'].makeTransformsPermanent()

        self.animObjs['left_jump_shoot'] = self.animObjs['jump_shoot'].getCopy()
        self.animObjs['left_jump_shoot'].flip(True, False)
        self.animObjs['left_jump_shoot'].makeTransformsPermanent()

        self.animObjs['left_run_shoot'] = self.animObjs['run_shoot'].getCopy()
        self.animObjs['left_run_shoot'].flip(True, False)
        self.animObjs['left_run_shoot'].makeTransformsPermanent()

        self.animObjs['left_idle_shoot'] = self.animObjs['idle_shoot'].getCopy()
        self.animObjs['left_idle_shoot'].flip(True, False)
        self.animObjs['left_idle_shoot'].makeTransformsPermanent()

        self.playerConductor = pyganim.PygConductor(self.animObjs) # animation blend tree

    def playerAnim(self, surf, pos, moving, hit, left, right, attack, grounded, vspeed):

        if not hit:
                self.playerConductor.play()
                
        if hit:
            moving = False
            hit = False
            left = False
            right = False
            attack = False
            grounded = False
            vspeed = 0
            if left:                            
                self.animObjs['left_hurt'].blit(surf, pos)
##                hit = False                    

            elif right:                
                self.animObjs['hurt'].blit(surf, pos)
##                hit = False         
        
        elif vspeed > 1:
            
            if attack == False:
                if right == True:
                    self.animObjs['jump'].blit(surf, pos)
                    
                elif left == True:
                    self.animObjs['left_jump'].blit(surf, pos)

            elif attack == True:
                if right == True:
                    self.animObjs['jump_shoot'].blit(surf, pos)
                    
                elif left == True:
                    self.animObjs['left_jump_shoot'].blit(surf, pos)
                    
        elif moving == True:            
            
            if grounded == True:

                if attack == False:
                    if right == True:
                        self.animObjs['run'].blit(surf, pos)
                        
                    elif left == True:
                        self.animObjs['left_run'].blit(surf, pos)

                elif attack == True:
                    if right == True:
                        self.animObjs['run_shoot'].blit(surf, pos)
                        
                    elif left == True:
                        self.animObjs['left_run_shoot'].blit(surf, pos)

            elif vspeed != 0:

                if attack == False:
                    if right == True:
                        self.animObjs['jump'].blit(surf, pos)
                        
                    elif left == True:
                        self.animObjs['left_jump'].blit(surf, pos)

                elif attack == True:
                    if right == True:
                        self.animObjs['jump_shoot'].blit(surf, pos)
                        
                    elif left == True:
                        self.animObjs['left_jump_shoot'].blit(surf, pos)
                    
        elif moving == False:

            if grounded == True:

                if attack == False:
                    if right == True:
                        self.animObjs['idle'].blit(surf, pos)

                    elif left == True:
                        self.animObjs['left_idle'].blit(surf, pos)

                elif attack == True:
                    if right == True:
                        self.animObjs['idle_shoot'].blit(surf, pos)

                    elif left == True:
                        self.animObjs['left_idle_shoot'].blit(surf, pos)

            elif vspeed != 0:

                if attack == False:
                    if right == True:
                        self.animObjs['jump'].blit(surf, pos)
                        
                    elif left == True:
                        self.animObjs['left_jump'].blit(surf, pos)

                elif attack == True:
                    if right == True:
                        self.animObjs['jump_shoot'].blit(surf, pos)
                        
                    elif left == True:
                        self.animObjs['left_jump_shoot'].blit(surf, pos)



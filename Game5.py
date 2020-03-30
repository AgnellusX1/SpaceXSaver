import pygame
import random
import os
pygame.init()

screen_width=900
screen_height=500
window=pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("Star Trek Discovery")

                                                            # Loading Images
bg = pygame.image.load('sky.png')
bg = pygame.transform.scale(bg, (screen_width,screen_height))
falcon1 = pygame.image.load('falcon.png')
falcon1 = pygame.transform.scale(falcon1,(150,100))
weapon1 = pygame.image.load('mis1.png')
weapon1 = pygame.transform.scale(weapon1,(10,20))
targetx = pygame.image.load('fire.png')
targetx = pygame.transform.scale(targetx,(25,50))

class rocks(pygame.sprite.Sprite):
    def __init__(self,location):
        pygame.sprite.Sprite.__init__(self)
        self.frame = window
        self.rect = self.frame.get_rect()

    def moveRocks(self,window):


def collide()


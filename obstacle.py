import pygame
import random

from pygame import image

class BigCactus():
    def __init__(self,image1,image2):
        self.type = random.randint(0,1)
        self.image1 = image1
        self.image1_rect = self.image1.get_rect()
        self.image1_rect.x = 843
        self.image1_rect.y = 0

        self.image2 = image2
        self.image2_rect = self.image2.get_rect()
        self.image2_rect.x = 843
        self.image2_rect.y = 0

    def update1(self):
        self.image1_rect.x -= 6
        
        
    def update2(self,screen):
        self.image2_rect.x -= 6
        

    

        


        

    



        

 

        


        
        




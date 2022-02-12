

import pygame, sys, random

from pygame import image

from dino import Dino
from obstacle import BigCactus
from sounds import Sounds


pygame.init()


sounds = Sounds()
dino = Dino()
global obstacles

image1 = pygame.image.load("bigcactus1.png")



fps = 0
screen = pygame.display.set_mode((843,316))




background = pygame.image.load("19142a0241a00213209951e4f1724cd8 (1).jpg")
ground = pygame.image.load("ground.png")
ground_x = 0
game_speed = 10
name = pygame.display.set_caption("DinoDino")
bc1 = pygame.image.load("bigcactus1.png")
bc2 = pygame.image.load("bigcactus2.png")
sc1 = pygame.image.load("smallcactus1.png")
sc2 = pygame.image.load("smallcactus2.png")

points = 0
font = pygame.font.Font("freesansbold.ttf",20)

def score():
    global points, game_speed
    points += 1
    if points % 100 == 0:
        game_speed += 1
        if points % 500 == 0:
            sounds.play("beep")
        
    
        


    text = font.render("Points: "+str(points),True,(0,0,0))
    textRect = text.get_rect()
    textRect.center = (80,30)
    screen.blit(text,textRect)







class Obstacle:
    def __init__(self,image,type):
        self.image = image
        self.type = type
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(910,1000)
        


    def update(self)           :
        self.rect.x -= game_speed
        if self.rect.x < -843:
            obstacles.pop()

    def draw(self,screen):
        screen.blit(self.image,self.rect)





class SmallCactus(Obstacle):
    def __init__(self,image):
        self.type = random.randint(0,1)

        super().__init__(image,self.type)
        
        self.rect.y = 0
        
        


class BigCactus(Obstacle):
    def __init__(self,image):
        self.type = random.randint(0,1)

        super().__init__(image,self.type)
        
        self.rect.y = 0
        

obstacles = []

    

        

while True:
    key = pygame.key.get_pressed()

    if dino.jump is False and key[pygame.K_SPACE]:
        dino.jump = True

    if dino.jump is True:
        dino.apply_gravity(screen)



    
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            pygame.quit()
            sys.exit()

    ground_x -= game_speed

    screen.blit(background,(0,0))
    screen.blit(dino.dino,(dino.dino_rect))
    
    
    screen.blit(ground,(ground_x,0))
    screen.blit(ground,(ground_x+843,0))

    


    
    if len(obstacles) == 0:
        if random.randint(0,1) == 0:
            obstacles.append(Obstacle(bc1,0))
            obstacles.append(Obstacle(bc2,0))
            
            

        elif random.randint(0,1) == 1:
            obstacles.append(Obstacle(sc1,1))
            


    for obstacle in obstacles:
        obstacle.draw(screen)
        obstacle.update()

        



        
        
    


    if ground_x <= -843:
        ground_x = 0

    
    score()
    
    clock = pygame.time.Clock()
    clock.tick(fps)
    
    
    pygame.display.update()

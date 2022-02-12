import pygame

class Dino(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.jump = False
        self.gravity = 4
        self.velocity = 14
        self.dino = pygame.image.load("dino.png")
        pygame.transform.scale(self.dino,(20,20))
        self.dino_rect = self.dino.get_rect()
        self.dino_rect.x = -300
        self.dino_rect.y = 108

    def apply_gravity(self,screen):
        self.dino_rect.y -= self.velocity
       
        self.velocity -= 1

        if self.velocity < -14:
            self.jump = False
            self.velocity = 14

    



        
    

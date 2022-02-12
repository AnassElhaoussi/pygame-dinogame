import pygame

class Sounds:
    def __init__(self):
       self.sounds = {
        'beep': pygame.mixer.Sound("beep.wav")
        }

    def play(self,name):
        self.sounds[name].play()


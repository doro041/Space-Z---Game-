import pygame
import random

WHITE = (255,255,255)

class Aliens(pygame.sprite.Sprite):
   def __init__(self):
        super().__init__()
        self.x = 1100 #the x coordinate 
        self.y = random.randint(200, 750) #random movement of y
        self.image= pygame.image.load('/home/dolora/Downloads/DoroteyaStoyanova-Game/media/roadster.png')
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect() 
        self.rect.center = (self.x,self.y)
        
        
   def move(self):
       self.x -= random.randint(5,10) #random speed 
       self.rect.center = (self.x,self.y) 
 
   def distance(self, other):
       return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

        

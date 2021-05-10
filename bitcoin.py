import pygame
import random
import math

class Bitcoin(pygame.sprite.Sprite):
    def __init__(self,ship):
        super().__init__()
        self.ship = ship
        self.x = ship.rect.right #the bitcoins move with the ship
        self.y = ship.rect.centery #they move with the ship and +45 helps with the shooting
        self.image = pygame.image.load('/home/dolora/Downloads/DoroteyaStoyanova-Game/media/bitcoin.png')
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,self.y)
        self.type = "bitcoin"

 

    def update(self): # this is how it moves
        self.rect.x += 25
        if self.rect.right >= 1200:
            self.kill()
                
class Supercoin(Bitcoin):
    def __init__(self,ship):
        pygame.sprite.Sprite.__init__(self)
        self.ship = ship
        self.x = self.ship.rect.right 
        self.y = self.ship.rect.centery
        self.image = pygame.image.load('/home/dolora/Downloads/DoroteyaStoyanova-Game/media/bitcoin.png')
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,self.y) 
        self.angle_change() #calling the function 
        self.speed = 25 #this is the speed
        self.collission_borders = False #collission of borders is not True 
        
    def collission(self): #check borders 
        if self.rect.x <= 0 : #left side 
           self.collission_borders = True #right side 
        elif self.rect.x >= 1200:
           self.collission_borders = True  #up
        elif self.rect.y <= 0:
           self.collission_borders = True 
        elif self.rect.y >= 750:
           self.collission_borders = True         #down
        
 
    def angle_change(self): #change of angle of the supercoin and its 
        # Convert angle in degrees to radians.
        self.angle = random.randint (0,359) #angle can be anything between 0 and 359
        self.angle_rad = math.radians(self.angle) #change it to radians 

        
    
    def update(self): #how the supercoin moves
        self.rect.centerx += -self.speed * math.sin(self.angle_rad) #this is for the x coordinate
        self.rect.centery += self.speed * math.cos(self.angle_rad) #this is for the y coordinate
        self.collission()
        if self.collission_borders: #checking the borders 
            self.kill() #if borders are present - kill the supercoin
            
        
        
        


import pygame

FPS = 60
VELOCITY = 5

#create class Ship
class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Load the image of a ghost and set it as the image for this sprite
        self.image = pygame.image.load('/home/dolora/Downloads/DoroteyaStoyanova-Game/media/starship.png')
        self.rect = self.image.get_rect()
        # Handle the black background of the sprite (so we don't see it)
        self.image.set_colorkey((0, 0, 0))
        # Get the sprite's rect - and set its location
        self.x = 200 
        self.y = 750/2
        self.dx = 0
        self.dy = 0
        self.fire = False #firing = false - this is the beginning of the function 
        self.damage = 0 #defining the damage to 0
        self.rect.center = (self.x, self.y)
        self.mining = 0 #mining of the bitcoin
        self.chance = 0 #chance for a supercoin or a bitcoin 
 
    def up(self): #borders 
        if self.y >= 20:
            self.y -= 5
            self.rect.center = (self.x, self.y)

    def down(self):
        if self.y <= 730:
            self.y += 5
            self.rect.center = (self.x, self.y)

    def right(self):
        if self.x <= 1100:
            self.x += 5
            self.rect.center = (self.x, self.y)

    def left(self):
        if self.x >= 20:
            self.x -= 5
            self.rect.center = (self.x, self.y)
#firing function
    def fire(self):
       self.fire = True     

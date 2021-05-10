import sys
import pygame
from bitcoin import Bitcoin,Supercoin
import random

pygame.font.init() 

WHITE = (255, 255, 255)



def check_events(screen, ship, sprites,bitcoins):
    """Respond to key presses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # Move ship right.
                ship.right()
            elif event.key == pygame.K_LEFT:
                # Move ship left.
                ship.left()
            elif event.key == pygame.K_q:
                # Move ship up.
                ship.up()
            elif event.key == pygame.K_a:
                # Move ship down.
                ship.down()
            elif event.key == pygame.K_SPACE: # space is connected to the bitcoin mining 
                if ship.mining == 100: #if ship mining is 100 
                    ship.mining = 0
                    ship.fire = True   #ship can fire 
                    ship.chance = random.randint(1,2) 
                    #randomise the chance so as to have 50%chance
                    print(ship.chance)
                    if ship.chance == 1 :#chance 50% for bitcoin 
                           
                #when bitcoin mining is 100 : the bitcoin state is ready and the ship is ready to shoot
                         new_btc = Bitcoin(ship)#add new bitcoin if 1
                         bitcoins.add(new_btc)
                         sprites.add(bitcoins)
                    elif ship.chance == 2: #supercoin if 2 
                        supercoin = Supercoin(ship) #add new supercoin
                        bitcoins.add(supercoin)     
                        sprites.add(supercoin)
                       
                   
                 
                    
                   
            # ANY OTHER KEY OPTIONS GO HERE


def show_damage(damage,font,screen): #print on the screen the damage
    score = font.render(("%03d" % damage), True, (255, 0, 0))
    screen.blit(score, (95, 15))


def lives(lives,font,screen):  #print on the screen the lives
    score = font.render(("%03d" % lives), True, (255, 0, 0))
    screen.blit(score, (235, 13))


def mining_count(ship,font,screen): #print on the screen the mining 
    if ship.mining < 100:
        ship.mining += 1 #mining is incremented by 1 per the loop 
        
        score = font.render(str(ship.mining), True, (255, 0, 0))
        screen.blit(score, (333, 38))
    elif ship.mining == 100:
        score = font.render(str(ship.mining), True, (255, 0, 0))
        screen.blit(score, (333, 38))
        

def score(screen,font,score,ai_settings): #print on the screen the score 
    score = font.render(str(ai_settings.score),True,(255,0,0))
    screen.blit(score,(90,40))


def update_screen(sprites, ai_settings, screen, ship,bitcoins): 
    """Update sprites & messages on the screen."""
    rects = sprites.draw(screen)
    font = pygame.font.Font('freesansbold.ttf',18)

    
  

    
    # If damage reaches 100%, display CRASHED message
    if ship.damage ==100:
      over_font = pygame.font.Font('freesansbold.ttf',65)
      over_text = over_font.render("You have crashed",True,(255,255,255))
      screen.blit(over_text,(330,750/2))
      
       # CODE GOES HERE
       #create the classes
    screen.blit(ai_settings.screen_backgrnd,pygame.Rect(0,0,ai_settings.screen_width,ai_settings.screen_height))
    lives(ai_settings.lives,font,screen)
    show_damage(ship.damage,font,screen)
    mining_count(ship,font,screen)
    score(screen,font,score,ai_settings)
     # Update the background region.
    pygame.display.update(rects)


#calling all the instances 
    
    
    

              

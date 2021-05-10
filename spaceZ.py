#documentation : 
#Doroteya Stoyanova's code 
#I did most of the things by trial and error which is not the most efficient thing to do but I believe that if the code is somehow in a working state - this shows effort !
import sys
import pygame
import random 
import math
# COMPLETE FILE PROVIDED IN STARTER CODE
from settings import Settings

# PARTIAL FILE PROVIDED IN STARTER CODE
import game_functions as gf

# IMPORT OTHER FILES/CLASSES HERE AS REQUIRED
from ship import Ship
from aliens import Aliens
from bitcoin import Bitcoin
from bitcoin import Supercoin



def run_game():
  # Initialize pygame, settings and screen object.
  pygame.init()

  # Set keys to repeat if held down.
  pygame.key.set_repeat(5, 5)

  # Create settings object containing game settings
  ai_settings = Settings()

  # Create the main game screen
  screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
  screen.blit(ai_settings.screen_backgrnd, [0, 0])

  # Create a main window caption
  pygame.display.set_caption("Space Z - Mars Flight")

  while ai_settings.lives > 0:
    # * CODE TO CREATE SPRITES/GROUPS GOES HERE *
    sprites = pygame.sprite.Group()
    ship = Ship()
    sprites.add(ship)
    aliens2 = pygame.sprite.Group()
    for i in range(20):
      alien = Aliens()
      sprites.add(alien) 
      aliens2.add(alien) 
    bitcoins = pygame.sprite.Group()

    # Refresh the background
    sprites.clear(screen, ai_settings.screen_backgrnd)

    # Start the main loop for the game.
    while ship.damage<100:
      # Watch for keyboard events
      gf.check_events(screen, ship,sprites,bitcoins)
      # Tell all the sprites to update their status
      sprites.update()
      sprites.clear(screen, ai_settings.screen_backgrnd)
      sprites.draw(screen)
      pygame.display.flip()
      #creating the aliens
      for i in range(20): #if they are 20 
        aliens2.sprites()[i].move() #they move 
        sprites.clear(screen, ai_settings.screen_backgrnd)
        distance = (math.sqrt(math.pow(ship.x - aliens2.sprites()[i].x,2) + (math.pow(ship.y-aliens2.sprites()[i].y,2)))) #this is their distance
        if distance < 20: #if distance is less than 20 
          aliens2.sprites()[i].x = 1200
          aliens2.sprites()[i].y = random.randint(50,750)
          aliens2.sprites()[i].rect.center= (aliens2.sprites()[i].x,aliens2.sprites()[i].y) 
          ship.damage +=10 # the colission is detected and there is +10 damage
          ai_settings.boom_sound.play()        #the boom sound plays  
        if aliens2.sprites()[i].x< 0:
            aliens2.sprites()[i].x = 1200
            aliens2.sprites()[i].y = random.randint(50, 750)
            aliens2.sprites()[i].rect.center = (aliens2.sprites()[i].x,aliens2.sprites()[i].y)    
      #I decided to use the Groups collission for the interaction between bitcoins and between roadsters :
      #the bitcoins in the group update or move 
      bitcoins.update() 
      #.values())[0]: #used this thing for detecting the values but no more it being used
      if pygame.sprite.groupcollide(bitcoins,aliens2,False,False): #checked wether  the pygame collission works between the bitcoin and the alien - at first none of them are killed
        collide_dict = pygame.sprite.groupcollide(bitcoins,aliens2,False,True) #this function kills the aliens when collission is detected but not the bitcoins
#for supercoin in bitcoins:
        for i in collide_dict:
          if not hasattr(i,'angle_change'): #this checks whether it is a bitcoin or a supercoin = in this regard the bitcoin
            
           
            ai_settings.score += 10 #the score goes +10 
            ai_settings.boom_sound.play()
            i.kill() #kill bitcoin
            # * ANY OTHER MAIN GAME CODE GOES HERE *
          if hasattr(i, 'angle_change'): #this checks whether it's a supercoin
            i.angle_change() #angle is being changed to radius 
            ai_settings.score += 10 #the score goes +10 - the reason I used this method is because I had  an error where if I kill 2 roadsters with 1 bitcoin it gives me an error 
            ai_settings.boom_sound.play()
        for j in list(collide_dict.values())[0]:
            new_alien = Aliens() #creating a new alien
            new_alien.add(sprites,aliens2) #new alien is added to the aliens' group
          
            
            
      sprites.draw(screen)
      pygame.display.flip()
      # Now update the sprites, etc. on the screen
      gf.update_screen(sprites, ai_settings, screen, ship,bitcoins)
                
      if ship.damage == 100: #checking for damage
        over_font= pygame.font.Font("freesansbold.ttf",65)
        over_text = over_font.render("You have crashed",True,(255,255,255))
        gf.update_screen(sprites,ai_settings,screen,ship,bitcoins)
        screen.blit(over_text,(330,375))
        pygame.display.update()
        
            

      

      # Wait for a keypress to continue
    null_event = pygame.event.wait()
    screen.blit(ai_settings.screen_backgrnd,pygame.Rect(330,375,800,100),pygame.Rect(330,375,800,100))
    sprites.clear(screen, ai_settings.screen_backgrnd)
    # Remove a life
    ai_settings.lives -= 1
    if  ai_settings.lives == 0: #if 0 lives 
          pygame.display.quit()
          pygame.quit()
          sys.exit() #exit the screen
        

    # GAME ENDS


# Call the main method to start the game
run_game()

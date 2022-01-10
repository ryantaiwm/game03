
import pygame 
import sys 
  
  
# initializing the constructor 
pygame.init() 
  
# screen resolution 
res = (720,720) 
  
# opens up a window 
screen = pygame.display.set_mode(res) 
  
# white color 
color = (255,255,255) 
  
# light shade of the button 
color_light = (170,170,170) 
  
# dark shade of the button 
color_dark = (100,100,100) 
color_black = (255,255,255)
color_blue = (0,0,128)
  
# stores the width of the 
# screen into a variable 
width = screen.get_width() 
  
# stores the height of the 
# screen into a variable 
height = screen.get_height() 
  
# defining a font 
smallfont = pygame.font.SysFont('Corbel',35) 
  
# rendering a text written in 
# this font 
text = smallfont.render('Exit' , True , color)
TextNew = smallfont.render('New Game', True, color)
TextContinue = smallfont.render('Continue', True, color) 
  
while True: 
      
    for ev in pygame.event.get(): 
          
        if ev.type == pygame.QUIT: 
            pygame.quit() 
              
        #checks if a mouse is clicked 
        if ev.type == pygame.MOUSEBUTTONDOWN: 
              
            #if the mouse is clicked on the 
            # button the game is terminated 
            if 2 <= mouse[0] <= 2+140 and 2 <= mouse[1] <= 40: 
                pygame.quit() 
                  
    # fills the screen with a color 
    screen.fill((60,25,60)) 
      
    # stores the (x,y) coordinates into 
    # the variable as a tuple 
    mouse = pygame.mouse.get_pos() 
      
    # if mouse is hovered on a button it 
    # changes to lighter shade 
    pygame.draw.rect(screen,color_blue,[0,0,width,40])
    if 2 <= mouse[0] <= 2+140 and 2 <= mouse[1] <= 2+40: 
        pygame.draw.rect(screen,color_light,[2,2,140,40]) 
          
    else: 
        pygame.draw.rect(screen,color_dark,[2,2,140,40]) 
      
    # superimposing the text onto our button 
    screen.blit(text , (2+50+300,2)) 
    screen.blit(TextNew, (2+50,2))
    screen.blit(TextContinue, (2+50+150,2))
      
    # updates the frames of the game 
    pygame.display.update() 
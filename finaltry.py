#!/usr/bin/python

import pygame
import random
import time
 
pygame.init()
 
display_width = 900
display_height = 600
 
red = (255,69,0)		# Orange = (255,69,0)
green = (25,200,25)
bright_red = (255,0,0)
bright_green = (0,255,0)

gift_width = 30
gift_height = 50
gamer_width = 70
gamer_height = 120

pause = False

final_font = None

# Load all the Images

fuelImg = pygame.image.load("data/fuel1.png")
game_bg = pygame.image.load("data/game_back.png")
bg = pygame.image.load("data/back.png")
gamerImg = pygame.image.load('data/img3.png')
gameIcon = pygame.image.load('data/Firefox_wallpaper.png')

# Set up the surface to display and Initialise the Clock to be used for Number of frames per second

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Dodge For Eternity!!!')
clock = pygame.time.Clock()
pygame.display.set_icon(gameIcon)

def music_stop():
    pygame.mixer.music.stop()

def music_start():
    pygame.mixer.music.load('sfx/Heroic Demise .mp3')
    pygame.mixer.music.play(-1)

def isOverlap(l1_x,l1_y,r1_x,r1_y,l2_x,l2_y,r2_x,r2_y):
    if(l1_x >= r2_x or l2_x >= r1_x):
	return False
    
    if(l1_y >= r2_y or l2_y >= r1_y):
	return False
    return True

def create_things(gifts_x,gifts_y):
    gameDisplay.blit(fuelImg,(gifts_x,gifts_y))
 
def score(count):
    font = pygame.font.SysFont(final_font, 50)
    text = font.render("Score: "+str(count), True, red)
    gameDisplay.blit(text,(0,0))
 
def rect_box(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
 
def gamer(x,y):
    gameDisplay.blit(gamerImg,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, (0,0,0))	# Black = (0,0,0)
    return textSurface, textSurface.get_rect()
 
def crash():
  
    largeText = pygame.font.SysFont(final_font,125)
    TextSurf, TextRect = text_objects("You Crashed", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    
    while True:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
		
                pygame.quit()
                quit()

        button("Play Again",150,450,190,75,green,bright_green,game_loop)
        button("Quit",550,450,125,75,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15) 

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
    smallText = pygame.font.SysFont(final_font,50)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
    
def quitgame():
    
    pygame.quit()
    quit()

def unpause():
    global pause
    pause = False  

def paused():

    largeText = pygame.font.SysFont(final_font,125)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    

    while pause:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
		
                pygame.quit()
                quit()

	    if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_q:
		    
		    quitgame()
		if event.key == pygame.K_c:
		    unpause()
                
        button("Continue",150,450,175,75,green,bright_green,unpause)
        button("Quit",550,450,125,75,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)   


def game_intro():

    intro = True

    music_start()

    gameDisplay.blit(bg, (0, 0))
    while intro:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
		
                pygame.quit()
                quit()

	    if event.type == pygame.KEYDOWN:
		
		if event.key == pygame.K_q:
		    
		    quitgame()
		if event.key == pygame.K_g:
		    
		    game_loop()
                
        #gameDisplay.fill((255,255,255))		# White = (255,255,255)
	gameDisplay.blit(bg, (0, 0))
        largeText = pygame.font.SysFont(final_font,100)
        TextSurf, TextRect = text_objects("DODGE FOR ETERNITY!!!", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

	largeText = pygame.font.SysFont(final_font,60)
        TextSurf, TextRect = text_objects("NIGESU - NEVER GIVE UP", largeText)
        TextRect.center = ((display_width/2),(100))
        gameDisplay.blit(TextSurf, TextRect)

	largeText = pygame.font.SysFont(final_font,25)
        TextSurf, TextRect = text_objects("m:Mute--u:Unmute--p:Pause--g:Go--q:Quit", largeText)
        TextRect.center = ((0.80*900),(25))
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!",150,450,125,75,green,bright_green,game_loop)
        button("Quit",550,450,125,75,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)
        
def game_loop():

    global pause

    first = True

    music_start()

    gift_x = random.randrange(100, display_width-100)
    gift_y = random.randrange(100, display_height-100)
    x_x = gift_x
    y_y = gift_y		
    create_things(gift_x,gift_y) 

    x = (display_width * 0.50)
    y = (display_height * 0.50)
 
    x_change = 0
    y_change = 0
 
    thing_startx_td = random.randrange(0, display_width)
    thing_starty_td = -200
    thing_hori_startx_lr = -200
    thing_hori_starty_lr = random.randrange(0, display_height)
    thing_startx_dt = random.randrange(0, display_width)
    thing_starty_dt = 1100
    thing_hori_startx_rl = 1100
    thing_hori_starty_rl = random.randrange(0, display_height)

    block_color_td = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))

    block_hori_color_lr = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))

    block_color_dt = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
  
    block_hori_color_rl  = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
 
    thing_speed = 6
    thing_width = 100
    thing_height = 100

    scored = 0

    gameExit = False
 
    while not gameExit:
 
        for event in pygame.event.get():
	    
            if event.type == pygame.QUIT:
                quitgame()
 
            if event.type == pygame.KEYDOWN:
		
		if event.key == pygame.K_q:
		    quitgame()
		if event.key == pygame.K_m:
		    music_stop()
		if event.key == pygame.K_u:
		    music_start()
		if event.key == pygame.K_p:
                    pause = True
                    paused()
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
		if event.key == pygame.K_UP:
		    y_change = -5
		if event.key == pygame.K_DOWN:
		    y_change = 5
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
		if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
		    y_change = 0
 
        #gameDisplay.fill((255,255,255))		#For White = (255,255,255)
	gameDisplay.blit(game_bg, (0, 0))
	
        rect_box(thing_startx_td, thing_starty_td, thing_width, thing_height, block_color_td)

	rect_box(thing_hori_startx_lr, thing_hori_starty_lr, thing_width, thing_height, block_hori_color_lr)

	thing_starty_td += thing_speed
	thing_hori_startx_lr += thing_speed
        
	x += x_change
	y += y_change
	gamer(x,y)

	create_things(x_x,y_y)	

	if (isOverlap(gift_x,gift_y,gift_x+gift_width,gift_y+gift_height,x,y,x + gamer_width,y + gamer_height)):	
		gift_x = random.randrange(125, display_width-125)
		gift_y = random.randrange(125, display_height-125)		
		create_things(gift_x,gift_y)
		x_x = gift_x
		y_y = gift_y
		scored += 2

	score(scored)
 
        if x > display_width - gamer_width or x < 0 or y > display_height - gamer_height or y < 0:
	    crash()
 
        if thing_starty_td > display_height:
            thing_starty_td = 0 - thing_height
            thing_startx_td = random.randrange(50,display_width-50)
            thing_speed += 0.05
            block_color_td = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))

	if thing_hori_startx_lr > display_width:
            thing_hori_starty_lr = random.randrange(50,display_height-50)
            thing_hori_startx_lr = 0 - thing_width
            thing_speed += 0.05
	    block_hori_color_lr = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))

	if thing_starty_dt < 0:
            thing_starty_dt = display_height + thing_height
            thing_startx_dt = random.randrange(50,display_width-50)
            thing_speed += 0.05
            block_color_dt = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))

	if thing_hori_startx_rl < 0:
            thing_hori_starty_rl = random.randrange(50,display_height-50)
            thing_hori_startx_rl = display_width + thing_width
            thing_speed += 0.05
	    block_hori_color_rl = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))	
	
	if(scored > 10):
	
	    rect_box(thing_startx_dt, thing_starty_dt, thing_width, thing_height, block_color_dt)
            rect_box(thing_hori_startx_rl, thing_hori_starty_rl, thing_width, thing_height, block_hori_color_rl)
	    if(first):
	        thing_speed = 5
		first = False
		
	    thing_starty_dt -= thing_speed
	    thing_hori_startx_rl -= thing_speed
	    
	
	if(isOverlap(thing_startx_td,thing_starty_td,thing_startx_td + thing_width,thing_starty_td + thing_height,x,y,x + gamer_width,y + gamer_height)):
		crash()

	if(isOverlap(thing_hori_startx_lr,thing_hori_starty_lr,thing_hori_startx_lr + thing_width,thing_hori_starty_lr + thing_height,x,y,x + gamer_width,y + gamer_height)):
		crash()

	if(isOverlap(thing_startx_dt,thing_starty_dt,thing_startx_dt + thing_width,thing_starty_dt + thing_height,x,y,x + gamer_width,y + gamer_height)):
		crash()

	if(isOverlap(thing_hori_startx_rl,thing_hori_starty_rl,thing_hori_startx_rl + thing_width,thing_hori_starty_rl + thing_height,x,y,x + gamer_width,y + gamer_height)):
		crash()

        
        pygame.display.update()
        clock.tick(60)

game_intro()
#game_loop()
pygame.quit()
quit()

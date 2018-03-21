 # Imports
import pygame
import intersects

# Initialize game engine
pygame.init()


# Window
WIDTH = 800
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
TITLE = "Cube Dudes: Great Escape!"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)


# Make a player
player1 =  [200, 150, 25, 25]
vel1 = [0, 0]
player1_speed = 5
score1 = 0

player2 =  [700, 500, 25, 25]
vel2 = [0, 0]
player2_speed = 5
score2 = 0

key1 = [750, 25, 25, 25]

keys = [key1]

# make walls
wall1 =  [200, 0, 600, 25]
wall2 =  [0, 0, 100, 25]
wall3 =  [200, 575, 600, 25]
wall4 =  [0, 575, 100, 25]
wall5 =  [100, 100, 25, 200]
wall6 = [550,50, 300, 25]
wall7 = [500, 100, 250, 25]
wall8 = [550, 150, 250, 25]
wall9 = [775, 0, 25, 175]
wall10 = [500, 0, 25, 500]
wall11 = [550, 250, 25, 225]
wall12 = [550, 200, 150, 25]
wall13 = [725, 200, 25, 150]
wall14 = [600, 250, 150, 25]
wall15 = [550, 350, 150, 25]
wall16 = [550, 300, 250, 25]
wall17 = [500, 200, 50, 25]


wallA = [600,400, 200, 25]
wallB = [600, 400, 25, 250]
wallC= [775, 400, 25, 250]
wallD = [775, 100, 25, 400]


walls = [wall1, wall2, wall3, wall4, wall5,
         wall6, wall7, wall8, wall9, wall10,
         wall11, wall12, wall13, wall14, wall15,
         wall16, wall17]


walls2 = [ wallA, wallB, wallC, wallD]

trap1 = [675, 500, 25, 250]

traps = [trap1]

# Make coins
coin1 = [300, 500, 25, 25]
coin2 = [400, 200, 25, 25]
coin3 = [150, 150, 25, 25]

coins = [coin1, coin2, coin3]



# Fonts
MY_FONT = pygame.font.Font(None, 50)


# stages
START = 0
PLAYING = 1
END = 2

def setup():
    global block_pos, block_vel, size, stage
    
    block_pos = [375, 275]
    block_vel = [0, 0]
    size = 50

    stage = START

'''
def wall_move(wall_vel, wall_speed):
    while stage == PLAYING:
        wall_vel[1] = wall_speed
'''    


# Game loop

setup()

win = False
done = False
keyget = False


while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:

            if stage == START:
                if event.key == pygame.K_SPACE:
                    stage = PLAYING
            
            elif stage == PLAYING:

                pressed = pygame.key.get_pressed()

                up1 = pressed[pygame.K_UP]
                down1 = pressed[pygame.K_DOWN]
                left1 = pressed[pygame.K_LEFT]
                right1 = pressed[pygame.K_RIGHT]

                up2 = pressed[pygame.K_w]
                down2 = pressed[pygame.K_s]
                left2 = pressed[pygame.K_a]
                right2 = pressed[pygame.K_d]

                
                if left1:
                    vel1[0] = -player1_speed
                elif right1:
                    vel1[0] = player1_speed
                else:
                    vel1[0] = 0
                
                
                if left2:
                    vel2[0] = -player2_speed
                elif right2:
                    vel2[0] = player2_speed
                else:
                    vel2[0] = 0

                
                if up1:
                    vel1[1] = -player1_speed
                elif down1:
                    vel1[1] = player1_speed
                else:
                    vel1[1] = 0
                
                
                if up2:
                    vel2[1] = -player2_speed
                elif down2:
                    vel2[1] = player2_speed
                else:
                    vel2[1] = 0


            elif stage == END:
                if event.key == pygame.K_SPACE:
                    setup()

                    
        
    # Game logic (Check for collisions, update points, etc.)
        
    if stage == PLAYING:
        ''' move the player in horizontal direction '''
        player1[0] += vel1[0]
        player2[0] += vel2[0]
        
        ''' move the player in vertical direction '''
        player1[1] += vel1[1]
        player2[1] += vel2[1]
        


        ''' resolve collisions horizontally '''
        for w in walls:
            if intersects.rect_rect(player1, w):        
                if vel1[0] > 0:
                    player1[0] = w[0] - player1[2]
                elif vel1[0] < 0:
                    player1[0] = w[0] + w[2]

            if intersects.rect_rect(player2, w):        
                if vel2[0] > 0:
                    player2[0] = w[0] - player2[2]
                elif vel2[0] < 0:
                    player2[0] = w[0] + w[2]
                    
        if not keyget:
            for w in walls2:
                if intersects.rect_rect(player1, w):        
                    if vel1[0] > 0:
                        player1[0] = w[0] - player1[2]
                    elif vel1[0] < 0:
                        player1[0] = w[0] + w[2]

                if intersects.rect_rect(player2, w):        
                    if vel2[0] > 0:
                        player2[0] = w[0] - player2[2]
                    elif vel2[0] < 0:
                        player2[0] = w[0] + w[2]
 


        ''' resolve collisions vertically '''
        for w in walls:
            if intersects.rect_rect(player1, w):                    
                if vel1[1] > 0:
                    player1[1] = w[1] - player1[3]
                elif vel1[1]< 0:
                    player1[1] = w[1] + w[3]


            if intersects.rect_rect(player2, w):                    
                if vel2[1] > 0:
                    player2[1] = w[1] - player2[3]
                elif vel2[1]< 0:
                    player2[1] = w[1] + w[3]
                    
        if not keyget:             
            for w in walls2:
                if intersects.rect_rect(player1, w):                    
                    if vel1[1] > 0:
                        player1[1] = w[1] - player1[3]
                    elif vel1[1]< 0:
                        player1[1] = w[1] + w[3]


                if intersects.rect_rect(player2, w):                    
                    if vel2[1] > 0:
                        player2[1] = w[1] - player2[3]
                    elif vel2[1]< 0:
                        player2[1] = w[1] + w[3]
                        
                
        for k in keys:
            if intersects.rect_rect(player1, k):
                keyget = True
            else:
                keyget = False 
                     
        ''' end game on wall collision '''
        '''
        if block_pos[0] < 0 or block_pos[0] > 950 or \
           block_pos[1] <  0 or block_pos[1] > 650:
            stage = END

        '''

        '''   
        wall_move(wall_vel, wall_speed)
        '''
    #''' here is where you should resolve player collisions with screen edges '''

    
    ''' get block edges (makes collision resolution easier to read) '''
     
    block_left1 = player1[0] 
    block_right1 = player1[0] + player1[2]
    block_top1 = player1[1]
    block_bottom1 = player1[1] + player1[3]

    block_left2 = player2[0] 
    block_right2 = player2[0] + player2[2]
    block_top2 = player2[1]
    block_bottom2 = player2[1] + player2[3]

    ''' if the block is moved completely off of the window, reposition it on the other side '''

    
    if block_left1 > WIDTH:
        player1[0] = 0 - player1[2]
        
    elif block_right1 < 0:
        player1[0] = WIDTH



    if block_left2 > WIDTH:
        player2[0] = 0 - player2[2]
        
    elif block_right2 < 0:
        player2[0] = WIDTH

       
    if block_bottom1 < 0:
        player1[1] = HEIGHT
        
    elif block_top1 > HEIGHT:
        player1[1] = 0 - player1[3]


    if block_bottom2 < 0:
        player1[1] = HEIGHT
        
    elif block_top2 > HEIGHT:
        player2[1] = 0 - player2[3]







    ''' get the coins '''
    hit_list = []

    for c in coins:
        if intersects.rect_rect(player1, c):
            hit_list.append(c)

        if intersects.rect_rect(player2, c):
            hit_list.append(c)
     
    hit_list = [c for c in coins if intersects.rect_rect(player1, c)]
    
    for hit in hit_list:
        coins.remove(hit)
        score1 += 1
        print("sound!")
        
    if len(coins) == 0:
        win = True

        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLACK)

    for k in keys:
        pygame.draw.rect(screen, GREEN, k)
    

    pygame.draw.rect(screen, RED, player1)    
    pygame.draw.rect(screen, BLUE, player2)


    for w in walls:
        pygame.draw.rect(screen, WHITE, w)
        
    if not keyget:
        walls2 = [ wallA, wallB, wallC, wallD]


        for a in walls2:
            pygame.draw.rect(screen, WHITE, a)
    if keyget:
        
        walls2 = []

        traps = [trap1]
        
        for t in traps:
            pygame.draw.rect(screen, GREEN, t)

    for c in coins:
        pygame.draw.rect(screen, YELLOW, c)
        
    if win:
        font = pygame.font.Font(None, 48)
        text = font.render("You Win!", 5, GREEN)
        screen.blit(text, [400, 200])


        
    ''' begin/end game text '''
    if stage == START:
        text1 = MY_FONT.render("Block", True, WHITE)
        text2 = MY_FONT.render("(Press SPACE to play.)", True, WHITE)
        screen.blit(text1, [350, 150])
        screen.blit(text2, [225, 200])
    elif stage == END:
        text1 = MY_FONT.render("Game Over", True, WHITE)
        text2 = MY_FONT.render("(Press SPACE to restart.)", True, WHITE)
        screen.blit(text1, [310, 150])
        screen.blit(text2, [210, 200])



    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()

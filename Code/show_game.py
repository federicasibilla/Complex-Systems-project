# -*- coding: utf-8 -*-

import numpy as np
import random
import math
import pygame

black = (0,0,0)
red = (255, 0 ,0)
green = (0, 255, 0)
white = (255, 255, 255)

# Falling ball game

# stage : a grid NxN      (0,0)----->(0,N-1)
#                           |
#                           |
#                           |
#                           ˇ
#                       (N-1,0)

# X balls of 1 pixel will fall one by one from the top of the grid to the 
# bottom. A platform of 3 pixels large is positioned at the bottom line and can
# move left or right. Each ball will be green or red with equal probability.
# The platform has to catch the green balls but not the red ones.

# inputs :  chromosome of length 2*(N-1)*(2*(N-1)+1) : rules to play
#           N : len of side of grid
#           lbd : paramter lambda
#           s : size of pod

# Chromosome structure
# g  g  g  g  .... g  g  g .... r r r r
# y1 y1 y1 y1 .... y2 y2 y2
# x1 x2 x3 x4 .... x1 x2 x3 
# with possible values -1 (move left) or 1 (move 1)
# should work also if we add 0 (stay still)

# output : average fitness of the chromosome after 100 balls

def falling_ball_game(rules, N, lbd, s):
    try:
        if N/2 == int(N/2) or s/2 == int(s/2):
            er = 1/0
    except:
        print('Error : N and s must be odd, not even !')
    else:
        # number of balls
        nb_balls = 100
        # size of chromosome
        n = len(rules)
        g = 0 # will be mean distance from green ball
        r = 0 # same for red
        nb_green = 0
        nb_red = 0
        catched_green = 0
        avoided_red = 0
        paused = True # useful bool to pause with space bar
        go = False # useful bool to go step by step with right-key
        running = True # useful bool to stop when closing the window
        
        global SCREEN, width, height
        height = 800
        width = 800
        speed = 5 # fps
        pygame.init()
        SCREEN = pygame.display.set_mode((width, height))
        SCREEN.fill(white)
        pygame.display.set_caption('Falling ball Game')
        
        # Set Clock and simulation speed
        clock = pygame.time.Clock()
        clock.tick(speed)
        
        for b in np.arange(nb_balls):
            if running:        
                # assign random color
                color = random.choice(['green', 'red'])
                # assign ball random horizontal position at the top
                x = random.choice(np.arange(N))
                y = 0
                # assign initial middle position of platform
                plat = math.floor(N/2)
                
                drawGrid(x, y, color, plat, N, s)
                message("catched green : " + str(catched_green) + "/" + str(nb_green)
                + "   avoided red : " + str(avoided_red) + "/" + str(nb_red)
                , black)
                pygame.display.update()
                
                # play ! iteration on the ball falling down line by line
                while y <= N-1 and running:
                    if not paused or go:
                        # evaluation of relative positions
                        dx = round(plat - x)
                        dy = round((N-1) - y)
                        if dy == 0:
                            # take distance to the platform and count balls
                            if color == 'green':
                                nb_green += 1
                                g += abs(dx)
                                if abs(dx) < s/2:
                                    catched_green += 1
                            else:
                                nb_red += 1
                                r += abs(dx)
                                if abs(dx) > s/2:
                                    avoided_red += 1
                            drawGrid(x, N-1, color, plat, N, s)
                            message("catched green : " + str(catched_green) + "/" + str(nb_green)
                            + "   avoided red : " + str(avoided_red) + "/" + str(nb_red)
                            , black)
                            pygame.display.update()
                            clock.tick(speed)
                            break
                        # find index i in chromosome
                        if color == 'green':
                            i = 0
                        else:
                            i = n/2
                        i += (dy-1)*(2*(N-1)+1)
                        i += dx + N-1
                        # take order from rule
                        rule = rules[round(i)]
                        # move left ?
                        if rule == -1:
                            if plat > s/2:
                                plat -= 1
                        # or move right ?
                        elif rule == 1:
                            if plat < (N-1)-s/2:
                                plat += 1  
                        drawGrid(x, y, color, plat, N, s)
                        message("catched green : " + str(catched_green) + "/" + str(nb_green)
                        + "   avoided red : " + str(avoided_red) + "/" + str(nb_red)
                        , black)
                        pygame.display.update()
                        clock.tick(speed)
                        y+=1
                    # Commands interaction
                    keys = pygame.key.get_pressed()  #checking pressed keys
                    if keys[pygame.K_UP]:
                      go = True
                    if keys[pygame.K_ESCAPE]:
                      running = False
                  
                    for event in pygame.event.get():
                      if event.type == pygame.QUIT:
                          running = False # quit by closing the window
                      if event.type == pygame.KEYDOWN:
                          if event.key == pygame.K_SPACE:
                              paused = not paused # pause and resume with spacebar
                          if event.key == pygame.K_RIGHT:
                              go = True
                    
        while running: # to close the window if last step has been reached
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            keys = pygame.key.get_pressed()  #checking pressed keys
            if keys[pygame.K_ESCAPE]:
                running = False
        pygame.quit()
        # normalize distances to number of balls of the right color
        g = g/nb_green
        r = r/nb_red
        # compute fitness with average distances
        f = 1/(1+np.exp(-lbd*((s/2) - g))) - 1/(1+np.exp(-lbd*((s/2) - r))) + 1
        return f
        

def drawGrid(x_ball, y_ball, color, plat , N, s):
    block_size = width/N
    SCREEN.fill(white)
    for i in range(0,N):
        for j in range(0, N):
            rect = pygame.Rect(i*block_size, j*block_size, block_size+1, 0.5*block_size)
            #pygame.draw.rect(SCREEN, white, rect, width=0)
            if x_ball == i and y_ball == j and color == 'green':
                #pygame.draw.rect(SCREEN, green, rect, width=0)
                pygame.draw.circle(SCREEN, green, ((i+0.5)*block_size,(j+0.5)*block_size), block_size/3)
            elif x_ball == i and y_ball == j:
                pygame.draw.circle(SCREEN, red, ((i+0.5)*block_size,(j+0.5)*block_size), block_size/3)
                #pygame.draw.rect(SCREEN, red, rect, width=0)
            if j == N-1 and i == plat:
                pygame.draw.rect(SCREEN, black, rect, width=0)
                for x in range(math.floor(s/2)+1):
                    rect1 = pygame.Rect((i-x)*block_size, j*block_size, block_size+1, 0.5*block_size)
                    rect2 = pygame.Rect((i+x)*block_size, j*block_size, block_size+1, 0.5*block_size)
                    pygame.draw.rect(SCREEN, black, rect1, width=0)
                    pygame.draw.rect(SCREEN, black, rect2, width=0)
                
def message(msg,color):
    font_style = pygame.font.SysFont("Helvetica", 42)
    text = font_style.render(msg, True, color)
    text_rect = text.get_rect(center=(width/2, height/45))
    SCREEN.blit(text, text_rect)

N = 9 # size of grid, must be odd /!\
s = 3 # length of pod, must be odd /!\
lbd = 0.5 # paramter lambda

test_rule = np.zeros(2*(N-1)*(2*(N-1)+1))
for i in np.arange(len(test_rule)):
    test_rule[i] = random.choice([-1, 1])

print(falling_ball_game(test_rule, N, lbd, s))
        
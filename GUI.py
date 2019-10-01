import pygame, sys
from pygame.locals import *

pygame.init()
def makeBoard(screen, gameBoard):
    for i in range(6):
        for j in range(7):
            if (gameBoard[i][j] == 0):
                pygame.draw.circle(screen,BLACK,(j * COLUMN_SIZE + COLUMN_SIZE//2, i * COLUMN_SIZE + COLUMN_SIZE//2), COLUMN_SIZE//2 - 5)
            elif (gameBoard[i][j] == 1):
                pygame.draw.circle(screen,YELLOW,(j * COLUMN_SIZE + COLUMN_SIZE//2, i * COLUMN_SIZE + COLUMN_SIZE//2), COLUMN_SIZE//2 - 5)
            elif (gameBoard[i][j] == 2):
                pygame.draw.circle(screen,RED,(j * COLUMN_SIZE + COLUMN_SIZE//2, i * COLUMN_SIZE + COLUMN_SIZE//2), COLUMN_SIZE//2 - 5)


def makeBackground(screen, gameBoard):
    screen.fill(BLUE)
    pygame.draw.rect(screen,WHITE,(700,0,200,600)) # menu bar
    makeBoard(screen, gameBoard)
    # Button 
    menuFont = pygame.font.Font("Aaargh.ttf", 20)
    # New Game Button
    pygame.draw.rect(screen,BLACK,(720,25,160,50))
    text = menuFont.render('New Game', True, WHITE, BLACK)
    textRect = text.get_rect()  
    textRect.center = (800, 50) 
    screen.blit(text, textRect)
    # Category Selection
    text = menuFont.render('Select Category:', True, BLACK, WHITE)
    textRect = text.get_rect()  
    textRect.center = (800, 100)
    screen.blit(text, textRect)
    # Button 1
    pygame.draw.rect(screen,BLACK,(720,125,160,50))
    text = menuFont.render('You vs Random', True, WHITE, BLACK)
    textRect = text.get_rect()  
    textRect.center = (800, 150) 
    screen.blit(text, textRect)
    # Button 2
    pygame.draw.rect(screen,BLACK,(720,200,160,50))
    text = menuFont.render('You vs AI', True, WHITE, BLACK)
    textRect = text.get_rect()  
    textRect.center = (800, 225) 
    screen.blit(text, textRect)
    # Button 3
    pygame.draw.rect(screen,BLACK,(720,275,160,50))
    text = menuFont.render('Random vs AI', True, WHITE, BLACK)
    textRect = text.get_rect()  
    textRect.center = (800, 300) 
    screen.blit(text, textRect)
    # Game Difficulty
    text = menuFont.render('Select Difficulty:', True, BLACK, WHITE)
    textRect = text.get_rect()  
    textRect.center = (800, 350)
    screen.blit(text, textRect)
    # Button 1
    pygame.draw.rect(screen,BLACK,(720,375,160,50))
    text = menuFont.render('1', True, WHITE, BLACK)
    textRect = text.get_rect()  
    textRect.center = (800, 400) 
    screen.blit(text, textRect)
    # Button 2
    pygame.draw.rect(screen,BLACK,(720,450,160,50))
    text = menuFont.render('2', True, WHITE, BLACK)
    textRect = text.get_rect()  
    textRect.center = (800, 475) 
    screen.blit(text, textRect)
    # Button 3
    pygame.draw.rect(screen,BLACK,(720,525,160,50))
    text = menuFont.render('3', True, WHITE, BLACK)
    textRect = text.get_rect()  
    textRect.center = (800, 550) 
    screen.blit(text, textRect)

#Constant
COLUMN_SIZE = 100
WHITE=(255,255,255)
RED = (255,0,0)
YELLOW = (255,255,0)
BLUE=(0,0,255)
BLACK  = (0,0,0)
#screen Initializer
gameBoard = [[0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,2,0],
            [0,0,0,0,0,2,0],
            [0,0,0,0,0,1,1],
            [0,0,0,0,0,1,2],]
screen=pygame.display.set_mode((9 * COLUMN_SIZE,6 * COLUMN_SIZE),0,32)
makeBackground(screen, gameBoard)

while True:
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            if position[0] <= 95 and position[0] >=5:
                print('Input Col 1')
            elif position[0] <= 195 and position[0] >=105:
                print('Input Col 2')
            elif position[0] <= 295 and position[0] >=205:
                print('Input Col 3')
            elif position[0] <= 395 and position[0] >=305:
                print('Input Col 4')
            elif position[0] <= 495 and position[0] >=405:
                print('Input Col 5')
            elif position[0] <= 595 and position[0] >=505:
                print('Input Col 6')
            elif position[0] <= 695 and position[0] >=605:
                print('Input Col 7')
            else: # Menu bar
                if position[1] >= 25 and position[1] <= 75:
                    print('New Game')
                if position[1] >= 125 and position[1] <= 175:
                    print('Category 1')
                if position[1] >= 200 and position[1] <= 250:
                    print('Category 2')
                if position[1] >= 275 and position[1] <= 325:
                    print('Category 3')
                if position[1] >= 375 and position[1] <= 425:
                    print('Difficulty 1')
                if position[1] >= 450 and position[1] <= 500:
                    print('Difficulty 2')
                if position[1] >= 525 and position[1] <= 575:
                    print('Difficulty 3')
        elif event.type==QUIT:
            pygame.quit()
            sys.exit()
    makeBoard(screen, gameBoard)
    pygame.display.update()
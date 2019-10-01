import pygame, sys
from pygame.locals import *
from main import gameEngine

def makeBoard(screen, gameBoard):
    for i in range(6):
        for j in range(7):
            if (gameBoard[i][j] == 0):
                pygame.draw.circle(screen,BLACK,(j * COLUMN_SIZE + COLUMN_SIZE//2, i * COLUMN_SIZE + COLUMN_SIZE//2), COLUMN_SIZE//2 - 5)
            elif (gameBoard[i][j] == 1):
                pygame.draw.circle(screen,YELLOW,(j * COLUMN_SIZE + COLUMN_SIZE//2, i * COLUMN_SIZE + COLUMN_SIZE//2), COLUMN_SIZE//2 - 5)
            elif (gameBoard[i][j] == 2):
                pygame.draw.circle(screen,RED,(j * COLUMN_SIZE + COLUMN_SIZE//2, i * COLUMN_SIZE + COLUMN_SIZE//2), COLUMN_SIZE//2 - 5)

def putPiece(gameBoard, input, category):
    if (not isInputNotValid(input, gameBoard)):
        gameEngine.updateBoard(PLAYER, input, gameBoard)
        if (category == 1):
            gameEngine.updateBoard(AI, gameEngine.randomizeMove(gameBoard), gameBoard)
        elif (category == 2):
            gameEngine.updateBoard(AI, gameEngine.minimaxAlphaBetaPruning(gameBoard, DEPTH, -999999, 999999, AI)[1], gameBoard)
        if(gameEngine.checkWin(gameBoard,PLAYER) or gameEngine.checkWin(gameBoard,AI)):
            print('WIIIN')

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
    text = menuFont.render('Easy', True, WHITE, BLACK)
    textRect = text.get_rect()  
    textRect.center = (800, 400) 
    screen.blit(text, textRect)
    # Button 2
    pygame.draw.rect(screen,BLACK,(720,450,160,50))
    text = menuFont.render('Normal', True, WHITE, BLACK)
    textRect = text.get_rect()  
    textRect.center = (800, 475) 
    screen.blit(text, textRect)
    # Button 3
    pygame.draw.rect(screen,BLACK,(720,525,160,50))
    text = menuFont.render('Hard', True, WHITE, BLACK)
    textRect = text.get_rect()  
    textRect.center = (800, 550) 
    screen.blit(text, textRect)

def popup(screen,gameBoard,cond):
    menuFont = pygame.font.Font("Aaargh.ttf", 20)
    if(cond != 0):
        if(cond == PLAYER):
            displayed_text = "Yellow Win."
        elif(cond == AI):
            displayed_text = "Red Win."
        elif(cond == DRAW):
            displayed_text = "Draw."
        pygame.draw.rect(screen,YELLOW,(720,25,160,50))
        text = menuFont.render(displayed_text, True, BLACK, YELLOW)
        textRect = text.get_rect()  
        textRect.center = (800, 50) 
        screen.blit(text, textRect)
    else:
        pygame.draw.rect(screen,BLACK,(720,25,160,50))
        text = menuFont.render('New Game', True, WHITE, BLACK)
        textRect = text.get_rect()  
        textRect.center = (800, 50) 
        screen.blit(text, textRect)

def isInputNotValid (input, gameBoard):
    return input < 0 or input > 6 or gameBoard[0][input] != 0
    
#Constant
PLAYER = 1
AI = 2
DRAW = 10
COLUMN_SIZE = 100
WHITE=(255,255,255)
RED = (255,0,0)
YELLOW = (255,255,0)
BLUE=(0,0,255)
BLACK  = (0,0,0)
EASY = 3
NORMAL = 4
HARD = 6

WIN = False
DEPTH = NORMAL
WIN_SIDE = 0
#screen Initializer
category = 2
pygame.init()
gameBoard = [[0 for col in range(7)] for row in range(6)]
screen = pygame.display.set_mode((9 * COLUMN_SIZE,6 * COLUMN_SIZE),0,32)
makeBackground(screen, gameBoard)

while True:
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            if position[0] >=5 and position[0]<=695:
                if(not WIN):
                    if position[0] <= 95 and position[0] >=5:
                        putPiece(gameBoard, 0, category)
                    elif position[0] <= 195 and position[0] >=105:
                        putPiece(gameBoard, 1, category)
                    elif position[0] <= 295 and position[0] >=205:
                        putPiece(gameBoard, 2, category)
                    elif position[0] <= 395 and position[0] >=305:
                        putPiece(gameBoard, 3, category)
                    elif position[0] <= 495 and position[0] >=405:
                        putPiece(gameBoard, 4, category)
                    elif position[0] <= 595 and position[0] >=505:
                        putPiece(gameBoard, 5, category)
                    elif position[0] <= 695 and position[0] >=605:
                        putPiece(gameBoard, 6, category)
            elif position[0] <= 875 and position[0] >=725: # Menu bar
                if position[1] >= 25 and position[1] <= 75:
                    gameBoard = [[0 for col in range(7)] for row in range(6)]
                    WIN = False
                    WIN_SIDE = 0
                if position[1] >= 125 and position[1] <= 175:
                    category = 1
                    gameBoard = [[0 for col in range(7)] for row in range(6)]
                    WIN = False
                    WIN_SIDE = 0
                if position[1] >= 200 and position[1] <= 250:
                    category = 2
                    gameBoard = [[0 for col in range(7)] for row in range(6)]
                    WIN = False
                    WIN_SIDE = 0
                if position[1] >= 275 and position[1] <= 325:
                    category = 3
                    gameBoard = [[0 for col in range(7)] for row in range(6)]
                    WIN = False
                    WIN_SIDE = 0
                if position[1] >= 375 and position[1] <= 425:
                    print('Difficulty 1')
                    gameBoard = [[0 for col in range(7)] for row in range(6)]
                    DEPTH = EASY
                    WIN = False
                    WIN_SIDE = 0
                if position[1] >= 450 and position[1] <= 500:
                    print('Difficulty 2')
                    gameBoard = [[0 for col in range(7)] for row in range(6)]
                    DEPTH = NORMAL
                    WIN = False
                    WIN_SIDE = 0
                if position[1] >= 525 and position[1] <= 575:
                    print('Difficulty 3')
                    gameBoard = [[0 for col in range(7)] for row in range(6)]
                    DEPTH = HARD
                    WIN = False
                    WIN_SIDE = 0
        elif event.type==QUIT:
            pygame.quit()
            sys.exit()
    if(gameEngine.checkEndCondition(gameBoard)):
        WIN = True
        if(gameEngine.checkWin(gameBoard,PLAYER)):
            WIN_SIDE = PLAYER
        elif(gameEngine.checkWin(gameBoard,AI)):
            WIN_SIDE = AI
        elif(gameEngine.checkFullBoard(gameBoard)):
            WIN_SIDE = DRAW
    popup(screen, gameBoard, WIN_SIDE)

    makeBoard(screen, gameBoard)
    pygame.display.update()
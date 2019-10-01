import random
import os

def printBoard (gameBoard,enable) :
    if(enable):
        os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(6):
        for j in range(7):
            print(gameBoard[i][j], end = '')
            if (j != 7):
                print('   ', end = '')
        print()

def updateBoard (playerNumber, position, gameBoard):
    for i in range(6):
        if(gameBoard[5-i][position] == 0):
            gameBoard[5-i][position] = playerNumber
            break

def inputStep (gameBoard):
    step = int(input('Masukkan kolom langkah anda selanjutnya: ')) - 1
    while (isInputNotValid(step, gameBoard)):
        print('Masukkan anda salah, ulangi')
        step = int(input('Masukkan kolom langkah anda selanjutnya: ')) - 1
    return step

def isInputNotValid (input, gameBoard):
    return input < 0 or input > 6 or gameBoard[0][input] != 0

def randomizeMove (gameBoard):
    randomBotMove =  random.randint(0, 7)
    while (isInputNotValid(randomBotMove, gameBoard)):
        randomBotMove =  random.randint(0, 7)
    return randomBotMove

def checkEndCondition (gameBoard):
    return checkFullBoard(gameBoard) # or checkWinOrLose(gameBoard)

def checkFullBoard (gameBoard):
    for i in range(7):
        if (gameBoard[0][i] == 0):
            return False
    return True

def minimaxAlphaBetaPruning(gameBoard, depth, alpha, beta, playerNumber):
    legalMoves = []
    for i in range(7):
        if (gameBoard[0][i] == 0):
            legalMoves.append(i)
    print(legalMoves)
    move = randomizeMove(gameBoard)
    if depth == 0 or checkEndCondition(gameBoard):
        return utility(gameboard), move
    if playerNumber == 2:
        value = -999999
        for move in legalMoves:
            value = max(value, minimaxAlphaBetaPruning(gameBoard, depth - 1, alpha, beta, 1)[0])
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        print(value, move)
        return value, move
    else: # playerNumber == 1
        value = 999999
        for move in legalMoves:
            value = min(value, minimaxAlphaBetaPruning(gameBoard, depth - 1, alpha, beta, 2)[0])
            beta = min(beta, value)
            if alpha >= beta:
                break
        print(value, move)
        return value, move

def checkWin(gameBoard,piece):
    #Check horizontal condition
    for c in range(4):
        for r in range(6):
            if(gameBoard[r][c] == gameBoard[r][c+1] == gameBoard[r][c+2] == gameBoard[r][c+3] == piece):
                return True
    #Check vertical condition
    for c in range(7):
        for r in range(3):
            if(gameBoard[r][c] == gameBoard[r+1][c] == gameBoard[r+2][c] == gameBoard[r+3][c] == piece):
                return True
    #Check positive slope
    for c in range(4):
        for r in range(3):
            if(gameBoard[r][c] == gameBoard[r+1][c+1] == gameBoard[r+2][c+2] == gameBoard[r+3][c+3] == piece):
                return True
    #Check negative slope
    for c in range(4):
        for r in range(3,6):
            if(gameBoard[r][c] == gameBoard[r-1][c+1] == gameBoard[r-2][c+2] == gameBoard[r-3][c+3] == piece):
                return True



PLAYER = 1
AI = 2
clear_screen = False

gameBoard = [[0 for col in range(7)] for row in range(6)]
# Board structure
#   1  2  3  4  5  6  7 => column
# 1 0  0  0  0  0  0  0
# 2 0  0  0  0  0  0  0
# 3 0  0  0  0  0  0  0
# 4 0  0  0  0  0  0  0
# 5 0  0  0  0  0  0  0
# 6 0  0  0  0  0  0  0
printBoard(gameBoard,clear_screen)
win = False

while (not win):
    updateBoard(PLAYER, inputStep(gameBoard), gameBoard)
    # updateBoard(AI, randomizeMove(gameBoard), gameBoard)
    updateBoard(AI, minimaxAlphaBetaPruning(gameBoard, 4, -999999, 999999, AI)[1], gameBoard)
    printBoard(gameBoard,clear_screen)
    if(checkWin(gameBoard,PLAYER) or checkWin(gameBoard,AI)):
        win = True

print('Permainan berakhir!!!')
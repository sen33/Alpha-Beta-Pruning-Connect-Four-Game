import random

def printBoard (gameBoard) :
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

gameBoard = [[0 for col in range(7)] for row in range(6)]
# Board structure
#   1  2  3  4  5  6  7
# 1 0  0  0  0  0  0  0
# 2 0  0  0  0  0  0  0
# 3 0  0  0  0  0  0  0
# 4 0  0  0  0  0  0  0
# 5 0  0  0  0  0  0  0
# 6 0  0  0  0  0  0  0
printBoard(gameBoard)
while (not checkEndCondition(gameBoard)):
    updateBoard(1, inputStep(gameBoard), gameBoard)
    updateBoard(2, randomizeMove(gameBoard), gameBoard)
    printBoard(gameBoard)

print('Permainan berakhir!!!')
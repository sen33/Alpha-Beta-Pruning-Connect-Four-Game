import random
import os
import math

class gameEngine():
    def printBoard (gameBoard,enable) :
        if(enable):
            os.system('cls' if os.name == 'nt' else 'clear')
        for i in range(6):
            for j in range(7):
                print(gameBoard[i][j], end = '')
                if (j != 7):
                    print('   ', end = '')
            print()

    def copyBoard(board):
        new_board = []
        for i in range(6):
            temp = board[i].copy()
            new_board.append(temp)
        return new_board

    def updateBoard (playerNumber, position, gameBoard):
        for i in range(6):
            if(position != None):
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
        while (gameEngine.isInputNotValid(randomBotMove, gameBoard)):
            randomBotMove =  random.randint(0, 7)
        return randomBotMove

    def checkEndCondition (gameBoard):
        return gameEngine.checkFullBoard(gameBoard) or gameEngine.checkWin(gameBoard,gameEngine.PLAYER) or gameEngine.checkWin(gameBoard,gameEngine.AI)

    def checkFullBoard (gameBoard):
        for i in range(7):
            if (gameBoard[0][i] == 0):
                return False
        return True

    def evaluate(block, piece):
        score = 0

        opponent = gameEngine.PLAYER
        if(piece == gameEngine.PLAYER):
            opponent = gameEngine.AI
        
        if block.count(piece) == 4:
            score += 100   
        elif block.count(piece) == 3 and block.count(0) == 1:
            score += 10
        elif block.count(piece) == 2 and block.count(0) == 2:
            score += 5
        if block.count(opponent) == 3 and block.count(0) == 1:
            score -= 8

        return score

    def utility(gameBoard, piece):
        score = 0
        
        #Horizontal scoring
        for r in range(6):
            #fetch a row into arr
            row_arr = []
            for i in range(7):
                row_arr.append(gameBoard[r][i])

            #divade the arr into 4 column block
            for c in range(4):
                block = row_arr[c:c+4]
                score += gameEngine.evaluate(block, piece)

        #Vertical scoring
        for c in range(7):
            col_arr = []
            for i in range(6):
                col_arr.append(gameBoard[i][c])

            for r in range(3):
                block = col_arr[r:r+4]
                score += gameEngine.evaluate(block, piece)


        #Positive slope scoring
        for r in range(3):
            for c in range(4):
                block = []
                for i in range(4):
                    block.append(gameBoard[r+i][c+i])
                    score += gameEngine.evaluate(block, piece)

        #Negative slope scoring
        for r in range(3):
            for c in range(3,6):
                block = []
                for i in range(4):
                    block.append(gameBoard[r+3-i][c-i])
                    score += gameEngine.evaluate(block, piece)

        return score

    def validMoveSearch(gameBoard):
        valid_moves = []
        for c in range(7):
            for r in range(6):
                if (gameBoard[r][c] == 0):
                    valid_moves.append(c)
                    break
        return valid_moves

    def minimaxAlphaBetaPruning(gameBoard, depth, alpha, beta, playerNumber):
        
        legalMoves = gameEngine.validMoveSearch(gameBoard)

        if depth == 0 or gameEngine.checkEndCondition(gameBoard):
            if (gameEngine.checkWin(gameBoard, gameEngine.PLAYER)):
                return [-999999, None]
            elif (gameEngine.checkWin(gameBoard, gameEngine.AI)):
                return [999999, None]
            elif (gameEngine.checkFullBoard(gameBoard)):
                return [0, None]
            else: # depth == 0
                return [gameEngine.utility(gameBoard, gameEngine.AI), None]
                

        if (playerNumber == 2):
            value = -math.inf
            res_move = random.choice(legalMoves)
            for move in legalMoves:
                board = gameEngine.copyBoard(gameBoard)
                gameEngine.updateBoard(2, move, board)
                score = gameEngine.minimaxAlphaBetaPruning(board, depth - 1, alpha, beta, 1)[0]
                if(score>value):
                    value = score
                    res_move = move
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return [value, res_move]

        else: # playerNumber == 1
            value = math.inf
            res_move = random.choice(legalMoves)
            for move in legalMoves:
                board = gameEngine.copyBoard(gameBoard)
                gameEngine.updateBoard(1, move, board)
                score = gameEngine.minimaxAlphaBetaPruning(board, depth - 1, alpha, beta, 2)[0]
                if(score<value):
                    value = score
                    res_move = move
                beta = min(beta,value)
                if alpha >= beta:
                    break
            return [value, res_move]

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
    # clear_screen = False

    # gameBoard = [[0 for col in range(7)] for row in range(6)]
    # # Board structure
    # #   1  2  3  4  5  6  7 => column
    # # 1 0  0  0  0  0  0  0
    # # 2 0  0  0  0  0  0  0
    # # 3 0  0  0  0  0  0  0
    # # 4 0  0  0  0  0  0  0
    # # 5 0  0  0  0  0  0  0
    # # 6 0  0  0  0  0  0  0
    # printBoard(gameBoard,clear_screen)
    # win = False

    # while (not win):
    #     updateBoard(PLAYER, inputStep(gameBoard), gameBoard)
    #     # updateBoard(AI, randomizeMove(gameBoard), gameBoard)
    #     updateBoard(AI, minimaxAlphaBetaPruning(gameBoard, 5, -999999, 999999, AI)[1], gameBoard)
    #     printBoard(gameBoard,clear_screen)
    #     if(checkWin(gameBoard,PLAYER) or checkWin(gameBoard,AI)):
    #         win = True

    # print('Permainan berakhir!!!')
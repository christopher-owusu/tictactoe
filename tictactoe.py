import random
from turtle import position

board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]
currPlayer = "X"
winner = None
gameRunning = True


# printing the game board
def printBoard(board):
    print("----------")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("----------")
printBoard(board)


# take player input
def playerInput(board):
    inp = int(input("Enter a number 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp - 1] == "-":
        board[inp - 1] = currPlayer
    else:
        print("Space already occupied!! ")


# check for win or tie
def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def checkVeritcal(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

def checkDiagonaL(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True


def checkTie(board):
    global winner
    if "-" not in board:
        printBoard(board)
        print("It's a tie 🎊🎉🎉🎉🎊 ")
        gameRunning = False


def checkWin():
    if checkDiagonaL(board) or checkHorizontal(board) or checkVeritcal(board):
        print(f"The winner is {winner}")

# switch the player
def switchPlayer ():
    global currPlayer
    if currPlayer == "X":
        currPlayer = "0"
    else:
        currPlayer = "X"

# computer AI
def computer(board):
    while currPlayer == "0":
        position = random.randint(0, 8)
        if board[position] =="-":
            board[position] = "0"
            switchPlayer()


# check for win or tie again
while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()
    computer(board)
    checkWin()
    checkTie(board)
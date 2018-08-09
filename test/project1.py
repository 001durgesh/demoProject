# tic tac toe Game
from __future__ import print_function
import os

test_board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9'];
checkMove = []
xArray=[]
oArray=[]

def displayBoard(board):
    # os.system('clear')
    os.system('clear')
    print(board[7] + ' |' + board[8] + ' |' + board[9])
    print(board[4] + ' |' + board[5] + ' |' + board[6])
    print(board[1] + ' |' + board[2] + ' |' + board[3])


def playMove(player, symbol):
    print(player, ", take a move : ")
    move = input()
    if move in checkMove:
        print("This is not valid move.")
        playMove(player, symbol)
    else:
        checkMove.append(move)
        test_board[move] = symbol

        if symbol=='X':
            xArray.append(move)
        else:
            oArray.append(move)

    return checkMove


def isPlayerWon(data):
    count=0

    if len(data) >= 3:
        for i in range(0, len(data) - 1):
            for j in range(i + i, len(data)):
                if data[i] - data[j] in sub:
                    count += 1
                    break
                else:
                    sub.append(data[i] - data[j])

            if count >= 1:
                break

    if count >= 1:
        return True
    else:
        False


displayBoard(test_board)
move = []

print("Select your player 'X' or 'O' : ")
player1 = raw_input()

while player1 != 'X' and player1 != 'O':
    print("Select your player 'X' or 'O' : ")
    player1 = raw_input()

if player1 == 'X':
    player2 = 'O'
else:
    player2 = 'X'

print("You have selected player1 = " + player1)
flag = 0

for move in range(1, 7):

    if flag == 0:
        playMove("Player1", "X")
        print('\n' * 20)
        print("Current status : ")
        displayBoard(test_board)

        if isPlayerWon(xArray) is True:
            print("Player1 is Winner...!!!")
            break
        else:
            flag = 1

    else:

        playMove("Player2", "O")
        print('\n' * 20)
        print("Current status : ")
        displayBoard(test_board)

        if isPlayerWon(oArray) is True:
            print("Player2 is Winner...!!!")
            break
        else:
            flag = 0

print("Final status of game is : ")
displayBoard(test_board)

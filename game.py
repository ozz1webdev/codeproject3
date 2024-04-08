import board
import word_art
import ai
import globalFunc as gf
import sys
import time
from colorama import Fore

# spining cursor function


def spin_cursor():
    """
        spinning cursor to show the computer is thinking
    """
    spin = ['\\', '|', '/', '-', '\\', '|', '/', '-' ]
    print("Computer Calculating ...")
    for e in range(1):
        for i in range(len(spin)):
            sys.stdout.write("\b%s" % spin[i])
            sys.stdout.flush()
            time.sleep(0.2)

# set the mark in board


def setMark(squareVal, boardNr, boardSel, square, mark):
    """
    places the correct mark with the correct color to board
    """
    if boardNr == 1:
        boardList = list(board.board1)

        for i in range(len(squareVal)):
            if squareVal[i] == 'X':
                boardList[boardList.index(str(i))] = Fore.RED + 'X'  + Fore.BLUE
            if squareVal[i] == 'O':
                boardList[boardList.index(str(i))] = Fore.GREEN + 'O' + Fore.BLUE
            else:
                pass

    if boardNr == 2:
        boardList = list(board.board2)

        for i in range(len(squareVal)):
            if squareVal[i] == 'X':
                boardList[boardList.index(str(i))] = Fore.RED + 'X'  + Fore.BLUE
            if squareVal[i] == 'O':
                boardList[boardList.index(str(i))] = Fore.GREEN + 'O' + Fore.BLUE
            else:
                pass
    
    boardSel = ''.join(map(str,boardList))
    gf.clearScreen()
    print(word_art.logo)
    return boardSel


# check if player or computer has won
def checkWin(squareVal):
    """
    checks if the player or the computer has won
    """
    if squareVal[1] == squareVal[2] and squareVal[2] == squareVal[3]:
        if squareVal[1] == 'X':
            print(word_art.you_win)
            time.sleep(1)
            return 'win'
        elif squareVal[1] == 'O':
            print(word_art.you_lose)
            time.sleep(1)
            return 'lose'
    elif squareVal[4] == squareVal[5] and squareVal[5] == squareVal[6]:
        if squareVal[4] == 'X':
            print(word_art.you_win)
            time.sleep(1)
            return 'win'
        elif squareVal[4] == 'O':
            print(word_art.you_lose)
            time.sleep(1)
            return 'lose'
    elif squareVal[7] == squareVal[8] and squareVal[8] == squareVal[9]:
        if squareVal[7] == 'X':
            print(word_art.you_win)
            time.sleep(1)
            return 'win'
        elif squareVal[7] == 'O':
            print(word_art.you_lose)
            time.sleep(1)
            return 'lose'
    elif squareVal[1] == squareVal[4] and squareVal[4] == squareVal[7]:
        if squareVal[1] == 'X':
            print(word_art.you_win)
            time.sleep(1)
            return 'win'
        elif squareVal[1] == 'O':
            print(word_art.you_lose)
            time.sleep(1)
            return 'lose'
    elif squareVal[2] == squareVal[5] and squareVal[5] == squareVal[8]:
        if squareVal[2] == 'X':
            print(word_art.you_win)
            time.sleep(1)
            return 'win'
        elif squareVal[2] == 'O':
            print(word_art.you_lose)
            time.sleep(1)
            return 'lose'
    elif squareVal[3] == squareVal[6] and squareVal[6] == squareVal[9]:
        if squareVal[3] == 'X':
            print(word_art.you_win)
            time.sleep(1)
            return 'win'
        elif squareVal[3] == 'O':
            print(word_art.you_lose)
            time.sleep(1)
            return 'lose'
    elif squareVal[1] == squareVal[5] and squareVal[5] == squareVal[9]:
        if squareVal[1] == 'X':
            print(word_art.you_win)
            time.sleep(1)
            return 'win'
        elif squareVal[1] == 'O':
            print(word_art.you_lose)
            time.sleep(1)
            return 'lose'
    elif squareVal[3] == squareVal[5] and squareVal[5] == squareVal[7]:
        if squareVal[3] == 'X':
            print(word_art.you_win)
            time.sleep(1)
            return 'win'
        elif squareVal[3] == 'O':
            print(word_art.you_lose)
            time.sleep(1)
            return 'lose'

    for i in range(1, len(squareVal)):
        if squareVal[i] == 0:
            return 'continue'
    else:
        print(word_art.draw)
        time.sleep(1)
        return 'draw'


def runGame():
    """
        runs the game
    """

    selection = ''
    playerScore = gf.getScore()[0]
    computerScore = gf.getScore()[1]
    draw = gf.getScore()[2]
    playFirst = True

    while selection != '3':
        squareVal = [0,0,0,0,0,0,0,0,0,0]
        gf.clearScreen()
        print(word_art.logo)
        print(f"Player : "+Fore.RED+str(playerScore)+Fore.BLUE + "   Computer : "+Fore.GREEN+str(computerScore)+Fore.BLUE + "   Draw : "+str(draw)+"\n")
        print(board.board1 + board.board2)
        gf.typingPrint('Please select Board 1 or Board 2 or 3 to Exit: ')
        board_selection = input()
        try:
            if board_selection == '1':
                boardSel = board.board1
                boardNr = 1
                pass
            elif board_selection == '2':
                boardSel = board.board2
                boardNr = 2
                pass
            elif board_selection == '3':
                gf.clearScreen()
                print(word_art.logo)
                break
            else:
                raise ValueError
        except (ValueError, NameError, KeyboardInterrupt):
            gf.typingPrint('Wrong Selection. Try Again!')
            time.sleep(1)
            pass
        else:
            while True: #game loop
                gf.clearScreen()
                print(word_art.logo)
                print(f"Player : "+Fore.RED+str(playerScore)+Fore.BLUE + "   Computer : "+Fore.GREEN+str(computerScore)+Fore.BLUE + "   Draw : "+str(draw)+"\n")
                print(boardSel)

                while playFirst:
                    gf.typingPrint("Do you like to play first ? (y/n): ")
                    playFirst = input()
                    if playFirst == 'y' or playFirst == 'Y' or playFirst == 'yes' or playFirst == 'Yes':
                        playFirst = False
                        break
                    elif playFirst == 'n' or playFirst == 'N' or playFirst == 'no' or playFirst == 'No':
                        gf.typingPrint("Computer will play first.\n")
                        time.sleep(1)
                        spin_cursor()
                        compPos = ai.compTurn(squareVal)
                        squareVal[compPos] = 'O'
                        boardSel = setMark(squareVal, boardNr, boardSel, int(compPos), Fore.GREEN + "O " + Fore.BLUE + "\b")
                        gf.clearScreen()
                        print(word_art.logo)
                        print(f"Player : "+Fore.RED+str(playerScore)+Fore.BLUE + "   Computer : "+Fore.GREEN+str(computerScore)+Fore.BLUE + "   Draw : "+str(draw)+"\n")
                        print(boardSel)
                        playFirst = False
                        break
                    else:
                        gf.typingPrint("Wrong Selection. Try Again!\n")
                        time.sleep(1)
                        playFirst = True
                        pass
                while True:

                    try:
                        gf.typingPrint('Your turn enter Square Number: ')
                        square = int(input())

                        if square < 1 or square > 9:
                            gf.typingPrint('Wrong Selection. Try Again!\n')
                            raise ValueError

                        if squareVal[square] != 0:
                            gf.typingPrint('Wrong Selection, Square Taken. Try Again!\n')
                            raise ValueError

                    except (ValueError, KeyboardInterrupt):
                        pass
                    else:
                        squareVal[square] = 'X'
                        boardSel = setMark(squareVal, boardNr, boardSel, int(square), Fore.RED + "X " + Fore.BLUE + "\b")
                        print(f"Player : "+Fore.RED+str(playerScore)+Fore.BLUE + "   Computer : "+Fore.GREEN+str(computerScore)+Fore.BLUE + "   Draw : "+str(draw)+"\n")
                        print(boardSel)
                        break
                winStatus = checkWin(squareVal)
                if winStatus == "continue":
                    print("Computer turn ...")
                    spin_cursor()
                    compPos = ai.compTurn(squareVal)
                    squareVal[compPos] = 'O'
                    boardSel = setMark(squareVal, boardNr, boardSel,int(compPos), Fore.GREEN + "O " + Fore.BLUE + "\b")
                    winStatus = checkWin(squareVal)
                    print(f"Player : "+Fore.RED+str(playerScore)+Fore.BLUE + "   Computer : "+Fore.GREEN+str(computerScore)+Fore.BLUE + "   Draw : "+str(draw)+"\n")
                    print(boardSel)
                if winStatus == 'win':
                    gf.addScore('player')
                    gf.typingPrint('You Win. Do you want to play again? (y/n): ')
                    playAgain = input()
                    if playAgain == 'y' or playAgain == 'Y' or playAgain == 'yes' or playAgain == 'YES':
                        squareVal = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                        runGame()

                    elif playAgain == 'n' or playAgain == 'N' or playAgain == 'no' or playAgain == 'NO':
                        squareVal = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                        break
                    else:
                        gf.typingPrint('Wrong Selection. Try Again!')
                        time.sleep(1)

                elif winStatus == 'lose':
                    gf.addScore('computer')
                    gf.typingPrint('You Lose. Do you want to play again? (y/n): ')
                    playAgain = input()
                    if playAgain == 'y' or playAgain == 'Y' or playAgain == 'yes' or playAgain == 'YES':
                        squareVal = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                        runGame()

                    elif playAgain == 'n' or playAgain == 'N' or playAgain == 'no' or playAgain == 'NO':
                        squareVal = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                        break
                    else:
                        gf.typingPrint('Wrong Selection. Try Again!')
                        time.sleep(1)

                elif winStatus == 'draw':
                    gf.addScore('draw')
                    gf.typingPrint('Draw. Do you want to play again? (y/n): ')
                    playAgain = input()
                    if playAgain == 'y' or playAgain == 'Y' or playAgain == 'yes' or playAgain == 'YES':
                        squareVal = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                        runGame()

                    elif playAgain == 'n' or playAgain == 'N' or playAgain == 'no' or playAgain == 'NO':
                        squareVal = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                        break
                    else:
                        gf.typingPrint('Wrong Selection. Try Again!')
                        time.sleep(1)

                else:
                    pass
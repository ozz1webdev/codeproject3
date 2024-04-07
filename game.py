import board,word_art,ai
import globalFunc as gf
import sys,time
from colorama import Fore

#spining cursor
def spin_cursor():
    spin = ['\\', '|', '/', '-', '\\', '|', '/', '-' ]
    print("Computer Calculating ...")
    for e in range (1):
        for i in range(len(spin)):
            sys.stdout.write("\b%s" % spin[i])
            sys.stdout.flush()
            time.sleep(0.2)

def setMark2(boardSel,square,mark):
    boardSel = boardSel.replace(str(square),mark)
    gf.clearScreen()
    print(word_art.logo)
    return boardSel
def setMark(boardNr,boardSel,square,mark):
    boardList = list(boardSel)
    if boardNr == 1:
        if square == 1:
            pos = boardList.index('1')
            boardList[pos] = mark
        if square == 2:
            pos = boardList.index('2')
            boardList[pos] = mark
        if square == 3:
            pos = boardList.index('3')
            boardList[pos] = mark
        if square == 4:
            pos = boardList.index('4')
            boardList[pos] = mark
        if square == 5:
            pos = boardList.index('5')
            boardList[pos] = mark
        if square == 6:
            pos = boardList.index('6')
            boardList[pos] = mark
        if square == 7:
            pos = boardList.index('7')
            boardList[pos] = mark
        if square == 8:
            pos = boardList.index('8')
            boardList[pos] = mark
        if square == 9:
            pos = boardList.index('9')
            boardList[pos] = mark
    print(pos)
    input()
    boardSel = ''.join(boardList)
    return boardSel

def checkWin(squareVal):
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
    selection = ''
    while selection != '3':
        squareVal = [0,0,0,0,0,0,0,0,0,0]
        gf.clearScreen()
        print(word_art.logo)
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
                break
            else:
                raise ValueError
        except (ValueError,NameError):
            gf.typingPrint('Wrong Selection. Try Again!')
            time.sleep(1)
            pass
        else:
            playerScore = 0
            computerScore = 0
            draw = 0
            while True: #game loop
                gf.clearScreen()
                print(word_art.logo)
                print(f"Score :    Player : {playerScore}     Computer : {computerScore}     Draw : {draw}")
                print(boardSel)
                #boardSel.replace('X','\033[1;31;40m X'+'\033[1;34;40m') # \033[1;34;40m')
                #boardSel.replace('O','\033[1;32;40m O')# \033[1;34;40m')
                #print(squareVal) 
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
                        
                    except ValueError:
                        pass
                    else:
                        squareVal[square] = 'X'
                        #boardSel = setMark(boardNr,boardSel,square,'\033[1;31;40m'+ 'X' + '\033[1;34;40m')
                        boardSel = setMark(boardNr,boardSel,square,Fore.RED + 'X' + Fore.BLUE)
                        print(boardSel)
                        break
                winStatus = checkWin(squareVal)
                if winStatus == "continue":
                    print("Computer turn ...")
                    spin_cursor()
                    #boardSel,square = ai.compTurn(boardNr,boardSel,squareVal)
                    compPos = ai.compTurn(boardNr,boardSel,squareVal)
                    squareVal[compPos] = 'O'
                    boardSel = setMark(boardNr,boardSel,compPos,Fore.GREEN + 'O' + Fore.BLUE)
                    winStatus = checkWin(squareVal)
                    print(boardSel)
                if winStatus == 'win':
                    playerScore = playerScore + 1
                    gf.typingPrint('You Win. Do you want to play again? (y/n): ')
                    playAgain = input()
                    if playAgain == 'y' or playAgain == 'Y' or playAgain == 'yes' or playAgain == 'YES':
                        squareVal = [0,0,0,0,0,0,0,0,0,0]
                        runGame()
                            
                    elif playAgain == 'n' or playAgain == 'N' or playAgain == 'no' or playAgain == 'NO':
                        squareVal = [0,0,0,0,0,0,0,0,0,0]
                        
                    else:
                        gf.typingPrint('Wrong Selection. Try Again!')
                        time.sleep(1)
                        
                elif winStatus == 'lose':
                    computerScore = computerScore + 1
                    gf.typingPrint('You Lose. Do you want to play again? (y/n): ')
                    playAgain = input()
                    if playAgain == 'y' or playAgain == 'Y' or playAgain == 'yes' or playAgain == 'YES':
                        squareVal = [0,0,0,0,0,0,0,0,0,0]
                        runGame()
                        
                    elif playAgain == 'n' or playAgain == 'N' or playAgain == 'no' or playAgain == 'NO':
                        squareVal = [0,0,0,0,0,0,0,0,0,0]
                        
                    else:
                        gf.typingPrint('Wrong Selection. Try Again!')
                        time.sleep(1)
                        
                elif winStatus == 'draw':
                    draw = draw + 1
                    gf.typingPrint('Draw. Do you want to play again? (y/n): ')
                    playAgain = input()
                    if playAgain == 'y' or playAgain == 'Y' or playAgain == 'yes' or playAgain == 'YES':
                        squareVal = [0,0,0,0,0,0,0,0,0,0]
                        runGame()
                        
                    elif playAgain == 'n' or playAgain == 'N' or playAgain == 'no' or playAgain == 'NO':
                        squareVal = [0,0,0,0,0,0,0,0,0,0]
                        
                    else:
                        gf.typingPrint('Wrong Selection. Try Again!')
                        time.sleep(1)
                        
                else:
                    pass


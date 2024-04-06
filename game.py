import board,word_art,ai
import globalFunc as gf
import sys,time
import colorama as color
#spining cursor
def spin_cursor():
    spin = ['\\', '|', '/', '-', '\\', '|', '/', '-' ]
    print("Computer Calculating ...")
    for e in range (5):
        for i in range(len(spin)):
            sys.stdout.write("\b%s" % spin[i])
            sys.stdout.flush()
            time.sleep(0.2)

def setMark(boardSel,square,mark):
    boardSel = boardSel.replace(str(square),mark)
    gf.clearScreen()
    print(word_art.logo)
    #print(boardSel)
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
    else:
        return 'continue'

def runGame():
    selection = ''
    while selection != '3':
        playerScore = 0
        computerScore = 0
        squareVal = [0,0,0,0,0,0,0,0,0,0]
        gf.clearScreen()
        print(word_art.logo)
        print(board.board1 + board.board2)
        gf.typingPrint('Please select Board 1 or Board 2 or 3 to Exit: ')
        board_selection = input()
        try:
            if board_selection == '1':
                boardSel = board.board1
                pass
            elif board_selection == '2':
                boardSel = board.board2
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
            while True:
                gf.clearScreen()
                print(word_art.logo)
                print(boardSel)
                print(squareVal)                    
                try:
                    gf.typingPrint('Your turn enter Square Number: ')
                    square = int(input())
                    if square < 1 or square > 9:
                        raise ValueError

                    if squareVal[square] == 'X' or squareVal[square] == 'O':
                        gf.typingPrint('Wrong Selection, Square Taken. Try Again!\n') # NameError
                        raise NameError

                    else:
                        squareVal[square] = 'X'

                except (ValueError,NameError):
                    gf.typingPrint('Wrong Selection. Try Again!')
                    time.sleep(1)
                    pass
                else:
                    boardSel = setMark(boardSel,square,'X')
                    print(boardSel)
                    checkWin(squareVal)
                    print("Computer turn ...")
                    #spin_cursor()
                    boardSel,square = ai.compTurn(boardSel,squareVal)
                    squareVal[square] = 'O'
                    print(boardSel)

                finally:
                    winStatus = checkWin(squareVal)
                    if winStatus == 'win':
                        playerScore = playerScore + 1
                        gf.typingPrint('You Win. Do you want to play again? (y/n): ')
                        playAgain = input()
                        if playAgain == 'y' or playAgain == 'Y':
                            squareVal = [0,0,0,0,0,0,0,0,0,0]
                            runGame()
                            break
                        elif playAgain == 'n' or playAgain == 'N':
                            break
                        else:
                            gf.typingPrint('Wrong Selection. Try Again!')
                            time.sleep(1)
                            break
                    elif winStatus == 'lose':
                        computerScore = computerScore + 1
                        break
                    else:
                        pass


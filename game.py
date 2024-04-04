import board,word_art
import globalFunc as gf
import sys,time

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
            gf.typingPrint(word_art.you_win)
            time.sleep(1)
            return 'win'
        elif squareVal[1] == 'O':
            gf.typingPrint(word_art.you_lose)
            time.sleep(1)
            return 'lose'
    elif squareVal[4] == squareVal[5] and squareVal[5] == squareVal[6]:
        if squareVal[4] == 'X':
            gf.typingPrint(word_art.you_win)
            time.sleep(1)
            return 'win'
        elif squareVal[4] == 'O':
            gf.typingPrint(word_art.you_lose)
            time.sleep(1)
            return 'lose'
    elif squareVal[7] == squareVal[8] and squareVal[8] == squareVal[9]:
        if squareVal[7] == 'X':
            gf.typingPrint(word_art.you_win)
            time.sleep(1)
            return 'win'
        elif squareVal[7] == 'O':
            gf.typingPrint(word_art.you_lose)
            time.sleep(1)
            return 'lose'
    elif squareVal[1] == squareVal[4] and squareVal[4] == squareVal[7]:
        if squareVal[1] == 'X':
            gf.typingPrint(word_art.you_win)
            time.sleep(1)
            return 'win'
        elif squareVal[1] == 'O':
            gf.typingPrint(word_art.you_lose)
            time.sleep(1)
            return 'lose'
    elif squareVal[2] == squareVal[5] and squareVal[5] == squareVal[8]:
        if squareVal[2] == 'X':
            gf.typingPrint(word_art.you_win)
            time.sleep(1)
            return 'win'
        elif squareVal[2] == 'O':
            gf.typingPrint(word_art.you_lose)
            time.sleep(1)
            return 'lose'
    elif squareVal[3] == squareVal[6] and squareVal[6] == squareVal[9]:
        if squareVal[3] == 'X':
            gf.typingPrint(word_art.you_win)
            time.sleep(1)
            return 'win'
        elif squareVal[3] == 'O':
            gf.typingPrint(word_art.you_lose)
            time.sleep(1)
            return 'lose'
    elif squareVal[1] == squareVal[5] and squareVal[5] == squareVal[9]:
        if squareVal[1] == 'X':
            gf.typingPrint(word_art.you_win)
            time.sleep(1)
            return 'win'
        elif squareVal[1] == 'O':
            gf.typingPrint(word_art.you_lose)
            time.sleep(1)
            return 'lose'
    elif squareVal[3] == squareVal[5] and squareVal[5] == squareVal[7]:
        if squareVal[3] == 'X':
            gf.typingPrint(word_art.you_win)
            time.sleep(1)
            return 'win'
        elif squareVal[3] == 'O':
            gf.typingPrint(word_art.you_lose)
            time.sleep(1)
            return 'lose'
    else:
        return 'continue'
def compTurn(boardSel):
    print("compTurn func")
    boardSel = setMark(boardSel,1,'O')
    return boardSel,1
def runGame():
    squareVal = [0,0,0,0,0,0,0,0,0,0]
    selection = ''
    while selection != '3':
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
                gf.typingPrint('Your turn enter Square Number: ')
                try:
                    square = int(input())
                    if square < 1 or square > 9:
                        raise ValueError
                    else:
                        squareVal[square] = 'X'
                except (ValueError,NameError):
                    gf.typingPrint('Wrong Selection. Try Again!')
                    time.sleep(1)
                    pass
                else:
                    boardSel = setMark(boardSel,square,'X')
                    print(boardSel)
                    print("Computer turn ...")
                    spin_cursor()
                    boardSel,square = compTurn(boardSel)
                    squareVal[square] = 'O'
                    print(boardSel)
                finally:
                    pass


#print(board.board1)
#board.board1 = board.board1.replace('5','X')
"""
text = list(board)

print(text)
text[5]='x'
text = "".join(text)
print(text)
"""
from os import system, name
import board,word_art,time
import globalFunc as gf

def runGame():
    board = '0'
    gf.clearScreen()
    print(word_art.logo)
    print(board.board1 + "                 " + board.board2)
    print("-------Board 1----------------------------------------- Board 2 -----------------")
    gf.typingPrint('Please select Board: ')
    board_selection = input()
    try:
        if board_selection == '1':
            boardSel = board.board1
        elif board_selection == '2':
            boardSel = board.board2
        else:
            raise ValueError
    except (ValueError,NameError):
        gf.typingPrint('Wrong Selection. Try Again!')
        time.sleep(20)
        pass
    else:
        gf.clearScreen()
        print(word_art.logo)
        print(boardSel)
        gf.typingPrint('Enter Square Number: ')
        square = input()
        print(boardSel.replace(square,'X'))


#print(board.board1)
#board.board1 = board.board1.replace('5','X')
"""
text = list(board)

print(text)
text[5]='x'
text = "".join(text)
print(text)
"""
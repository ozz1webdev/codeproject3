from os import system, name
import time,sys
import board
import word_art

#define typingtext effect
def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

def typingInput(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
        value = input()  
        return value  

#Clear The screen
def clearScreen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
clearScreen()



#print the logo
print(f"\033[1;34;40m {word_art.logo}")

#print welcome text
typingPrint("Welcome to TicTacToe Game have fun ...\n")
typingPrint("--------------------------------------\n")


#print menu to user
#print(board.board1)
#board.board1 = board.board1.replace('5','X')
"""
text = list(board)

print(text)
text[5]='x'
text = "".join(text)
print(text)
"""
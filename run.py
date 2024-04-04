from os import system, name
import time,sys
import board,word_art,ui

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

def mainScreen():
    clearScreen()
    print(word_art.logo)
    print(ui.menu)
    menu_selection = input("Select your option: ")

#print the logo
print(f"\033[1;34;40m {word_art.logo}")

#print welcome text
typingPrint("Welcome to Tic Tac Toe Game have fun\n")
print("------------------------------------\n")

#spining cursor
def spin_cursor():
    spin = ['\\', '|', '/', '-', '\\', '|', '/', '-' ]
    print("Computer Calculating ...")
    for e in range (5):
        for i in range(len(spin)):
            sys.stdout.write("\b%s" % spin[i])
            sys.stdout.flush()
            time.sleep(0.2)

#print menu to user
menu_selection = ''
while menu_selection != 3:
    clearScreen()
    print(word_art.logo)
    print(ui.menu)
    menu_selection = input("Select your option: ")

    if menu_selection == '1':
        pass

    if menu_selection == '2':
        clearScreen()
        print(word_art.logo)
        print(ui.rules)
        try:
            input("Press enter to continue ...")
        except SyntaxError:
            pass

    if menu_selection == '3':
        typingPrint("Good Bye!")
        break


#print(board.board1)
#board.board1 = board.board1.replace('5','X')
"""
text = list(board)

print(text)
text[5]='x'
text = "".join(text)
print(text)
"""
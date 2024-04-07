from os import system, name
import time,sys
import word_art,ui,game
import globalFunc as gf


gf.clearScreen()

def mainScreen():
    gf.clearScreen()
    print(word_art.logo)
    print(ui.menu)
    menu_selection = input("Select your option: ")

#print the logo
print(f"\033[1;34;40m {word_art.logo}")

#print welcome text
gf.typingPrint("Welcome to Tic Tac Toe Game have fun\n")
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
menu_selection = '0'
while menu_selection != 3:
    try:
        print(ui.menu) #print the menu
        menu_selection = input("Select your option: ") #user menu selection

    except (RuntimeError,ValueError):
        print("Wrong Selection. Try Again!")
        time.sleep(20)
        pass
    
    else:
        if menu_selection == '1': #start the game
            game.runGame()

        elif menu_selection == '2':   #print rules
            gf.clearScreen()
            print(word_art.logo)
            print(ui.rules)
            try:
                input("Press ENTER to continue ...")
            except SyntaxError:
                pass

        elif menu_selection == '3': #exit the game
            gf.typingPrint("Good Bye!")
            break
        else:
            print("Wrong Selection. Try Again!")
            time.sleep(2)
            pass
    finally:
        pass

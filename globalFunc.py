from os import system, name
import time,sys,board


score = {
    'player': 0,
    'computer': 0,
    'draw': 0
}
def addScore(winner):
    score[winner] += 1

def getScore():
    vars = [score['player'],score['computer'],score['draw']]
    return vars
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
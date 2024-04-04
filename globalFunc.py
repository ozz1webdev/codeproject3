from os import system, name
import time,sys

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
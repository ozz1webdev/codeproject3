import game
from colorama import Fore

def compTurn(squareval):
    """
        the computer logic
    """

    pos = 0

    #check if computer can win
    while True:
        try:
            if squareval[1] == 'O' and squareval[2] == 'O' and squareval[3] == 0:
                pos = 3
                break
            if squareval[1] == 'O' and squareval[3] == 'O' and squareval[2] == 0:
                pos = 2
                break
            if squareval[2] == 'O' and squareval[3] == 'O' and squareval[1] == 0:
                pos = 1
                break
            if squareval[4] == 'O' and squareval[5] == 'O' and squareval[6] == 0:
                pos = 6
                break
            if squareval[4] == 'O' and squareval[6] == 'O' and squareval[5] == 0:
                pos = 5
                break
            if squareval[5] == 'O' and squareval[6] == 'O' and squareval[4] == 0:
                pos = 4
                break
            if squareval[7] == 'O' and squareval[8] == 'O' and squareval[9] == 0:
                pos = 9
                break
            if squareval[7] == 'O' and squareval[9] == 'O' and squareval[8] == 0:
                pos = 8
                break
            if squareval[8] == 'O' and squareval[9] == 'O' and squareval[7] == 0:
                pos = 7
                break
            if squareval[1] == 'O' and squareval[4] == 'O' and squareval[7] == 0:
                pos = 7
                break
            if squareval[1] == 'O' and squareval[7] == 'O' and squareval[4] == 0:
                pos = 4
                break
            if squareval[4] == 'O' and squareval[7] == 'O' and squareval[1] == 0:
                pos = 1
                break
            if squareval[2] == 'O' and squareval[5] == 'O' and squareval[8] == 0:
                pos = 8
                break
            if squareval[2] == 'O' and squareval[8] == 'O' and squareval[5] == 0:
                pos = 5
                break
            if squareval[5] == 'O' and squareval[8] == 'O' and squareval[2] == 0:
                pos = 2
                break
            if squareval[3] == 'O' and squareval[6] == 'O' and squareval[9] == 0:
                pos = 9
                break
            if squareval[3] == 'O' and squareval[9] == 'O' and squareval[6] == 0:
                pos = 6
                break
            if squareval[6] == 'O' and squareval[9] == 'O' and squareval[3] == 0:
                pos = 3
                break
            if squareval[1] == 'O' and squareval[5] == 'O' and squareval[9] == 0:
                pos = 9
                break
            if squareval[1] == 'O' and squareval[9] == 'O' and squareval[5] == 0:
                pos = 5
                break
            if squareval[5] == 'O' and squareval[9] == 'O' and squareval[1] == 0:
                pos = 1
                break
            if squareval[3] == 'O' and squareval[5] == 'O' and squareval[7] == 0:
                pos = 7
                break
            if squareval[3] == 'O' and squareval[7] == 'O' and squareval[5] == 0:
                pos = 5    
                break
            if squareval[5] == 'O' and squareval[7] == 'O' and squareval[3] == 0:
                pos = 3

        except:
            pass
#check if Player can win
        else:
            if squareval[1] == 'X' and squareval[2] == 'X' and squareval[3] == 0:
                pos = 3
                break
            if squareval[1] == 'X' and squareval[3] == 'X' and squareval[2] == 0:
                pos = 2
                break
            if squareval[2] == 'X' and squareval[3] == 'X' and squareval[1] == 0:
                pos = 1
                break
            if squareval[4] == 'X' and squareval[5] == 'X' and squareval[6] == 0:
                pos = 6
                break
            if squareval[4] == 'X' and squareval[6] == 'X' and squareval[5] == 0:
                pos = 5
                break
            if squareval[5] == 'X' and squareval[6] == 'X' and squareval[4] == 0:
                pos = 4
                break
            if squareval[7] == 'X' and squareval[8] == 'X' and squareval[9] == 0:
                pos = 9
                break
            if squareval[7] == 'X' and squareval[9] == 'X' and squareval[8] == 0:
                pos = 8
                break
            if squareval[8] == 'X' and squareval[9] == 'X' and squareval[7] == 0:
                pos = 7
                break
            if squareval[1] == 'X' and squareval[4] == 'X' and squareval[7] == 0:
                pos = 7
                break
            if squareval[1] == 'X' and squareval[7] == 'X' and squareval[4] == 0:
                pos = 4
                break
            if squareval[4] == 'X' and squareval[7] == 'X' and squareval[1] == 0:
                pos = 1
                break
            if squareval[2] == 'X' and squareval[5] == 'X' and squareval[8] == 0:
                pos = 8
                break
            if squareval[2] == 'X' and squareval[8] == 'X' and squareval[5] == 0:
                pos = 5
                break
            if squareval[5] == 'X' and squareval[8] == 'X' and squareval[2] == 0:
                pos = 2
                break
            if squareval[3] == 'X' and squareval[6] == 'X' and squareval[9] == 0:
                pos = 9
                break
            if squareval[3] == 'X' and squareval[9] == 'X' and squareval[6] == 0:
                pos = 6
                break
            if squareval[6] == 'X' and squareval[9] == 'X' and squareval[3] == 0:
                pos = 3
                break
            if squareval[1] == 'X' and squareval[5] == 'X' and squareval[9] == 0:
                pos = 9
                break
            if squareval[1] == 'X' and squareval[9] == 'X' and squareval[5] == 0:
                pos = 5
                break
            if squareval[5] == 'X' and squareval[9] == 'X' and squareval[1] == 0:
                pos = 1
                break
            if squareval[3] == 'X' and squareval[5] == 'X' and squareval[7] == 0:
                pos = 7
                break
            if squareval[3] == 'X' and squareval[7] == 'X' and squareval[5] == 0:
                pos = 5    
                break
            if squareval[5] == 'X' and squareval[7] == 'X' and squareval[3] == 0:
                pos = 3
                break

    #choise square
        finally:
            if pos == 0:
                if squareval[1] == 0 :
                    pos = 1
                    break
                elif squareval[9] == 0:
                    pos = 9
                    break
                elif squareval[3] == 0:
                    pos = 3
                    break
                elif squareval[7] == 0:
                    pos = 7
                    break
                elif squareval[5] == 0:
                    pos = 5
                    break
                elif squareval[2] == 0:
                    pos = 2
                    break
                elif squareval[4] == 0:
                    pos = 4
                    break
                elif squareval[6] == 0:
                    pos = 6
                    break
                elif squareval[8] == 0:
                    pos = 8
                    break
            else:
                break
    
    return pos

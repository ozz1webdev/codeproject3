import game

def compTurn(boardSel,squareval):
#check if player 1 can win
    if squareval[1] == 'X' and squareval[2] == 'X':
        pos = 3
    elif squareval[1] == 'X' and squareval[3] == 'X':
        pos = 2
    elif squareval[2] == 'X' and squareval[3] == 'X':
        pos = 1
    elif squareval[4] == 'X' and squareval[5] == 'X':
        pos = 6
    elif squareval[4] == 'X' and squareval[6] == 'X':
        pos = 5
    elif squareval[5] == 'X' and squareval[6] == 'X':
        pos = 4
    elif squareval[7] == 'X' and squareval[8] == 'X':
        pos = 9
    elif squareval[7] == 'X' and squareval[9] == 'X':
        pos = 8
    elif squareval[8] == 'X' and squareval[9] == 'X':
        pos = 7
    elif squareval[1] == 'X' and squareval[4] == 'X':
        pos = 7
    elif squareval[1] == 'X' and squareval[7] == 'X':
        pos = 4
    elif squareval[4] == 'X' and squareval[7] == 'X':
        pos = 1
    elif squareval[2] == 'X' and squareval[5] == 'X':
        pos = 9
    elif squareval[2] == 'X' and squareval[8] == 'X':
        pos = 5
    elif squareval[5] == 'X' and squareval[8] == 'X':
        pos = 2
    elif squareval[3] == 'X' and squareval[6] == 'X':
        pos = 9
    elif squareval[3] == 'X' and squareval[9] == 'X':
        pos = 6
    elif squareval[6] == 'X' and squareval[9] == 'X':
        pos = 3
    elif squareval[1] == 'X' and squareval[5] == 'X':
        pos = 9
    elif squareval[1] == 'X' and squareval[9] == 'X':
        pos = 5
    elif squareval[5] == 'X' and squareval[9] == 'X':
        pos = 1
    elif squareval[3] == 'X' and squareval[5] == 'X':
        pos = 7
    elif squareval[3] == 'X' and squareval[7] == 'X':
        pos = 5    
    elif squareval[5] == 'X' and squareval[7] == 'X':
        pos = 3
#check if computer can win
    if squareval[1] == 'O' and squareval[2] == 'O':
        pos = 3
    elif squareval[1] == 'O' and squareval[3] == 'O':
        pos = 2
    elif squareval[2] == 'O' and squareval[3] == 'O':
        pos = 1
    elif squareval[4] == 'O' and squareval[5] == 'O':
        pos = 6
    elif squareval[4] == 'O' and squareval[6] == 'O':
        pos = 5
    elif squareval[5] == 'O' and squareval[6] == 'O':
        pos = 4
    elif squareval[7] == 'O' and squareval[8] == 'O':
        pos = 9
    elif squareval[7] == 'O' and squareval[9] == 'O':
        pos = 8
    elif squareval[8] == 'O' and squareval[9] == 'O':
        pos = 7
    elif squareval[1] == 'O' and squareval[4] == 'O':
        pos = 7
    elif squareval[1] == 'O' and squareval[7] == 'O':
        pos = 4
    elif squareval[4] == 'O' and squareval[7] == 'O':
        pos = 1
    elif squareval[2] == 'O' and squareval[5] == 'O':
        pos = 9
    elif squareval[2] == 'O' and squareval[8] == 'O':
        pos = 5
    elif squareval[5] == 'O' and squareval[8] == 'O':
        pos = 2
    elif squareval[3] == 'O' and squareval[6] == 'O':
        pos = 9
    elif squareval[3] == 'O' and squareval[9] == 'O':
        pos = 6
    elif squareval[6] == 'O' and squareval[9] == 'O':
        pos = 3
    elif squareval[1] == 'O' and squareval[5] == 'O':
        pos = 9
    elif squareval[1] == 'O' and squareval[9] == 'O':
        pos = 5
    elif squareval[5] == 'O' and squareval[9] == 'O':
        pos = 1
    elif squareval[3] == 'O' and squareval[5] == 'O':
        pos = 7
    elif squareval[3] == 'O' and squareval[7] == 'O':
        pos = 5    
    elif squareval[5] == 'O' and squareval[7] == 'O':
        pos = 3
#choise square
    if squareval[1] != 'X' and squareval[1] != 'O':
        pos = 1
    elif squareval[3] != 'X' and squareval[3] != 'O':
        pos = 3
    elif squareval[5] != 'X' and squareval[5] != 'O':
        pos = 5
    elif squareval[7] != 'X' and squareval[7] != 'O':
        pos = 7
    elif squareval[9] != 'X' and squareval[9] != 'O':
        pos = 9
    elif squareval[2] != 'X' and squareval[2] != 'O':
        pos = 2
    elif squareval[4] != 'X' and squareval[4] != 'O':
        pos = 4
    elif squareval[6] != 'X' and squareval[6] != 'O':
        pos = 6
    elif squareval[8] != 'X' and squareval[8] != 'O':
        pos = 8

    boardSel = game.setMark(boardSel,pos,'O')
    return boardSel,pos

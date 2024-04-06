import game

def compTurn(boardSel,squareval):

    print("compTurn func")
    pos = 1
#check if player 1 can win
    if squareval[1] == 'X' and squareval[2] == 'X':
        pos = 3
    if squareval[1] == 'X' and squareval[3] == 'X':
        pos = 2
    if squareval[2] == 'X' and squareval[3] == 'X':
        pos = 1
    if squareval[4] == 'X' and squareval[5] == 'X':
        pos = 6
    if squareval[4] == 'X' and squareval[6] == 'X':
        pos = 5
    if squareval[5] == 'X' and squareval[6] == 'X':
        pos = 4
    if squareval[7] == 'X' and squareval[8] == 'X':
        pos = 9
    if squareval[7] == 'X' and squareval[9] == 'X':
        pos = 8
    if squareval[8] == 'X' and squareval[9] == 'X':
        pos = 7
    if squareval[1] == 'X' and squareval[4] == 'X':
        pos = 7
    if squareval[1] == 'X' and squareval[7] == 'X':
        pos = 4
    if squareval[4] == 'X' and squareval[7] == 'X':
        pos = 1
    if squareval[2] == 'X' and squareval[5] == 'X':
        pos = 8
    if squareval[2] == 'X' and squareval[8] == 'X':
        pos = 5
    if squareval[5] == 'X' and squareval[8] == 'X':
        pos = 2
    if squareval[3] == 'X' and squareval[6] == 'X':
        pos = 9
    if squareval[3] == 'X' and squareval[9] == 'X':
        pos = 6
    if squareval[6] == 'X' and squareval[9] == 'X':
        pos = 3
    if squareval[1] == 'X' and squareval[5] == 'X':
        pos = 9
    if squareval[1] == 'X' and squareval[9] == 'X':
        pos = 5
    if squareval[5] == 'X' and squareval[9] == 'X':
        pos = 1
    if squareval[3] == 'X' and squareval[5] == 'X':
        pos = 7
    if squareval[3] == 'X' and squareval[7] == 'X':
        pos = 5    
    if squareval[5] == 'X' and squareval[7] == 'X':
        pos = 3
#choise square
    if squareval[1] != 'X' and squareval[1] != 'O':
        pos = 1
    if squareval[3] != 'X' and squareval[3] != 'O':
        pos = 3
    if squareval[5] != 'X' and squareval[5] != 'O':
        pos = 5
    if squareval[7] != 'X' and squareval[7] != 'O':
        pos = 7
    if squareval[9] != 'X' and squareval[9] != 'O':
        pos = 9
    if squareval[2] != 'X' and squareval[2] != 'O':
        pos = 2
    if squareval[4] != 'X' and squareval[4] != 'O':
        pos = 4
    if squareval[6] != 'X' and squareval[6] != 'O':
        pos = 6
    if squareval[8] != 'X' and squareval[8] != 'O':
        pos = 8

    boardSel = game.setMark(boardSel,pos,'O')
    return boardSel,pos

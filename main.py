import time
import random
import math

class Colo:
    R = '\033[91m'
    DR = '\033[31m'
    G = '\033[92m'
    Y = '\033[93m'
    B = '\033[94m'
    DB = '\033[34m'
    C = '\033[96m'
    M = '\033[95m'
    RE = '\033[0m'
    BO = '\033[1m'
    GR = '\033[90m'
    BL = '\033[30m'

mapsize = input("Map size: ")

while mapsize.isdigit() == False:
    print("Must be a number")
    mapsize = input("Map size: ")

mapsize = int(mapsize)

###custom Board
bcustom = [

    ]
for i in range(mapsize):
    bcustom.append({})
    for j in range(mapsize):
        leterj = chr(ord('@')+j+1)
        what = str(leterj)+str(i+1)
        bcustom[i].update({what : "■"})
bcustom.append({})


#custom board where mines
bcustomines = [

    ]
for i in range(mapsize):
    bcustomines.append({})
    for j in range(mapsize):
        leterj = chr(ord('@')+j+1)
        what = str(leterj)+str(i+1)
        bcustomines[i].update({what : "□"})
bcustomines.append({})
        

board = bcustom ##board size change
boardm = bcustomines ####
boards = mapsize


flags = None


def boardprint(what):
    if flags != None:
        print("Flags ",flags)
    for i in range(len(what)):
        
        if i < 10:
            print("0"+str(i),end=" ")
        else:
            print(i,end=" ")
            

        for j in range(len(what[0])):

            if i == 0:
                print(chr(ord('@')+j+1),end=" ")
            else:
                where = chr(ord('@')+j+1) + str(i)
                #print(i-1,where)
                if what[i-1][where] == "1":
                    print(Colo.B + what[i-1][where] + Colo.RE,end=" ")
                elif what[i-1][where] == "2":
                    print(Colo.G + what[i-1][where] + Colo.RE,end=" ")
                elif what[i-1][where] == "3":
                    print(Colo.R + what[i-1][where] + Colo.RE,end=" ")
                elif what[i-1][where] == "4":
                    print(Colo.DB + Colo.BO + what[i-1][where] + Colo.RE,end=" ")
                elif what[i-1][where] == "5":
                    print(Colo.DR + Colo.BO + what[i-1][where] + Colo.RE,end=" ")
                elif what[i-1][where] == "6":
                    print(Colo.C + what[i-1][where] + Colo.RE,end=" ")
                elif what[i-1][where] == "7":
                    print(Colo.M + what[i-1][where] + Colo.RE,end=" ")
                elif what[i-1][where] == "8":
                    print(Colo.GR + what[i-1][where] + Colo.RE,end=" ")

#                elif what[i-1][where] == "X":
#                    print(Colo.BL + what[i-1][where] + Colo.RE,end=" ")
                else:
                    print(what[i-1][where],end=" ")
        print("")



def check(boardm, boards, locleter, locnum, mode, board):
    if locleter > 0 and locnum > -1 and locleter < boards+1 and locnum < boards:

        buit = chr(ord('@')+locleter) + str(locnum+1)
        if mode == "m":
            if boardm[locnum][buit] == "□":
                boardm[locnum][buit] = "1"
            elif boardm[locnum][buit].isdigit() == True:
                boardm[locnum][buit] = str(int(boardm[locnum][buit])+1)
        elif mode == "e":
            if board[locnum][buit] != "□" and board[locnum][buit] != "⚑":
                if boardm[locnum][buit] != "□":
                    board[locnum][buit] = boardm[locnum][buit]
                else:
                    board[locnum][buit] = "O"

def checkUser(let, num, boardm, boards, a, board):
    locleter = let-1 ##let-1
    locnum = num-1
    check(boardm, boards, locleter, locnum, a, board)
    locleter = let
    locnum = num-2
    check(boardm, boards, locleter, locnum, a, board)
    locleter = let+1
    locnum = num-1
    check(boardm, boards, locleter, locnum, a, board)
    locleter = let
    locnum = num
    check(boardm, boards, locleter, locnum, a, board)
    ###diagational
    locleter = let-1 ##let-1
    locnum = num-2  ##num-1
    check(boardm, boards, locleter, locnum, a, board)
    locleter = let+1 
    locnum = num-2
    check(boardm, boards, locleter, locnum, a, board)
    locleter = let+1 
    locnum = num
    check(boardm, boards, locleter, locnum, a, board)
    locleter = let-1 
    locnum = num
    check(boardm, boards, locleter, locnum, a, board)


######################
###     Visible    ###
######################

boardprint(board)


inp = input("where ")
    


let = ord(inp[0])-64 #number

if len(inp) >= 3:
    if inp[2] != "F":
        num = int(inp[1]+inp[2])
    else:
        num = int(inp[1])
else:
    num = int(inp[1])

while num <= 0 or let > boards or num > boards:
    if num <= 0:
        print("Must be greater than 0")
    if num >boards:
        print("Number out of range")
    if let >boards:
        print("Leter out of range")
    inp = input("where ")
        
    let = ord(inp[0])-64 #number
    if len(inp) >= 3:
        if inp[2] != "F":
            num = int(inp[1]+inp[2])
        else:
            num = int(inp[1])
    else:
        num = int(inp[1])
    

buit = chr(ord('@')+let) + str(num)

board[num-1][buit] = "□"


checkUser(let, num, boardm, boards, "e", board)


######  Mines Generator  #######
flags = 0

minesnumber = boards*boards
minesnumber = int(minesnumber / 6)

for g in range(minesnumber):
    ranNum = random.randint(1, boards)
    ranLet = random.randint(1, boards)
    buit = chr(ord('@')+ranNum) + str(ranLet)
    if boardm[ranLet-1][buit] != "X" and board[ranLet-1][buit] != "□" and board[ranLet-1][buit] != "O":
        flags += 1
        boardm[ranLet-1][buit] = "X"

for i in range(len(boardm)):
    num = i
    for j in range(len(boardm[0])):
        let = j+1
        if i != 0:
            where = chr(ord('@')+let) + str(i)
            if boardm[i-1][where] == "X":
                checkUser(let, num, boardm, boards, "m", board)



for i in range(len(board)):
    num = i
    for j in range(len(board[0])):
        let = j+1
        if i != 0:
            where = chr(ord('@')+let) + str(i)

            if board[i-1][where] == "□" or board[i-1][where] == "O" and boardm[i-1][where] != "□":
                board[i-1][where] = boardm[i-1][where]





checkleft = ['A1']
while checkleft != []:
    for i in range(len(board)):
        num = i
        for j in range(len(board[0])):
            let = j+1
            if i != 0:
                where = chr(ord('@')+let) + str(i)
                if board[i-1][where] == "O":
                    board[i-1][where] = "□"
                    checkUser(let, num, boardm, boards, "e", board)
    checkleft = []
    for y in range(len(board)):
        for x, box in board[y].items():
            if box == "O":
                checkleft.append(x)





while True:
    boardprint(board)
    
    boxleft = []
    for y in range(len(board)):
        for x, box in board[y].items():
            if box == "■":
                boxleft.append(x)
    bombleft = []
    for y in range(len(boardm)):
        for x, box in boardm[y].items():
            if box == "X":
                bombleft.append(x)

    if len(list(set(boxleft) - set(bombleft))) == 0:
        print("!!!You Won!!!")
        break

    inp = input("where ")
    #print(ord("B")-64)

    let = ord(inp[0])-64 #number

    if len(inp) >= 3:
        if inp[2] != "F":
            num = int(inp[1]+inp[2])
            #print("num:",num)
        else:
            num = int(inp[1])
    else:
        num = int(inp[1])

    while num <= 0 or let > boards or num > boards:
        if num <= 0:
            print("Must be greater than 0")
        if num >boards:
            print("Number out of range")
        if let >boards:
            print("Leter out of range")
        inp = input("where ")
            
        let = ord(inp[0])-64 #number
        if len(inp) >= 3:
            if inp[2] != "F":
                num = int(inp[1]+inp[2])
            else:
                num = int(inp[1])
        else:
            num = int(inp[1])
            

    buit = chr(ord('@')+let) + str(num)


    if inp[-1] == "F":
        board[num-1][buit] = "⚑"
        flags -= 1
    else:
        if boardm[num-1][buit] != "□":
            board[num-1][buit] = boardm[num-1][buit]
        else:
            board[num-1][buit] = "O"
            
        if board[num-1][buit] == "X":
            boardprint(boardm)
            print("!!!!GAME OVER!!!!")
            break


                    


        checkleft = ['A1']
        while checkleft != []:
            for i in range(len(board)):
                num = i
                for j in range(len(board[0])):
                    let = j+1
                    if i != 0:
                        where = chr(ord('@')+let) + str(i)
                        if board[i-1][where] == "O":
                            board[i-1][where] = "□"
                            checkUser(let, num, boardm, boards, "e", board)
            checkleft = []
            for y in range(len(board)):
                for x, box in board[y].items():
                    if box == "O":
                        checkleft.append(x)
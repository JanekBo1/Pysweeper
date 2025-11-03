abcMap = {1 : "A", 2 : "B", 3 : "C", 4 : "D", 5 : "E", 6 : "F"}
RabcMap = {"A" : 1, "B" : 2, "C" : 3, "D" : 4, "E" : 5, "F" : 6}
import time
import random

b6x6 = [
    {"A1":"■", "B1": "■", "C1": "■", "D1": "■", "E1": "■", "F1": "■"},
    {"A2":"■", "B2": "■", "C2": "■", "D2": "■", "E2": "■", "F2": "■"},
    {"A3":"■", "B3": "■", "C3": "■", "D3": "■", "E3": "■", "F3": "■"},
    {"A4":"■", "B4": "■", "C4": "■", "D4": "■", "E4": "■", "F4": "■"},
    {"A5":"■", "B5": "■", "C5": "■", "D5": "■", "E5": "■", "F5": "■"},
    {"A6":"■", "B6": "■", "C6": "■", "D6": "■", "E6": "■", "F6": "■"},
    {}
]
b6x6m = [
    {"A1":"□", "B1": "□", "C1": "□", "D1": "□", "E1": "□", "F1": "□"},
    {"A2":"□", "B2": "□", "C2": "□", "D2": "□", "E2": "□", "F2": "□"},
    {"A3":"□", "B3": "□", "C3": "□", "D3": "□", "E3": "□", "F3": "□"},
    {"A4":"□", "B4": "□", "C4": "□", "D4": "□", "E4": "□", "F4": "□"},
    {"A5":"□", "B5": "□", "C5": "□", "D5": "□", "E5": "□", "F5": "□"},
    {"A6":"□", "B6": "□", "C6": "□", "D6": "□", "E6": "□", "F6": "□"},
    {}
]




board = b6x6 ##board size change
boardm = b6x6m ####
boards = 6





def boardprint(what):
    for i in range(len(what)):
        
        print(i,end=" ")

        for j in range(len(what[0])):

            if i == 0:
                print(abcMap[j+1],end=" ")
            else:
                where = abcMap[j+1] + str(i)
                #print(i-1,where)
                print(what[i-1][where],end=" ")
        print("")



def check(boardm, boards, locleter, locnum, mode, board):
    if locleter > 0 and locnum > -1 and locleter < boards+1 and locnum < boards:

        buit = abcMap[locleter] + str(locnum+1)
        if mode == "m":
            if boardm[locnum][buit] == "□":
                boardm[locnum][buit] = "1"
            elif boardm[locnum][buit].isdigit() == True:
                boardm[locnum][buit] = str(int(boardm[locnum][buit])+1)
        elif mode == "e":
            if board[locnum][buit] != "□":
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

###Visible
boardprint(board)

inp = input("where ")

let = RabcMap[inp[0]] #number
num = int(inp[1])


buit = abcMap[let] + str(num)
board[num-1][buit] = "□"

checkUser(let, num, boardm, boards, "e", board)


for g in range(5):
    ranNum = random.randint(1, boards)
    ranLet = random.randint(1, boards)
    buit = abcMap[ranNum] + str(ranLet)
    if boardm[ranLet-1][buit] != "X" and board[ranLet-1][buit] != "□" and board[ranLet-1][buit] != "O":
#       maxg = maxg + 1
        boardm[ranLet-1][buit] = "X"

for i in range(len(boardm)):
    num = i
    for j in range(len(boardm[0])):
        let = j+1
        if i != 0:
            where = abcMap[let] + str(i)
            if boardm[i-1][where] == "X":
                checkUser(let, num, boardm, boards, "m", board)



for i in range(len(board)):
    num = i
    for j in range(len(board[0])):
        let = j+1
        if i != 0:
            where = abcMap[let] + str(i)

            if board[i-1][where] == "□" or board[i-1][where] == "O" and boardm[i-1][where] != "□":
                board[i-1][where] = boardm[i-1][where]





checkleft = ['A1']
while checkleft != []:
    for i in range(len(board)):
        num = i
        for j in range(len(board[0])):
            let = j+1
            if i != 0:
                where = abcMap[let] + str(i)
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

    inp = input("where")
    
    let = RabcMap[inp[0]] #number
    num = int(inp[1])

    buit = abcMap[let] + str(num)

    if len(inp) >= 4:
        if inp[3] == "F":
            board[num-1][buit] = "⚑"
    elif len(inp) == 3:
        if inp[2] == "F":
            board[num-1][buit] = "⚑"
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
                    if box == "O":
                        checkleft.append(j)
                    let = j+1
                    if i != 0:
                        where = abcMap[let] + str(i)
                        if board[i-1][where] == "O":
                            board[i-1][where] = "□"
                            checkUser(let, num, boardm, boards, "e", board)
            checkleft = []
            for y in range(len(board)):
                for x, box in board[y].items():
                    if box == "O":
                        checkleft.append(x)

                            


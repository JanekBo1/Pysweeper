import curses
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

flags = 0



flags = 0

def boardprint(stdscr, what):
    if flags != None:
        stdscr.addstr(boards+4, 0, "Flags%i"%(flags))
    for i in range(len(what)):
        
        #print(i,end=" ")
        stdscr.addstr(i, 0, str(i))
		

        for j in range(len(what[0])):

            if i == 0:
                #print(chr(ord('@')+j+1),end=" ")
                stdscr.addstr(i, j+j+2, chr(ord('@')+j+1))
            else:
                where = chr(ord('@')+j+1) + str(i)

                #print(what[i-1][where],end=" ")
                stdscr.addstr(i, j+j+2, what[i-1][where])
        #print("")

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

def main(stdscr):
    curses.curs_set(0)
    curses.mousemask(1)

    boardprint(stdscr, board)

    key = stdscr.getch()

    #if key == curses.KEY_MOUSE:
    stdscr.addstr(12,0, "test")
    _, x, y, _, _ = curses.getmouse()

    xwhere = chr(int(ord('@')+x/2)) + str(y)
    board[y-1][xwhere] = "□"

    checkUser(int(x/2), y, boardm, boards, "e", board)

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

    boardprint(stdscr, board)                
    while 1:

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

        stdscr.refresh()
        key = stdscr.getch()

        if key == curses.KEY_MOUSE:
            _, x, y, _, _ = curses.getmouse()


            if x in range(2,boards*2+1) and y in range(1,boards+1):
                xwhere = chr(int(ord('@')+x/2)) + str(y)
                stdscr.addstr(11,0,'x, y = %i,%i \r'%(x,y))
                stdscr.addstr(11,0,'ywere, xwere ='+str(y-1)+xwhere)

                if boardm[y-1][xwhere] != "□":
                    board[y-1][xwhere] = boardm[y-1][xwhere]
                else:
                    board[y-1][xwhere] = "O"
                    
                if board[y-1][xwhere] == "X":
                    boardprint(stdscr, boardm)
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


                boardprint(stdscr, board)

        elif key == 27:
            break
curses.wrapper(main)

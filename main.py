abcMap = {1 : "A", 2 : "B", 3 : "C", 4 : "D", 5 : "E", 6 : "F"}
RabcMap = {"A" : 1, "B" : 2, "C" : 3, "D" : 4, "E" : 5, "F" : 6}
import time

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
    {"A2":"□", "B2": "1", "C2": "1", "D2": "1", "E2": "□", "F2": "□"},
    {"A3":"□", "B3": "1", "C3": "X", "D3": "1", "E3": "□", "F3": "□"},
    {"A4":"□", "B4": "1", "C4": "1", "D4": "1", "E4": "□", "F4": "□"},
    {"A5":"□", "B5": "□", "C5": "□", "D5": "1", "E5": "1", "F5": "1"},
    {"A6":"□", "B6": "□", "C6": "□", "D6": "1", "E6": "X", "F6": "1"},
    {}
]

board = b6x6 ##board size change
boardm = b6x6m ####
boards = 6

def boardprint():
    for i in range(len(board)):
        
        print(i,end=" ")

        for j in range(len(board[0])):

            if i == 0:
                print(abcMap[j+1],end=" ")
            else:
                where = abcMap[j+1] + str(i)
                #print(i-1,where)
                print(board[i-1][where],end=" ")
        print("")

while True:
    boardprint()
    inp = input("where")

    let = RabcMap[inp[0]] #number
    num = int(inp[1])

    buit = abcMap[let] + str(num)

    print(buit)

    board[num-1][buit] = boardm[num-1][buit]


    finR = False
    finL = False

    Up = False
    for h in range(20):
        for i in range(len(board)):
            num = i
            for j in range(len(board[0])):
                let = j+1
                if i != 0:
                    where = abcMap[let] + str(i)

                    if board[i-1][where] == "□":

                        if let > 1:
                            #number
                            buit = abcMap[let-1] + str(num)
                            if board[num-1][buit] != "O":
                                board[num-1][buit] = boardm[num-1][buit]
                        if num > 1:
                            buit = abcMap[let] + str(num-1)

                            if board[num-2][buit] != "O":
                                print("num",num-2)
                                board[num-2][buit] = boardm[num-2][buit]
                        if let < boards:
                            #number
                            buit = abcMap[let+1] + str(num)
                            if board[num-1][buit] != "O":
                                board[num-1][buit] = boardm[num-1][buit]
                        if num < boards:
                            buit = abcMap[let] + str(num+1)
                            if board[num][buit] != "O":
                                board[num][buit] = boardm[num][buit]
                        ##board[i-1][where] = "O"


                #print(board[i-1][where],end=" ")
        #print("")


    # for h in range(20):
    #     while board[num-1][buit] == "□" and let < boards:
    #         let += 1 #number

    #         buit = abcMap[let] + str(num)
    #         board[num-1][buit] = boardm[num-1][buit]
    #     while board[num-1][buit] == "□" and let > 1:
    #         let -= 1 #number

    #         buit = abcMap[let] + str(num)
    #         board[num-1][buit] = boardm[num-1][buit]
    #     if board[num-1][buit] != "□":
    #         let += 1 
    #     if num < boards and Up == False:
    #         num += 1
    #         buit = abcMap[let] + str(num)
    #         board[num-1][buit] = boardm[num-1][buit]
    #     else:
    #         Up = True

    #     if num > 1 and Up == True:
    #         num -= 1
    #         buit = abcMap[let] + str(num)
    #         board[num-1][buit] = boardm[num-1][buit]

    # if board[num-1][buit] == "□":
        
    #     while num < boards:
    #         #num += 1
    #         while let < boards and boardm[num-1][buit] == "□" :
    #             let += 1 #number
    #             buit = abcMap[let] + str(num)
                
    #             board[num-1][buit] = boardm[num-1][buit]
    #         while let > 1 and boardm[num-1][buit] == "□":
    #             let -= 1 #number
    #             buit = abcMap[let] + str(num)
                
    #             board[num-1][buit] = boardm[num-1][buit]
            
    #         let += 1
    #         num += 1
    #         buit = abcMap[let] + str(num)
    #         print(buit)

            


            


#        time.sleep(1)



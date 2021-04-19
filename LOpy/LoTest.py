# selection = input()
from os import system, name
moves = 0
rowX = ""

def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def ReadInput(moves):
    gridX, gridY = input('Enter location:').split()
    if gridX == 'a':
        gridX = 0
    elif gridX == 'b':
        gridX = 1
    elif gridX == 'c':
        gridX = 2
    elif gridX == 'd':
        gridX = 3
    elif gridX == 'e':
        gridX = 4
    gridY = int(gridY) - 1
    moves += 1
    return gridX, gridY, moves

def PrintBoard(newlevel):
    int = 1
    print(' : A : B : C : D : E :')
    for row in newlevel:

        rowX = " |"
        for each in row:
            if each == 0:
                rowX = rowX + "   |"
            else:
                rowX = rowX + "XXX|"
        if int <= 5:
            print(str(int) + '+---+---+---+---+---+')
        else:
            print(' +---+---+---+---+---+')
        print(rowX)
        print(rowX)
        rowX = ""
        int += 1

    print(' +---+---+---+---+---+')

def Move(gridX, gridY, newlevel):
   
    
    if newlevel[gridY][gridX] == 0:
        newlevel[gridY][gridX] = 1
    else:
        newlevel[gridY][gridX] = 0

    if gridX > 0:
        if newlevel[gridY][gridX - 1] == 0:
            newlevel[gridY][gridX - 1] = 1
        else:
            newlevel[gridY][gridX - 1] = 0
    
    if gridX < 4:
        if newlevel[gridY][gridX + 1] == 0:
            newlevel[gridY][gridX + 1] = 1
        else:
            newlevel[gridY][gridX + 1] = 0
    
    if gridY > 0:
        if newlevel[gridY - 1][gridX] == 0:
            newlevel[gridY - 1][gridX] = 1
        else:
            newlevel[gridY - 1][gridX] = 0
    
    if gridY < 4:
        if newlevel[gridY + 1][gridX] == 0:
            newlevel[gridY + 1][gridX] = 1
        else:
            newlevel[gridY + 1][gridX] = 0

# Define main method that calls other functions
def main(levelList):
    moves = 0
    levelNo = 1
    #print(sum(map(sum, grid)))
    
    while levelNo <= 50:
        for newlevel in levelList:
            #PrintBoard(grid)
            LevelComplete = False
            while LevelComplete == False:
                if (sum(map(sum, newlevel))) >= 1:
                    print('Level: ' + str(levelNo) + '  Moves: ' + str(moves)) 
                    PrintBoard(newlevel)                    
                    gridX, gridY, moves = ReadInput(moves)
                    Move(gridX, gridY, newlevel)
                    clear()
                    # print(gridX, gridY)

                    #print(grid[gridY][gridX])
                    #print(grid[0][1])

                else:
                    LevelComplete = True
                    levelNo += 1
                    moves = 0
                    #print('OUTAHEAR')
        



# Execute main() function
if __name__ == '__main__':
    level1 = [[0,0,0,0,0],[0,0,0,0,0],[1,0,1,0,1],[0,0,0,0,0],[0,0,0,0,0]]
    level2 = [[1,0,1,0,1],[1,0,1,0,1],[0,0,0,0,0],[1,0,1,0,1],[1,0,1,0,1]]
    level3 = [[0,1,0,1,0],[1,1,0,1,1],[1,1,0,1,1],[1,1,0,1,1],[0,1,0,1,0]]
    level4 = [[0,0,0,0,0],[1,1,0,1,1],[0,0,0,0,0],[1,0,0,0,1],[1,1,0,1,1]]
    level5 = [[1,1,1,1,0],[1,1,1,0,1],[1,1,1,0,1],[0,0,0,1,1],[1,1,0,1,1]]
    level6 = [[0,0,0,0,0],[0,0,0,0,0],[1,0,1,0,1],[1,0,1,0,1],[0,1,1,1,0]]
    level7 = [[1,1,1,1,0],[1,0,0,0,1],[1,0,0,0,1],[1,0,0,0,1],[1,1,1,1,0]]
    level8 = [[0,0,0,0,0],[0,0,1,0,0],[0,1,0,1,0],[1,0,1,0,1],[0,1,0,1,0]]
    level9 = [[0,1,0,1,0],[1,1,1,1,1],[0,1,1,1,0],[0,1,0,1,1],[1,1,1,0,0]]
    level10 = [[0,1,1,1,0],[0,1,1,1,0],[0,1,1,1,0],[0,0,0,0,0],[0,0,0,0,0]]
    level11 = [[1,0,1,0,1],[1,0,1,0,1],[1,0,1,0,1],[1,0,1,0,1],[0,1,1,1,0]]
    level12 = [[1,1,1,1,1],[0,1,0,1,0],[1,1,0,1,1],[0,1,1,1,0],[0,1,0,1,0]]
    level13 = [[0,0,0,1,0],[0,0,1,0,1],[0,1,0,1,0],[1,0,1,0,0],[0,1,0,0,0]]
    level14 = [[0,0,0,0,0],[0,0,0,0,0],[0,1,0,0,0],[0,1,0,0,0],[0,1,0,0,0]]
    level15 = [[0,0,0,0,0],[0,1,0,0,0],[0,0,0,0,0],[0,1,0,0,0],[0,0,0,0,0]]
    level16 = [[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[1,1,1,1,1]]
    level17 = [[0,0,0,0,0],[0,0,0,0,0],[0,0,1,0,0],[0,1,1,1,0],[1,1,1,1,1]]
    level18 = [[0,0,1,0,0],[0,1,0,1,0],[1,0,1,0,1],[0,1,0,1,0],[0,0,1,0,0]]
    level19 = [[1,0,1,0,1],[0,0,0,0,0],[1,0,1,0,1],[0,0,0,0,0],[1,0,1,0,1]]
    level20 = [[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,1],[0,0,0,0,0],[0,0,0,0,0]]
    level21 = [[0,1,1,1,1],[0,1,0,0,0],[0,1,1,1,0],[0,1,0,0,0],[0,1,0,0,0]]
    level22 = [[0,1,1,1,0],[1,0,0,0,1],[1,0,0,0,1],[1,0,0,0,1],[0,1,1,1,0]]
    level23 = [[0,0,0,0,0],[0,0,0,0,0],[0,0,1,1,1],[0,0,1,1,0],[0,0,1,0,0]]
    level24 = [[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,1],[1,1,1,1,1],[0,1,0,0,1]]
    level25 = [[1,0,0,0,0],[1,1,0,0,0],[1,1,1,0,0],[1,1,1,1,0],[0,1,1,1,1]]
    level26 = [[1,0,0,0,1],[1,0,0,0,1],[1,1,1,1,1],[1,0,0,0,1],[1,0,0,0,1]]
    level27 = [[0,0,1,0,0],[0,1,1,1,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0]]
    level28 = [[0,0,0,0,0],[0,0,0,0,0],[0,0,1,1,1],[0,0,1,1,1],[0,0,1,1,1]]
    level29 = [[0,0,0,0,0],[0,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    level30 = [[0,0,0,0,0],[0,0,0,0,0],[0,0,1,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    level31 = [[1,0,0,0,1],[1,1,0,0,1],[1,0,1,0,1],[1,0,0,1,1],[1,0,0,0,1]]
    level32 = [[1,1,1,1,1],[0,0,0,1,0],[0,0,1,0,0],[0,1,0,0,0],[1,1,1,1,1]]
    level33 = [[0,0,0,1,0],[0,0,0,1,0],[1,0,1,0,1],[1,0,0,0,1],[1,0,0,1,1]]
    level34 = [[0,0,1,0,1],[1,0,0,0,1],[1,0,0,0,1],[0,1,1,0,1],[0,1,1,1,1]]
    level35 = [[0,0,0,1,1],[0,1,0,1,0],[1,0,0,0,1],[1,0,1,0,1],[0,0,0,0,0]]
    level36 = [[0,0,1,0,0],[0,1,0,1,0],[1,0,0,0,1],[1,1,1,1,1],[1,0,0,0,1]]
    level37 = [[0,0,0,0,0],[0,1,1,1,0],[0,1,1,1,0],[0,1,1,1,0],[0,0,0,0,0]]
    level38 = [[1,0,1,0,1],[0,1,0,1,0],[1,0,1,0,1],[0,1,0,1,0],[1,0,1,0,1]]
    level39 = [[0,1,0,1,0],[1,0,0,0,0],[1,1,0,0,0],[0,0,1,1,0],[0,1,0,1,0]]
    level40 = [[0,0,0,0,0],[0,0,0,0,0],[0,1,0,1,0],[0,0,0,0,0],[0,0,0,0,0]]
    level41 = [[1,0,0,0,1],[0,1,0,1,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0]]
    level42 = [[1,1,1,0,0],[1,0,0,1,0],[1,1,1,0,0],[1,0,0,1,0],[1,1,1,0,0]]
    level43 = [[1,0,0,0,1],[1,1,0,1,0],[1,1,1,0,0],[0,1,0,0,0],[0,1,1,1,0]]
    level44 = [[0,0,0,0,0],[1,1,0,1,1],[1,1,1,1,1],[0,0,1,0,0],[0,1,1,1,0]]
    level45 = [[0,1,1,1,0],[1,0,1,0,0],[0,0,1,1,1],[1,1,1,1,0],[1,0,1,0,1]]
    level46 = [[0,0,1,0,0],[0,1,1,1,0],[1,1,1,1,1],[0,1,1,1,0],[0,0,1,0,0]]
    level47 = [[0,0,1,0,0],[1,1,1,1,1],[1,0,1,0,0],[0,1,0,0,1],[0,0,0,0,1]]
    level48 = [[0,0,0,0,0],[1,0,0,0,1],[0,0,1,0,0],[1,0,0,0,1],[0,0,0,0,0]]
    level49 = [[1,0,0,0,1],[0,1,0,1,0],[0,0,1,0,0],[0,1,0,1,0],[1,0,0,0,1]]
    level50 = [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
    levelList = [level1,level2,level3,level4,level5,level6,level7,level8,level9,level10,level11,level12,level13,level14,level15,level16,level17,level18,level19,level20,level21,level22,level23,level24,level25,level26,level27,level28,level29,level30,level31,level32,level33,level34,level35,level36,level37,level38,level39,level40,level41,level42,level43,level44,level45,level46,level47,level48,level49,level50]
    levelNo = 1
    main(levelList)
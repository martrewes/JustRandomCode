# selection = input()
moves = 0
rowX = ""

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

def PrintBoard(grid):
    int = 1
    print(' : A : B : C : D : E :')
    for row in grid:

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

def Move(gridX, gridY):
    #if gridX > 0:
    
    if grid[gridY][gridX] == 0:
        grid[gridY][gridX] = 1
    else:
        grid[gridY][gridX] = 0

    if gridX > 0:
        if grid[gridY][gridX - 1] == 0:
            grid[gridY][gridX - 1] = 1
        else:
            grid[gridY][gridX - 1] = 0
    
    if gridX < 4:
        if grid[gridY][gridX + 1] == 0:
            grid[gridY][gridX + 1] = 1
        else:
            grid[gridY][gridX + 1] = 0
    
    if gridY > 0:
        if grid[gridY - 1][gridX] == 0:
            grid[gridY - 1][gridX] = 1
        else:
            grid[gridY - 1][gridX] = 0
    
    if gridY < 4:
        if grid[gridY + 1][gridX] == 0:
            grid[gridY + 1][gridX] = 1
        else:
            grid[gridY + 1][gridX] = 0
    

# Define main method that calls other functions
def main(grid):
    moves = 0
    LevelComplete = False
    print(sum(map(sum, grid)))
    PrintBoard(grid)
    while LevelComplete == False:
        if (sum(map(sum, grid))) >= 1:

            gridX, gridY, moves = ReadInput(moves)
            Move(gridX, gridY)
            print(gridX, gridY)
            print('Moves: ' + str(moves))
            PrintBoard(grid)
            print(grid[gridY][gridX])
            print(grid[0][1])
            
        else:
            LevelComplete = True
            print('OUTAHEAR')
        



# Execute main() function
if __name__ == '__main__':
    grid = [[0,0,1,0,0],[0,1,1,1,0],[0,0,1,0,0],[1,0,1,0,1],[1,0,1,0,1]]
    main(grid)
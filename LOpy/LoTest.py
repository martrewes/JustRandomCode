# selection = input()

grid = [[0,0,1,0,0],[0,1,1,1,0],[0,0,1,0,0],[0,0,0,0,0],[0,0,1,1,0]]

rowX = ""
gridX, gridY = input('Enter location:').split()


int = 1
print('X Value:', gridX)
print('Y Value:', gridY)
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
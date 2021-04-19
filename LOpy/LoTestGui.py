from guizero import App, PushButton, Box, Text

app = App()

level1 = [[0,0,0,0,0],[0,0,0,0,0],[1,0,1,0,1],[0,0,0,0,0],[0,0,0,0,0]]
level2 = [1,0,1,0,1,1,0,1,0,1,0,0,0,0,0,1,0,1,0,1,1,0,1,0,1]
level3 = [0,1,0,1,0,1,1,0,1,1,1,1,0,1,1,1,1,0,1,1,0,1,0,1,0]
level4 = [0,0,0,0,0,1,1,0,1,1,0,0,0,0,0,1,0,0,0,1,1,1,0,1,1]
level5 = [1,1,1,1,0,1,1,1,0,1,1,1,1,0,1,0,0,0,1,1,1,1,0,1,1]
level6 = [0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,1,0,1,0,1,0,1,1,1,0]
level7 = [1,1,1,1,0,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,1,1,1,0]
level8 = [0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]
level9 = [0,1,0,1,0,1,1,1,1,1,0,1,1,1,0,0,1,0,1,1,1,1,1,0,0]
level10 = [0,1,1,1,0,0,1,1,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0]
level11 = [1,0,1,0,1,1,0,1,0,1,1,0,1,0,1,1,0,1,0,1,0,1,1,1,0]
level12 = [1,1,1,1,1,0,1,0,1,0,1,1,0,1,1,0,1,1,1,0,0,1,0,1,0]
level13 = [0,0,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0]
level14 = [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0]
level15 = [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]
level16 = [1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,1,1,1,1]
level17 = [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,1,1,0,1,1,1,1,1]
level18 = [0,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,0]
level19 = [1,0,1,0,1,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,1,0,1,0,1]
level20 = [0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0]
level21 = [0,1,1,1,1,0,1,0,0,0,0,1,1,1,0,0,1,0,0,0,0,1,0,0,0]
level22 = [0,1,1,1,0,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,0,1,1,1,0]
level23 = [0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,1,1,0,0,0,1,0,0]
level24 = [0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,1,1,1,1,1,0,1,0,0,1]
level25 = [1,0,0,0,0,1,1,0,0,0,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1]
level26 = [1,0,0,0,1,1,0,0,0,1,1,1,1,1,1,1,0,0,0,1,1,0,0,0,1]
level27 = [0,0,1,0,0,0,1,1,1,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0]
level28 = [0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,1,1,1,0,0,1,1,1]
level29 = [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
level30 = [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0]
level31 = [1,0,0,0,1,1,1,0,0,1,1,0,1,0,1,1,0,0,1,1,1,0,0,0,1]
level32 = [1,1,1,1,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,1,1,1,1]
level33 = [0,0,0,1,0,0,0,0,1,0,1,0,1,0,1,1,0,0,0,1,1,0,0,1,1]
level34 = [0,0,1,0,1,1,0,0,0,1,1,0,0,0,1,0,1,1,0,1,0,1,1,1,1]
level35 = [0,0,0,1,1,0,1,0,1,0,1,0,0,0,1,1,0,1,0,1,0,0,0,0,0]
level36 = [0,0,1,0,0,0,1,0,1,0,1,0,0,0,1,1,1,1,1,1,1,0,0,0,1]
level37 = [0,0,0,0,0,0,1,1,1,0,0,1,1,1,0,0,1,1,1,0,0,0,0,0,0]
level38 = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]
level39 = [0,1,0,1,0,1,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,1,0,1,0]
level40 = [0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0]
level41 = [1,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0]
level42 = [1,1,1,0,0,1,0,0,1,0,1,1,1,0,0,1,0,0,1,0,1,1,1,0,0]
level43 = [1,0,0,0,1,1,1,0,1,0,1,1,1,0,0,0,1,0,0,0,0,1,1,1,0]
level44 = [0,0,0,0,0,1,1,0,1,1,1,1,1,1,1,0,0,1,0,0,0,1,1,1,0]
level45 = [0,1,1,1,0,1,0,1,0,0,0,0,1,1,1,1,1,1,1,0,1,0,1,0,1]
level46 = [0,0,1,0,0,0,1,1,1,0,1,1,1,1,1,0,1,1,1,0,0,0,1,0,0]
level47 = [0,0,1,0,0,1,1,1,1,1,1,0,1,0,0,0,1,0,0,1,0,0,0,0,1]
level48 = [0,0,0,0,0,1,0,0,0,1,0,0,1,0,0,1,0,0,0,1,0,0,0,0,0]
level49 = [1,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0,1,0,0,0,1]
level50 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
levelList = [level1,level2,level3,level4,level5,level6,level7,level8,level9,level10,level11,level12,level13,level14,level15,level16,level17,level18,level19,level20,level21,level22,level23,level24,level25,level26,level27,level28,level29,level30,level31,level32,level33,level34,level35,level36,level37,level38,level39,level40,level41,level42,level43,level44,level45,level46,level47,level48,level49,level50]
    



def Move(btnNo, newlevel):
   
    if btnNo == 1:
        gridX = 0
        gridY = 0
    
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
    Read(newlevel)

def Read(newlevel):
    int = 0
    for row in newlevel:
        for pos in row:
            if pos == 0:
                button_list[int].bg = "black"
                int = int + 1
            
            else:
                button_list[int].bg = "green"
                int = int + 1

title_box = Box(app, width="fill", align="top")
title = Text(title_box, text="title", align="left")

newlevel = levelList[0]

button_grid = Box(app, width="fill",height="fill",align="bottom", layout="grid")
button1 = PushButton(button_grid, text="1", grid=[0,0], width="4", height="2",command=Move(1,newlevel))
button2 = PushButton(button_grid, text="2", grid=[1,0], width="4", height="2")
button3 = PushButton(button_grid, text="3", grid=[2,0], width="4", height="2")
button4 = PushButton(button_grid, text="4", grid=[3,0], width="4", height="2")
button5 = PushButton(button_grid, text="5", grid=[4,0], width="4", height="2")
button6 = PushButton(button_grid, text="6", grid=[0,1], width="4", height="2")
button7 = PushButton(button_grid, text="7", grid=[1,1], width="4", height="2")
button8 = PushButton(button_grid, text="8", grid=[2,1], width="4", height="2")
button9 = PushButton(button_grid, text="9", grid=[3,1], width="4", height="2")
button10 = PushButton(button_grid, text="10", grid=[4,1], width="4", height="2")
button11 = PushButton(button_grid, text="11", grid=[0,2], width="4", height="2")
button12 = PushButton(button_grid, text="12", grid=[1,2], width="4", height="2")
button13 = PushButton(button_grid, text="13", grid=[2,2], width="4", height="2")
button14 = PushButton(button_grid, text="14", grid=[3,2], width="4", height="2")
button15 = PushButton(button_grid, text="15", grid=[4,2], width="4", height="2")
button16 = PushButton(button_grid, text="16", grid=[0,3], width="4", height="2")
button17 = PushButton(button_grid, text="17", grid=[1,3], width="4", height="2")
button18 = PushButton(button_grid, text="18", grid=[2,3], width="4", height="2")
button19 = PushButton(button_grid, text="19", grid=[3,3], width="4", height="2")
button20 = PushButton(button_grid, text="20", grid=[4,3], width="4", height="2")
button21 = PushButton(button_grid, text="21", grid=[0,4], width="4", height="2")
button22 = PushButton(button_grid, text="22", grid=[1,4], width="4", height="2")
button23 = PushButton(button_grid, text="23", grid=[2,4], width="4", height="2")
button24 = PushButton(button_grid, text="24", grid=[3,4], width="4", height="2")
button25 = PushButton(button_grid, text="        ", grid=[4,4], width="4", height="2")
button1.bg = "red"



button_list = [button1,button2,button3,button4,button5,button6,button7,button8,button9,button10,button11,button12,button13,button14,button15,button16,button17,button18,button19,button20,button21,button22,button23,button24,button25]





Read(newlevel)
app.display()
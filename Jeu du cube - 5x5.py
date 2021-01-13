import pandas as pd
import random
from tkinter import *

imax = 25

#jeu du cube pour générer un cube de 5 x 5
for round in range(100) :

    cube = pd.DataFrame(0, index = [1,2,3,4,5], columns = [1,2,3,4,5])
    
    i = 1
    x = 1
    y = 1
    cube.loc[1,1] = 1
    
    for turn in range (1,300) :
        move = random.randint(1,8)    
        
        if (move == 1 and x<4 and y<4) :
            new_x = x+2
            new_y = y+2
            new_i = i+1
            if cube.loc[new_y,new_x] == 0:
                cube.loc[new_y,new_x] = new_i
                x = new_x
                y = new_y
                i = new_i
        elif (move == 2 and x<4 and y>2) : 
            new_x = x+2
            new_y = y-2
            new_i = i+1
            if cube.loc[new_y,new_x] == 0:
                cube.loc[new_y,new_x] = new_i
                x = new_x
                y = new_y
                i = new_i
        elif (move == 3  and x>2 and y<4) :
            new_x = x-2
            new_y = y+2
            new_i = i+1
            if cube.loc[new_y,new_x] == 0:
                cube.loc[new_y,new_x] = new_i
                x = new_x
                y = new_y
                i = new_i
        elif (move == 4 and x>2 and y>2) :
            new_x = x-2
            new_y = y-2
            new_i = i+1
            if cube.loc[new_y,new_x] == 0:
                cube.loc[new_y,new_x] = new_i
                x = new_x
                y = new_y
                i = new_i
        elif (move == 5 and x<3) :
            new_x = x+3
            new_y = y
            new_i = i+1
            if cube.loc[new_y,new_x] == 0:
                cube.loc[new_y,new_x] = new_i
                x = new_x
                i = new_i
        elif (move == 6 and x>3) :
            new_x = x-3
            new_y = y
            new_i = i+1
            if cube.loc[new_y,new_x] == 0:
                cube.loc[new_y,new_x] = new_i
                x = new_x
                i = new_i
        elif (move == 7 and y<3) :
            new_y = y+3
            new_x = x
            new_i = i+1
            if cube.loc[new_y,new_x] == 0:
                cube.loc[new_y,new_x] = new_i
                y = new_y
                i = new_i
        elif (move == 8 and y>3) :
            new_y = y-3
            new_x = x
            new_i = i+1
            if cube.loc[new_y,new_x] == 0:
                cube.loc[new_y,new_x] = new_i
                y = new_y
                i = new_i
    
    if i >= imax :
        imax = i
        print('')
        print ("round : " + str(round) + ' - max i = ' + str(i))
        print(cube)
        break

    
#Caleb Callaway
#3/27/18
#betterColorWindow.py - color change window with lists


from ggame import *
from random import randint

def randcol(event):
    gnum = randint (1,4)
    if gnum == 1:
        col = Color(0x00FF00,1)
    elif gnum == 2:
        col = Color(0xFF0000,1)
    elif gnum == 3:
        col =  Color(0x0000FF,1)
    elif gnum == 4:
        col = Color(0X00000000,1)
    theRectangle = RectangleAsset(1500,1000,LineStyle(1,col),col)
    Sprite(theRectangle)



App().listenMouseEvent("click",randcol)
App().run()

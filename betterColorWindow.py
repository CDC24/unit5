#Caleb Callaway
#3/27/18
#betterColorWindow.py - color change window with lists


from ggame import *
from random import randint


colors = [Color(0x00FF00,1),Color(0xFF0000,1),(0x0000FF,1),(0X00000000,1)]

def randcol(event):
    gnum = randint (0,3)
    col = colors[gnum]
    theRectangle = RectangleAsset(1500,1000,LineStyle(1,col),col)
    Sprite(theRectangle)



App().listenMouseEvent("click",randcol)
App().run()

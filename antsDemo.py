#Caleb Callaway
#4/10/18
# antsDemo.py - lists with graphics

from ggame import *
from random import randint

ANTS = 10
WIDTH = 1000
HEIGHT= 500

if __name__ == "__main__":
    
    red = Color(0xFF0000,1)
    ant = CircleAsset(15,LineStyle(1,red),red)
    
    for i in range (ANTS):
        Sprite (ant)
    
    App().run()
#Caleb Callaway
#4/10/18
# antsDemo.py - lists with graphics

from ggame import *

ANTS = 10

if __name__ == "__main__":
    
    red = Color(0xFF0000,1)
    ant = CircleAsset(15,LineStyle(1,red),red)
    
    
    Sprite (ant)
    
App().run()
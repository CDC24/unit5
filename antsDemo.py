#Caleb Callaway
#4/10/18
# antsDemo.py - lists with graphics

from ggame import *
from random import randint

ANTS = 100
WIDTH = 1000
HEIGHT= 500


def step():                             #move each ant randomly in x and y
    for ant in data["antlist"]:
        ant.x += randint (-8,10)
        ant.y += randint (-8,10)

if __name__ == "__main__":             #putting ants on screen
    
    
    data = {}
    data["antlist"] = []                #list of ants
    
    red = Color(0xFF0000,1)
    ant = CircleAsset(5,LineStyle(1,red),red)
    
    for i in range (ANTS):
        #data["antlist"].append(Sprite (ant,(randint(1,WIDTH),randint(1,HEIGHT))))
        data["antlist"].append(Sprite (ant))
    
    App().run(step)
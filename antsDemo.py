#Caleb Callaway
#4/10/18
# antsDemo.py - lists with graphics

from ggame import *
from random import randint

ANTS = 200
WIDTH = 1000
HEIGHT= 500


def step():
    for ant in data["antlist"]:
        ant.x +=1
        ant.y +=1

if __name__ == "__main__":
    
    
    data = {}
    data["antlist"] = []
    
    red = Color(0xFF0000,1)
    ant = CircleAsset(5,LineStyle(1,red),red)
    
    for i in range (ANTS):
        data["antlist"].append(Sprite (ant,(randint(1,WIDTH),randint(1,HEIGHT))))
    
    App().run(step)
#Caleb Callaway
#3/30/18
#snow.py - pleasant snow


from ggame import *
from random import randint

FLAKES = 100
WIDTH = 1000
HEIGHT= 500


def step():                             #move each flake randomly in x and y
    for flake in data["flakelist"]:
        flake.x += randint (-2,2)
        flake.y += randint (0,3)

if __name__ == "__main__":             #putting flakes on screen
    
    
    data = {}
    data["flakelist"] = []                #list of flakes
    
    white = Color(0x000000,1)
    flake = CircleAsset(5,LineStyle(1,white),white)
    
    for i in range (FLAKES):
        data["flakelist"].append(Sprite (flake,(randint(1,WIDTH),randint(1,HEIGHT))))
    
    
    App().run(step)
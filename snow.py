#Caleb Callaway
#3/30/18
#snow.py - pleasant snow


from ggame import *
from random import randint

FLAKES = 100
WIDTH = 1000
HEIGHT= 500


def step():                     #move each flake randomly in x and y
    data["frames"] += 1
    for flake in data["flakelist"]:
        flake.x += randint (-3,2)
        flake.y += randint (0,3)
    if data["frames"]%300 == 0:
        for i in range (FLAKES/10):
            data["flakelist"].append(Sprite (flake,(randint(1,WIDTH),0)))
            
        
    
        moveBanana()  
         

if __name__ == "__main__":             #putting flakes on screen
    
    
    data = {}
    data["flakelist"] = []                #list of flakes
    data["frames"] = 0
    
    white = Color(0xFFFFFF,1)
    black = Color(0x000000,0.5)
    background = RectangleAsset(1000,500,LineStyle(1,black),black)
    flake = CircleAsset(5,LineStyle(1,white),white)
    
    Sprite(background)
    for i in range (FLAKES):
        data["flakelist"].append(Sprite (flake,(randint(1,WIDTH),randint(1,HEIGHT))))
    
    
    App().run(step)
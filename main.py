from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import config
import os
import random

# Variables and Core functions

def randByte():
    return random.randint(0, 255)

def changePlayerColor(plr:FirstPersonController):
    plr.color = color.rgb(randByte(), randByte(), randByte())

# Game Configs

CONFIGS = config.edit()

dtext = CONFIGS.get("dtext")

if dtext != "dirt.png":
    os.system(f"cp {dtext} ./dirt.png")


# Ursina Configs

window.borderless = False
window.size = Vec2(1200, 660)
game = Ursina()
player = FirstPersonController()
player.model = "cube"
player.set_position(Vec3(0, 16, 0))

skybox = Sky()
skybox.texture = "sky.png"

print(player.X, player.Y, player.Z)
window.set_cursor_hidden(True)
mouse.locked = True

# Terrain

boxes = []

def gen():
    for i in range(0, 20):
        for j in range(0, 20):
            box = Button(color=color.white, model="cube", position=(j, 0, i), parent=scene, origin_y=random.randrange(0, 2, 1), texture="dirt.png")
            
            boxes.append(box)

gen()

# Functions

def click_spawn():
    print_on_screen("this is the spawn point. not destroyable.")



def go_to_spawn():
    player.position = Vec3(0, 0, 0)


        
def fix_spawn():
    spawn:Button = boxes[0]
    boxes.remove(spawn)

    spawn.on_click = click_spawn

    spawn.texture = "spawn.png"

fix_spawn()




# Ursina Functions

def input(key):
    if key == "left mouse down":
        for box in boxes:
            if box.hovered:
                boxes.remove(box)
                box.visible = False
                box.disable()
                
                
    elif key == "tab":
        mouse.locked = not mouse.locked
        # player.cursor.visible = not player.cursor.visible
        # mouse.visible = not mouse.visible
        

    elif key == "escape":
        game.userExit()

    elif key == "backspace":
        go_to_spawn()
        
    elif key == "r":
        for v in boxes:
            box:Button = v
            
            box.visible = False
            box.disable()
            boxes.remove(box)
        
        gen()
                
        # fix_spawn()
        go_to_spawn()
        print_on_screen("World regenerated.")
        
    elif key == "m":
        changePlayerColor(player)
                

def update():
    if held_keys["right mouse"]:
       for box in boxes:
            if box.hovered:
                boxes.remove(box)
                box.visible = False
                box.disable() 
                
                ()
                
    if player.Y == -60:
        go_to_spawn()
        
    changePlayerColor(player)

# Run the game

game.run()
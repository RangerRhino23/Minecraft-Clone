from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import assets.APIs.first_person_movement_api as fpm
from assets.APIs.block import *
import random as r

app = Ursina()
Sky(texture='assets/textures/sky.png')
player_speed = 15

world = []

def update():
    fpm.player_movement(player,player_speed)


def input(key):
    if key == 'q':
        quit()
    if key == 'g':
        EditorCamera()


player = FirstPersonController(position=(2,2,2))

world_size = 40
for x in range(world_size):
    for z in range(world_size):
        block = Block(position=(x,0,z),side_textures='assets/textures/grass_side.png',top_texture='assets/textures/grass_top.png', bottom_texture='assets/textures/dirt_side.png', visible=(True,False,False,False,False,False))


for i in range(10):
    tree = Tree(position=(r.randint(0,world_size),1,r.randint(0,world_size)), height=r.randint(2,7))


app.run()
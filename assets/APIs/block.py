from ursina import *


class Block(Entity):
    def __init__(self, position, top_texture, side_textures, bottom_texture, visible):
        super().__init__()
        if visible[0] == True:
            self.cube_top = Entity(model='quad', texture=top_texture, position=(position), rotation_x=90, collider='box', visible=visible[0])
        if visible[1] == True:
            self.cube_side = Entity(model='quad', texture=side_textures, position=position+(0,-0.5,-0.5), rotation_y=0, collider='box')
        if visible[2] == True:
            self.cube_side = Entity(model='quad', texture=side_textures, position=position+(0,-0.5,.5), rotation_y=180, collider='box')
        if visible[3] == True:
            self.cube_side = Entity(model='quad', texture=side_textures, position=position+(-0.5,-0.5,0), rotation_y=90, collider='box')
        if visible[4] == True:
            self.cube_side = Entity(model='quad', texture=side_textures, position=position+(0.5,-0.5,0), rotation_y=270, collider='box')
        if visible[5] == True:
            self.cube_bottom = Entity(model='quad', texture=bottom_texture, position=position+(0,-1,0), rotation_x=270, collider='box')

class Tree():
    def __init__(self, position, height):
        super().__init__()
        #Build Trunk
        for y in range(height):
            y += position[1]
            trunk = Block((position[0],y,position[2]),top_texture='assets/textures/log_top.png',side_textures='assets/textures/log_side.png', bottom_texture='assets/textures/log_top.png', visible=(False,True,True,True,True,False))
        leave = Block((position[0],y+1,position[2]), top_texture='assets/textures/leaves_side.png', side_textures='assets/textures/leaves_side.png', bottom_texture='assets/textures/leaves_side.png', visible=(True,True,True,True,True,True))
        leave = Block((position[0]+1,y,position[2]+1), top_texture='assets/textures/leaves_side.png', side_textures='assets/textures/leaves_side.png', bottom_texture='assets/textures/leaves_side.png', visible=(True,True,True,True,True,True))
        leave = Block((position[0]-1,y,position[2]+1), top_texture='assets/textures/leaves_side.png', side_textures='assets/textures/leaves_side.png', bottom_texture='assets/textures/leaves_side.png', visible=(True,True,True,True,True,True))
        leave = Block((position[0]-1,y,position[2]-1), top_texture='assets/textures/leaves_side.png', side_textures='assets/textures/leaves_side.png', bottom_texture='assets/textures/leaves_side.png', visible=(True,True,True,True,True,True))
        leave = Block((position[0]+1,y,position[2]-1), top_texture='assets/textures/leaves_side.png', side_textures='assets/textures/leaves_side.png', bottom_texture='assets/textures/leaves_side.png', visible=(True,True,True,True,True,True))
        leave = Block((position[0]+1,y,position[2]), top_texture='assets/textures/leaves_side.png', side_textures='assets/textures/leaves_side.png', bottom_texture='assets/textures/leaves_side.png', visible=(True,True,True,True,True,True))
        leave = Block((position[0]-1,y,position[2]), top_texture='assets/textures/leaves_side.png', side_textures='assets/textures/leaves_side.png', bottom_texture='assets/textures/leaves_side.png', visible=(True,True,True,True,True,True))
        leave = Block((position[0],y,position[2]+1), top_texture='assets/textures/leaves_side.png', side_textures='assets/textures/leaves_side.png', bottom_texture='assets/textures/leaves_side.png', visible=(True,True,True,True,True,True))
        leave = Block((position[0],y,position[2]-1), top_texture='assets/textures/leaves_side.png', side_textures='assets/textures/leaves_side.png', bottom_texture='assets/textures/leaves_side.png', visible=(True,True,True,True,True,True))
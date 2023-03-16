from ursina import *

#Version: 1.2

###REQUIREMENTS###
#Controls config file v1.0 or later

###SETUP###
#Import api: import assets.APIs.first_person_movement_api as fpm

#In update function (def update():): fpm.player_movement(player)


def player_movement(player, base_speed):
    camera.fov = 90
    camera.y = 0
    player.speed = base_speed
    #Sprint, Crouch, Zoom
    if held_keys['r']:
        player.speed = base_speed + 5
    if held_keys['left shift']:
        camera.y = -0.25
        player.speed = base_speed - 8
    if held_keys['c']:
        camera.fov = 60

def player_movement_controls(player, base_speed, controls):
    camera.fov = 90
    camera.y = 0
    player.speed = base_speed
    #Sprint, Crouch, Zoom
    if held_keys[controls.sprint_control]:
        player.speed = base_speed + 5
    if held_keys[controls.crouch_control]:
        camera.y = -0.25
        player.speed = base_speed - 5
    if held_keys[controls.zoom_control]:
        camera.fov = 60
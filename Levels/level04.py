from ursina import *
from player import Player
import sys
sys.path.append('../Parkour/')
from block import *

# App/Window
app = Ursina()

normalSpeed = 2
boostSpeed  = 3

normalJump = 0.3

# Player
player = Player("cube", (0, 10, 0), "box", controls='wasd')
player.SPEED = normalSpeed
player.jump_height = normalJump

# Sky
sky = Sky(texture = "../assets/sky")

# Lighting
light = PointLight(parent = camera, position = (0, 10, -1.5))
light.color = color.white

AmbientLight(color = color.rgba(100, 100, 100, 0.1))

#Level04
ground_4 = Entity(model = "cube", scale_x = 10, scale_z = 10, collider = "box", texture = "white_cube", color = "#CACACA")

block_4_1 = NormalBlock(position = (0, 1, 12))
block_4_2 = NormalBlock(position = (0, 2, 20))
block_4_3 = JumpBlock(position = (0, -49, 40))
block_4_4 = NormalBlock(position = (0, 50, 60))
block_4_5 = SpeedBlock(position = (0, 50, 93), scale = (3, 0.5, 50))
block_4_6 = JumpBlock(position = (0, 15, 163))

finishBlock_4 = Entity(model = "cube", scale_x = 10, scale_z = 10, collider = "box", texture = "white_cube", color = "#CACACA", position = (0, 20, 240))

def speed():
    player.SPEED = normalSpeed

def update():
    # Escape button quits
    if held_keys["escape"]:
        application.quit()

    # Stops the player from falling forever
    if player.position.y <= -50:
        player.position = Vec3(0, 5, 0)
        player.SPEED = normalSpeed
        player.jump_height = normalJump

    # Restart the level
    if held_keys["g"]:
        player.position = Vec3(0, 5, 0)
        player.SPEED = normalSpeed
        player.jump_height = normalJump

    # What entity the player hits
    hit = raycast(player.position, player.down, distance = 2, ignore = [player,])

    if hit.entity == block_4_3:
        player.jump_height = 2
    elif hit.entity != block_4_3:
        player.jump_height = normalJump

    if hit.entity == block_4_5:
        player.SPEED = boostSpeed * 2

    if hit.entity == block_4_6:
        player.jump_height = 1.3
    
app.run()

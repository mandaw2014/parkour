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

# Level 02 platforms
ground_2 = Entity(model = "cube", scale_x = 10, scale_z = 10, collider = "box", texture = "white_cube", color = "#CACACA")
finishBlock_2 = Entity(model = "cube", scale_x = 5, scale_z = 5, collider = "box", texture = "white_cube", color = "#CACACA", position = (0, 11, 67))

block_2 = NormalBlock(position = (0, 1, 9))
block_2_1 = NormalBlock(position = (0, 2, 15))
block_2_2 = JumpBlock(position = (0, -20, 25))
block_2_3 = NormalBlock(position = (0, 10, 30))
block_2_4 = NormalBlock(position = (0, 10, 37))
block_2_5 = SpeedBlock(position = (0, 10, 45))
block_2_6 = NormalBlock(position = (0, 11, 60))

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
    
    if block_2_2.enabled == True:
        if hit.entity == block_2_2:
            player.jump_height = 1.2
        elif hit.entity != block_2_2:
            player.jump_height = normalJump

    if block_2_5.enabled == True:
        if hit.entity == block_2_5:
            player.SPEED = boostSpeed * 1.5
            invoke(speed, delay=3)

app.run()
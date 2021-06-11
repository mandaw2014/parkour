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

ground_2 = StartBlock()

block_2_1 = NormalBlock(position = (0, 1, 12))
block_2_2 = NormalBlock(position = (0, 2, 20))
block_2_3 = JumpBlock(position = (0, -20, 30))
block_2_4 = NormalBlock(position = (0, 10, 42))
block_2_5 = NormalBlock(position = (0, 10, 50))
block_2_6 = SpeedBlock(position = (0, 10, 62))
block_2_7 = NormalBlock(position = (0, 11, 74))

finishBlock_2 = EndBlock(position = (0, 11, 88))

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
        if hit.entity == block_2_3:
            player.jump_height = 1.2
        elif hit.entity != block_2_3:
            player.jump_height = normalJump

    if block_2_6.enabled == True:
        if hit.entity == block_2_6:
            player.SPEED = boostSpeed * 1.5
            invoke(speed, delay=3)

app.run()

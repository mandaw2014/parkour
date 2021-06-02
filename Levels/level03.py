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

#Level03
ground_3 = StartBlock()

block_3_1 = NormalBlock(position = (0, 1, 10))
block_3_2 = NormalBlock(position = (0, 2, 18))
block_3_3 = NormalBlock(position = (8, 3, 18))
block_3_4 = NormalBlock(position = (16, 4, 18))
block_3_5 = NormalBlock(position = (16, 5, 10))
block_3_6 = NormalBlock(position = (16, 6, 2))
block_3_7 = NormalBlock(position = (8, 7, 2))
block_3_8 = NormalBlock(position = (8, 8, 10))
block_3_9 = NormalBlock(position = (8, 9, 18))
block_3_10 = NormalBlock(position = (16, 10, 18))
block_3_11 = NormalBlock(position = (16, 11, 10))
block_3_12 = NormalBlock(position = (16, 12, 2))
block_3_13 = NormalBlock(position = (8, 13, 2))
block_3_14 = NormalBlock(position = (8, 14, -6))
block_3_15 = JumpBlock(position = (8, 12, -15))
block_3_16 = JumpBlock(position = (8, 35, -25))

finishBlock_3 = EndBlock(position = (8, 80, -10))

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
        camera.rotation = (0, 0, 0)

    # Restart the level
    if held_keys["g"]:
        player.position = Vec3(0, 5, 0)
        player.SPEED = normalSpeed
        player.jump_height = normalJump
        camera.rotation = (0, 0, 0)

    # What entity the player hits
    hit = raycast(player.position, player.down, distance = 2, ignore = [player,])

    if hit.entity == block_3_15:
        player.jump_height = 1.2
    if hit.entity == block_3_16:
        player.jump_height = 1.4

app.run()

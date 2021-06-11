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

#Level01
block_1_1 = NormalBlock(position = (0, 1, 12))
block_1_2 = NormalBlock(position = (0, 2, 20))
block_1_3 = NormalBlock(position = (0, 3, 28))
block_1_4 = NormalBlock(position = (0, 4, 36))
block_1_5 = NormalBlock(position = (8, 5, 36))
block_1_6 = NormalBlock(position = (16, 6, 36))
block_1_7 = JumpBlock(position = (24, 2, 36))
block_1_8 = NormalBlock(position = (32, 10, 36))
block_1_9 = SpeedBlock(position = (32, 10, 46))

ground_1 = StartBlock()
finishBlock_1 = EndBlock(position = (32, 10, 62))

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
    
    if hit.entity == block_1_7:
        player.jump_height = 0.7
    elif hit.entity != block_1_7:
        player.jump_height = normalJump

    if hit.entity == block_1_9:
        player.SPEED = boostSpeed * 1.2
        invoke(speed, delay=3)

app.run()

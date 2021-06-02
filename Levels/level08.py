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

# Level 08 platforms
ground_8 = StartBlock()
block_8_1 = NormalBlock(position = (0, 0, 13))
block_8_2 = NormalBlock(position = (0, -20, 19))
block_8_3 = SlowBlock(position = (0, -20, 31))
block_8_4 = NormalBlock(position = (0, -20, 43))
block_8_5 = NormalBlock(position = (0, -20, 50))
block_8_6 = NormalBlock(position = (0, -20, 57))
block_8_7 = NormalBlock(position = (0, -20, 64))
block_8_8 = NormalBlock(position = (0, -22, 72))
block_8_9 = NormalBlock(position = (0, -24, 80))
block_8_10 = NormalBlock(position = (0, -26, 88))
block_8_11 = SpeedBlock(position = (0, -26, 98))

finishBlock_8 = EndBlock(position = (0, -10, 350))

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
    if hit.entity == block_8_3:
        player.SPEED = 1
    if hit.entity == block_8_11:
        player.SPEED = boostSpeed * 5.5
        player.jump_height = 1.4

app.run()
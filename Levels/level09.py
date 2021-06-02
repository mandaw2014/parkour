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

# Level 09 platforms
ground_9 = StartBlock()
block_9_1 = NormalBlock(position = (0, 1, 13))
block_9_2 = FakeBlock(position = (0, 1, 22))
block_9_3 = NormalBlock(position = (-6, 1, 22))
block_9_4 = NormalBlock(position = (6, 1, 22))
block_9_5 = NormalBlock(position = (0, 1, 29))
block_9_6 = FakeBlock(position = (0, 1, 40))
block_9_7 = NormalBlock(position = (0, -49, 40))
block_9_8 = JumpBlock(position = (0, -49, 51))
block_9_9 = FakeBlock(position = (0, 100, 70))
block_9_10 = NormalBlock(position = (0, 100, 80))
block_9_11 = SpeedBlock(position = (0, 100, 90))

finishBlock_9 = EndBlock(position = (0, 150, 300))

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
    if hit.entity == block_9_8:
        player.jump_height = 3
    elif hit.entity != block_9_8:
        player.jump_height = normalJump
    if hit.entity == block_9_11:
        player.SPEED = boostSpeed * 4
        player.jump_height = 2


app.run()
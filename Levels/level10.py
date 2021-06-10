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

# Level 10 platforms
ground_10 = StartBlock()
block_10_1 = NormalBlock(position = (0, 1, 13))
block_10_2 = SpeedBlock(position = (0, 1, 25))
block_10_3 = JumpBlock(position = (0, -10, 70))
block_10_4 = FakeBlock(position = (0, 10, 150))
block_10_5 = NormalBlock(position = (0, 10, 160))
block_10_6 = Wall(position = (0, 11, 165))
block_10_7 = NormalBlock(position = (0, 10, 170))
block_10_8 = Wall(position = (0, 11, 175))
block_10_9 = NormalBlock(position = (0, 10, 180))
block_10_10 = NormalBlock(position = (0, 10, 190))
block_10_11 = NormalBlock(position = (-5, 11, 190))
block_10_12 = NormalBlock(position = (-10, 12, 190))
block_10_13 = NormalBlock(position = (-10, 13, 185))
block_10_14 = NormalBlock(position = (-10, 14, 180))
block_10_15 = NormalBlock(position = (-10, 15, 175))
block_10_16 = NormalBlock(position = (-5, 16, 175))
block_10_17 = NormalBlock(position = (0, 17, 175))
block_10_18 = NormalBlock(position = (0, 18, 185))
block_10_19 = NormalBlock(position = (0, 19, 195))
block_10_20 = NormalBlock(position = (0, 20, 205))
block_10_21 = WeirdBlock(position = (0, 20, 220))
block_10_22 = NormalBlock(position = (0, 20, 233))
block_10_23 = NormalBlock(position = (0, 20, 243))
block_10_24 = NormalBlock(position = (0, 20, 253))
block_10_25 = NormalBlock(position = (0, 20, 263))

finishBlock_10 = EndBlock(position = (0, 20, 275))


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
    if hit.entity == block_10_2:
        player.SPEED = boostSpeed * 2.3
    if hit.entity == block_10_3:
        player.jump_height = 1.3
    elif hit.entity != block_10_3:
        player.jump_height = normalJump
    if hit.entity == block_10_5 or hit.entity == block_10_7 or hit.entity == block_10_9 or hit.entity == block_10_10 or hit.entity == block_10_11 or hit.entity == block_10_12 or hit.entity == block_10_13 or hit.entity == block_10_14 or hit.entity == block_10_15 or hit.entity == block_10_16 or hit.entity == block_10_17 or hit.entity == block_10_18 or hit.entity == block_10_19 or hit.entity == block_10_20:
        player.SPEED = normalSpeed
        player.jump_height = normalJump
    if hit.entity == block_10_21:
        camera.rotation_z = 180
    if hit.entity == finishBlock_10:
        camera.rotation_z = 0
    

app.run()
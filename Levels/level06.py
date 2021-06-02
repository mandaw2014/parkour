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

# Level 03 platforms
ground_6 = Entity(model = "cube", scale_x = 10, scale_z = 10, collider = "box", texture = "white_cube", color = "#CACACA")
block_6_1 = SpeedBlock(position = (0, 0, 13))
block_6_2 = SpeedBlock(position = (0, 0, 32))
block_6_3 = SpeedBlock(position = (0, 0, 58))
block_6_4 = SpeedBlock(position = (0, 0, 90))
block_6_5 = SpeedBlock(position = (0, 0, 130))
block_6_6 = SpeedBlock(position = (0, 0, 180))
block_6_7 = SpeedBlock(position = (0, 0, 240))
block_6_8 = SlowBlock(position = (0, 0, 300))

finishBlock_6 = Entity(model = "cube", scale_x = 10, scale_z = 10, collider = "box", texture = "white_cube", color = "#CACACA", position = (0, 0, 315))

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

    if hit.entity == block_6_1:
        player.SPEED = boostSpeed * 1.5
    if hit.entity == block_6_2:
        player.SPEED = boostSpeed * 2
    if hit.entity == block_6_3:
        player.SPEED = boostSpeed * 2.5
    if hit.entity == block_6_4:
        player.SPEED = boostSpeed * 3
    if hit.entity == block_6_5:
        player.SPEED = boostSpeed * 4.5
    if hit.entity == block_6_6:
        player.SPEED = boostSpeed * 5
    if hit.entity == block_6_7:
        player.SPEED = boostSpeed * 5.5
    if hit.entity == block_6_8:
        player.SPEED = normalSpeed

app.run()
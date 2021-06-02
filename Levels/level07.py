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

# Level 07 platforms
ground_7 = Entity(model = "cube", scale_x = 10, scale_z = 10, collider = "box", texture = "white_cube", color = "#CACACA")
block_7_1 = NormalBlock(position = (0, 1, 10))
block_7_2 = Wall(position = (0, 3, 15))
block_7_3 = NormalBlock(position = (0, 1, 20))
block_7_4 = Wall(position = (0, 3, 25))
block_7_5 = NormalBlock(position = (0, 1, 30))
block_7_6 = Wall(position = (0, 3, 35))
block_7_7 = NormalBlock(position = (0, 1, 40))
block_7_8 = Wall(position = (0, 3, 45))
block_7_9 = NormalBlock(position = (0, 1, 50))
block_7_10 = Wall(position = (0, 3, 55))
block_7_11 = NormalBlock(position = (0, 1, 60))
block_7_12 = WeirdBlock(position = (0, 1, 73))
block_7_13 = NormalBlock(position = (0, 1, 85))

finishBlock_7 = Entity(model = "cube", scale_x = 10, scale_z = 10, collider = "box", texture = "white_cube", color = "#CACACA", position = (0, 1, 95))

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
    if hit.entity == block_7_12:
        camera.rotation_z = 180
    if hit.entity == finishBlock_7:
        camera.rotation = (0, 0, 0)

app.run()
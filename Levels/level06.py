from ursina import *
from player import Player

# App/Window
app = Ursina()

normalSpeed = 2
boostSpeed  = 3

normalJump = 0.3

# Normal Block Class
class NormalBlock(Entity):
    def __init__(self, position = (0, 0, 0)):
        super().__init__(
            model = "cube",
            scale = Vec3(3, 0.8, 3),
            color = "#AFFF3C",
            collider = "box",
            texture = "white_cube",
            position = position,
        )

# Jump Block Class
class JumpBlock(Entity):
    def __init__(self, position = (0, 0, 0)):
        super().__init__(
            model = "cube",
            scale = Vec3(3, 0.8, 3),
            color = "#FF8B00",
            collider = "box",
            texture = "white_cube",
            position = position,
        )

# Speed Block Class
class SpeedBlock(Entity):
    def __init__(self, position = (0, 0, 0)):
        super().__init__(
            model = "cube",
            scale = Vec3(3, 0.5, 8),
            color = "#53FFF5",
            collider = "box",
            texture = "white_cube",
            position = position,
        )

# Slow Block Class
class SlowBlock(Entity):
    def __init__(self, position = (0, 0, 0)):
        super().__init__(
            model = "cube",
            scale = Vec3(3, 0.5, 15),
            color = "#FF453F",
            collider = "box",
            texture = "white_cube",
            position = position,
        )

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
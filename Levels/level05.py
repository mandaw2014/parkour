from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from player import Player

# App/Window
app = Ursina()

normalSpeed = 2
boostSpeed  = 3

normalJump = 0.3

# Normal Block Class
class NormalBlock(Entity):
    def __init__(self, position = (0, 0, 0), rotation = (0, 0, 0)):
        super().__init__(
            model = "cube",
            scale = Vec3(3, 0.8, 3),
            color = "#AFFF3C",
            collider = "box",
            texture = "white_cube",
            position = position,
            rotation = rotation
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
    def __init__(self, position = (0, 0, 0), scale = (3, 0.5, 8)):
        super().__init__(
            model = "cube",
            scale = scale,
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

class WeirdBlock(Entity):
    def __init__(self, position = (0, 0, 0)):
        super().__init__(
            model = "cube",
            scale = Vec3(3, 0.5, 15),
            color = "#7116FE",
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

#Level05
ground_5 = Entity(model = "cube", scale_x = 10, scale_z = 10, collider = "box", texture = "white_cube", color = "#CACACA")

block_5_1 = NormalBlock(position = (0, 1, 10))
block_5_2 = NormalBlock(position = (-4, 1, 18), rotation = (0, 0, 30))
block_5_3 = NormalBlock(position = (4, 1, 26), rotation = (0, 0, -30))
block_5_4 = NormalBlock(position = (-4, 1, 34), rotation = (0, 0, 30))
block_5_5 = NormalBlock(position = (4, 1, 42), rotation = (0, 0, -30))
block_5_6 = NormalBlock(position = (-4, 1, 50), rotation = (0, 0, 30))
block_5_7 = NormalBlock(position = (4, 1, 58), rotation = (0, 0, -30))
block_5_8 = NormalBlock(position = (-4, 1, 66), rotation = (0, 0, 30))

block_5_9 = SpeedBlock(position = (0, 1, 78))
block_5_10 = WeirdBlock(position = (0, 1, 95))

finishBlock_5 = Entity(model = "cube", scale_x = 10, scale_z = 10, collider = "box", texture = "white_cube", color = "#CACACA", position = (0, 1, 112))

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

    if hit.entity == block_5_9:
        player.SPEED = boostSpeed * 2
    elif hit.entity == block_5_9:
        invoke(speed, delay = 1)

    if hit.entity == block_5_10:
        camera.rotation_z = 180
    if hit.entity == finishBlock_5:
        camera.rotation = (0, 0, 0)

app.run()

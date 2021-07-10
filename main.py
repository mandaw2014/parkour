from ursina import *
from player import Player
from block import *

from Levels.level01 import Level01

from main_menu import MainMenu
from pause_menu import PauseMenu

application.development_mode = True

# App/Window
app = Ursina(borderless = False)

window.title = "Parkour"
window.fps_counter.disable()

window.exit_button = False

normalSpeed = 2
boostSpeed  = 3

normalJump = 0.3

# Player
player = Player("cube", (500, 500, 0), "box", controls="wasd")
player.SPEED = normalSpeed
player.jump_height = normalJump
player.disable()

mouse.locked = False

m = MainMenu()
m.player = player

sky = Sky(texture = "./assets/sky")

# Lighting
PointLight(parent = camera, position = (0, 10, -1.5), color = color.white)
AmbientLight(color = color.rgba(100, 100, 100, 0.1))

level01 = Level01()
level01.player = player
player.position = (888, 10, 18)
player.rotation = (0, -141.511, 0)

def reset_player():
    player.position = (0, 3, 0)
    player.SPEED = normalSpeed
    player.jump_height = normalJump
    camera.rotation_z = 0

def input(key):
    if key == "escape":
        mouse.locked = False
        player.disable()
        player.time_running = False
        player.time.disable()
        
        p = PauseMenu()
        p.player = player

def update():
    # Stops the player from falling forever
    if player.position.y <= -50:
        player.position = (888, 10, 18)
        player.SPEED = normalSpeed
        player.jump_height = normalJump
        camera.rotation_z = 0

    # Restart the level
    if held_keys["g"]:
        player.position = (888, 10, 18)
        player.SPEED = normalSpeed
        player.jump_height = normalJump
        camera.rotation_z = 0

    ray = raycast(player.position, player.down, distance = 2, ignore = [player, ])

app.run()

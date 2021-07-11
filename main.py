from ursina import *
from player import Player
from block import *

from Levels.level01 import Level01
from Levels.level02 import Level02
from Levels.level03 import Level03

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
player = Player("cube", (0, 10, 0), "box", controls="wasd")
player.SPEED = normalSpeed
player.jump_height = normalJump
player.disable()
player.position = (888, 10, 18)
player.rotation = (0, 181, 0)

mouse.locked = False

m = MainMenu()
m.player = player

sky = Sky(texture = "./assets/sky")

# Lighting
PointLight(parent = camera, position = (0, 10, -1.5), color = color.white)
AmbientLight(color = color.rgba(100, 100, 100, 0.1))

level01 = Level01()
level01.player = player

level02 = Level02()
level02.player = player

level03 = Level03()
level03.player = player

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
    ray = raycast(player.position, player.down, distance = 2, ignore = [player, ])

    if ray.entity == level01.finishBlock_1:
        player.position = (811, 14, 108)
        player.rotation = (0, -267, 0)

        level01.disable()
        level02.enable()

    if ray.entity == level02.finishBlock_2:
        player.position = (809, 4, 106)
        player.rotation = (0, 181, 0)

        level02.disable()
        level03.enable()

    print(round(player.position, 0), round(player.rotation, 0))

app.run()

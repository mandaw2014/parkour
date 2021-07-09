from ursina import *
from player import Player
from block import *

from Levels.level01 import Level01
from Levels.level02 import Level02
from Levels.level03 import Level03
from Levels.level04 import Level04
from Levels.level05 import Level05
from Levels.level06 import Level06
from Levels.level07 import Level07
from Levels.level08 import Level08
from Levels.level09 import Level09
from Levels.level10 import Level10

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

level04 = Level04()
level04.player = player

level05 = Level05()
level05.player = player

level06 = Level06()
level06.player = player

level07 = Level07()
level07.player = player

level08 = Level08()
level08.player = player

level09 = Level09()
level09.player = player

level10 = Level10()
level10.player = player

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
        player.position = Vec3(0, 5, 0)
        player.SPEED = normalSpeed
        player.jump_height = normalJump
        camera.rotation_z = 0

    # Restart the level
    if held_keys["g"]:
        player.position = Vec3(0, 5, 0)
        player.SPEED = normalSpeed
        player.jump_height = normalJump
        camera.rotation_z = 0

    ray = raycast(player.position, player.down, distance = 2, ignore = [player, ])

    if ray.entity == level01.finishBlock_1:
        level02.enable()
        level01.disable()
        reset_player()
    if ray.entity == level02.finishBlock_2:
        level03.enable()
        level02.disable()
        reset_player()
    if ray.entity == level03.finishBlock_3:
        level04.enable()
        level03.disable()
        reset_player()
    if ray.entity == level04.finishBlock_4:
        level05.enable()
        level04.disable()
        reset_player()
    if ray.entity == level05.finishBlock_5:
        level06.enable()
        level05.disable()
        reset_player()
    if ray.entity == level06.finishBlock_6:
        level07.enable()
        level06.disable()
        reset_player()
    if ray.entity == level07.finishBlock_7:
        level08.enable()
        level07.disable()
        reset_player()
    if ray.entity == level08.finishBlock_8:
        level09.enable()
        level08.disable()
        reset_player()
    if ray.entity == level09.finishBlock_9:
        level10.enable()
        level09.disable()
        reset_player()
    if ray.entity == level10.finishBlock_10:
        m.main_menu.enable()
        player.disable()
        mouse.locked = False
        level01.enable()
        level10.disable()
        reset_player()

app.run()

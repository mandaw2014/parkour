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
player.position = (888, 12, 18)
player.rotation = (0, -142, 0)

mouse.locked = False

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

m = MainMenu()
m.player = player
m.level01 = level01
m.level02 = level02
m.level03 = level03
m.level04 = level04
m.level05 = level05
m.level06 = level06
m.level07 = level07
m.level08 = level08
m.level09 = level09

sky = Sky(texture = "sky")

# Lighting
light = PointLight(parent = camera, position = (0, 10, -1.5), color = color.white)
AmbientLight(color = color.rgba(100, 100, 100, 0.1))

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
        p.level01 = level01
        p.level02 = level02
        p.level03 = level03
        p.level04 = level04
        p.level05 = level05
        p.level06 = level06
        p.level07 = level07
        p.level08 = level08
        p.level09 = level09

def update():
    ray = raycast(player.position, player.forward, distance = 2, ignore = [player, ])

    if ray.entity == level01.finishBlock_1:
        player.position = (811, 14, 108)
        player.rotation = (0, -267, 0)
        player.SPEED = normalSpeed
        player.jump_height = normalJump
        player.count = 0.0

        level01.disable()
        level02.enable()

    if ray.entity == level02.finishBlock_2:
        player.position = (809, 4, 106)
        player.rotation = (0, 181, 0)
        player.SPEED = normalSpeed
        player.jump_height = normalJump
        player.count = 0.0

        level02.disable()
        level03.enable()
    
    if ray.entity == level03.finishBlock_3:
        player.position = (5, 10, -150)
        player.rotation = (0, -90, 0)
        player.SPEED = normalSpeed
        player.jump_height = normalJump
        player.count = 0.0

        level03.disable()
        level04.enable()

    if ray.entity == level04.finishBlock_4:
        player.position = (-1, -5, 34)
        player.rotation = (0, -180, 0)
        player.SPEED = normalSpeed
        player.jump_height = normalJump
        player.count = 0.0

        level04.disable()
        level05.enable()

    if ray.entity == level05.finishBlock_5:
        player.position = (130, -120, 0)
        player.rotation = (0, -90, 0)
        player.SPEED = normalSpeed
        player.jump_height = normalJump
        player.count = 0.0

        level05.disable()
        level06.enable()

    if ray.entity == level06.finishBlock_6:
        player.position = (0, 10, 0)
        player.rotation = (0, 0, 0)
        player.SPEED = normalSpeed
        player.jump_height = normalJump
        player.count = 0.0

        level06.disable()
        level07.enable()

    if ray.entity == level07.finishBlock_7:
        player.position = (0, 10, 0)
        player.rotation = (0, 0, 0)
        player.SPEED = normalSpeed
        player.jump_height = normalJump
        player.count = 0.0

        level07.disable()
        level08.enable()

    if ray.entity == level08.finishBlock_8:
        player.position = (0, 10, 0)
        player.rotation = (0, 0, 0)
        player.SPEED = normalSpeed
        player.jump_height = normalJump
        player.count = 0.0

        level08.disable()
        level09.enable()

    if ray.entity == level09.finishBlock_9:
        player.position = (888, 12, 18)
        player.rotation = (0, -142, 0)
        player.SPEED = normalSpeed
        player.jump_height = normalJump
        player.count = 0.0

        player.disable()
        mouse.locked = False
        m.main_menu.enable()
        player.time_running = False

        level09.disable()
        level01.enable()

    print(round(player.position, 0), round(player.rotation, 0))

app.run()

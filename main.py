from ursina import *
from player import Player
from block import *

application.development_mode = True

# App/Window
app = Ursina()

window.title = "Parkour"
window.fps_counter.disable()

window.borderless = False
window.exit_button = False

normalSpeed = 2
boostSpeed  = 3

normalJump = 0.3

# Player
player = Player("cube", (0, 10, 0), "box", controls="wasd")
player.SPEED = normalSpeed
player.jump_height = normalJump

# Main Menu
class MainMenu(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui
        )

        self.main_menu = Entity(parent = self, enabled = True)

        def start():
            player.enable()
            mouse.locked = True
            self.main_menu.disable()

        title = Entity(model = "quad", scale = (0.65, 0.2, 0.2), texture = "assets/parkour_logo_4", parent = self.main_menu, y = 0.3)

        start_button = Button(text = "S t a r t - G a m e", color = color.black, scale_y = 0.1, scale_x = 0.3, y = -0.1, parent = self.main_menu)
        quit_button = Button(text = "Q u i t", color = color.black, scale_y = 0.1, scale_x = 0.3, y = -0.22, parent = self.main_menu)
        quit_button.on_click = application.quit
        start_button.on_click = Func(start)

class PauseMenu(Entity):
    def __init__(self):
        super().__init__(parent = camera.ui, ignore_paused = True)

        self.pause_menu = Entity(parent = self, enabled = True)

        def reset():
            self.pause_menu.disable()
            player.position = (0, 5, 0)
            player.enable()
            mouse.locked = True

        def resume():
            player.enable()
            mouse.locked = True
            self.pause_menu.disable()

        resume_button = Button(text = "R e s u m e", color = color.black, scale_y = 0.1, scale_x = 0.3, y = -0.08, parent = self.pause_menu)
        reset_button = Button(text = "R e s e t", color = color.black, scale_y = 0.1, scale_x = 0.3, y = -0.2, parent = self.pause_menu)
        quit_button = Button(text = "Q u i t", color = color.black, scale_y = 0.1, scale_x = 0.3, y = -0.32, parent = self.pause_menu)
        quit_button.on_click = application.quit
        reset_button.on_click = Func(reset)
        resume_button.on_click = Func(resume)


m = MainMenu()
player.disable()
mouse.locked = False

sky = Sky(texture = "./assets/sky")

# Audio
jump = Audio(sound_file_name = "assets/jumping.mp3", autoplay = False)
jump.volume = 0.5
land = Audio(sound_file_name = "assets/land.mp3", autoplay = False)
land.volume = 0.1

# Lighting
light = PointLight(parent = camera, position = (0, 10, -1.5))
light.color = color.white

AmbientLight(color = color.rgba(100, 100, 100, 0.1))

def start():
    player.enable()

def speed():
    player.SPEED = normalSpeed

def input(key):
    # Escape button quits
    if key == "escape":
        mouse.locked = False
        player.disable()
        p = PauseMenu()

def update():
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

    # # Jump sound effect
    # if hit.hit:
    #     jump.play()

    # if not hit.hit:
    #     land.play()

    # Level01
    if ground_1.enabled == True:
        if hit.entity == block_1_7:
            player.jump_height = 0.7
        elif hit.entity != block_1_7:
            player.jump_height = normalJump

        if hit.entity == block_1_9:
            player.SPEED = boostSpeed * 1.2
            invoke(speed, delay=3)

        if hit.entity == finishBlock_1:
            destroyLevel01()
            player.position = Vec3(0, 5, 0)
            player.SPEED = normalSpeed
            player.jump_height = normalJump
    

    # Level02
    if ground_2.enabled == True:
        if block_2_3.enabled == True:
            if hit.entity == block_2_3:
                player.jump_height = 1.2
            elif hit.entity != block_2_3:
                player.jump_height = normalJump

        if block_2_6.enabled == True:
            if hit.entity == block_2_6:
                player.SPEED = boostSpeed * 1.5
                invoke(speed, delay=3)

        if finishBlock_2.enabled == True:
            if hit.entity == finishBlock_2:
                destroyLevel02()
                player.SPEED = normalSpeed
                player.jump_height = normalJump
                player.position = Vec3(0, 5, 0)


    # Level03
    if ground_3.enabled == True:
        if hit.entity == block_3_15:
            player.jump_height = 1.2
        if hit.entity == block_3_16:
            player.jump_height = 1.4

        if finishBlock_3.enabled == True:
            if hit.entity == finishBlock_3:
                destroyLevel03()
                player.SPEED = normalSpeed
                player.jump_height = normalJump
                player.position = Vec3(0, 5, 0)


    # Level04
    if ground_4.enabled == True:
        if hit.entity == block_4_3:
            player.jump_height = 2
        elif hit.entity != block_4_3:
            player.jump_height = normalJump
        if hit.entity == block_4_5:
            player.SPEED = boostSpeed * 2
        if hit.entity == block_4_6:
            player.jump_height = 1.3

        if finishBlock_4.enabled == True:
            if hit.entity == finishBlock_4:
                destroyLevel04()
                player.SPEED = normalSpeed
                player.jump_height = normalJump
                player.position = Vec3(0, 5, 0)


    # Level05
    if ground_5.enabled == True:
        if hit.entity == block_5_9:
            player.SPEED = boostSpeed * 2
        elif hit.entity == block_5_9:
            invoke(speed, delay = 1)

        if hit.entity == block_5_10:
            camera.rotation_z = 180
        if hit.entity == finishBlock_5:
            camera.rotation = (0, 0, 0)

        if finishBlock_5.enabled == True:
            if hit.entity == finishBlock_5:
                destroyLevel05()
                player.SPEED = normalSpeed
                player.jump_height = normalJump
                player.position = Vec3(0, 5, 0)


    # Level06
    if ground_6.enabled == True:
        if hit.entity == block_6_1:
            player.SPEED = boostSpeed * 1.5
        if hit.entity == block_6_2:
            player.SPEED = boostSpeed * 2
        if hit.entity == block_6_3:
            player.SPEED = boostSpeed * 2.5
        if hit.entity == block_6_4:
            player.SPEED = boostSpeed * 3.3
        if hit.entity == block_6_5:
            player.SPEED = boostSpeed * 4
        if hit.entity == block_6_6:
            player.SPEED = boostSpeed * 5
        if hit.entity == block_6_7:
            player.SPEED = boostSpeed * 5.3
        if hit.entity == block_6_8:
            player.SPEED = normalSpeed
        if hit.entity == finishBlock_6:
            destroyLevel06()
            player.position = (0, 5, 0)


    # Level07
    if ground_7.enabled == True:
        if hit.entity == block_7_12:
            camera.rotation_z = 180
        if hit.entity == finishBlock_7:
            camera.rotation = (0, 0, 0)
        if hit.entity == finishBlock_7:
            destroyLevel07()
            player.position = (0, 5, 0)

    
    # Level08
    if ground_8.enabled == True:
        if hit.entity == block_8_3:
            player.SPEED = 1
        if hit.entity == block_8_11:
            player.SPEED = boostSpeed * 5.5
            player.jump_height = 1.4

        if hit.entity == finishBlock_8:
            destroyLevel08()
            player.position = (0, 5, 0)


    # Level09
    if ground_9.enabled == True:
        if hit.entity == block_9_8:
            player.jump_height = 3
        elif hit.entity != block_9_8:
            player.jump_height = normalJump
        if hit.entity == block_9_11:
            player.SPEED = boostSpeed * 4
            player.jump_height = 2
        if hit.entity == finishBlock_9:
            destroyLevel09()
            player.position = (0, 5, 0)

    
    # Level10
    if ground_10.enabled == True:
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
            destroyLevel10()




# Level01

block_1_1 = NormalBlock(position = (0, 1, 12))
block_1_2 = NormalBlock(position = (0, 2, 20))
block_1_3 = NormalBlock(position = (0, 3, 28))
block_1_4 = NormalBlock(position = (0, 4, 36))
block_1_5 = NormalBlock(position = (8, 5, 36))
block_1_6 = NormalBlock(position = (16, 6, 36))
block_1_7 = JumpBlock(position = (24, 2, 36))
block_1_8 = NormalBlock(position = (32, 10, 36))
block_1_9 = SpeedBlock(position = (32, 10, 46))

ground_1 = StartBlock()
finishBlock_1 = EndBlock(position = (32, 10, 62))

# block_1_1.disable()
# block_1_2.disable()
# block_1_3.disable()
# block_1_4.disable()
# block_1_5.disable()
# block_1_6.disable()
# block_1_7.disable()
# block_1_8.disable()
# block_1_9.disable()

# ground_1.disable()
# finishBlock_1.disable()



#Level02

ground_2 = StartBlock()

block_2_1 = NormalBlock(position = (0, 1, 12))
block_2_2 = NormalBlock(position = (0, 2, 20))
block_2_3 = JumpBlock(position = (0, -20, 30))
block_2_4 = NormalBlock(position = (0, 10, 42))
block_2_5 = NormalBlock(position = (0, 10, 50))
block_2_6 = SpeedBlock(position = (0, 10, 62))
block_2_7 = NormalBlock(position = (0, 11, 74))

finishBlock_2 = EndBlock(position = (0, 11, 88))

ground_2.disable()
finishBlock_2.disable()
block_2_1.disable()
block_2_2.disable()
block_2_3.disable()
block_2_4.disable()
block_2_5.disable()
block_2_6.disable()
block_2_7.disable()




#Level03

ground_3 = StartBlock()

block_3_1 = NormalBlock(position = (0, 1, 10))
block_3_2 = NormalBlock(position = (0, 2, 18))
block_3_3 = NormalBlock(position = (8, 3, 18))
block_3_4 = NormalBlock(position = (16, 4, 18))
block_3_5 = NormalBlock(position = (16, 5, 10))
block_3_6 = NormalBlock(position = (16, 6, 2))
block_3_7 = NormalBlock(position = (8, 7, 2))
block_3_8 = NormalBlock(position = (8, 8, 10))
block_3_9 = NormalBlock(position = (8, 9, 18))
block_3_10 = NormalBlock(position = (16, 10, 18))
block_3_11 = NormalBlock(position = (16, 11, 10))
block_3_12 = NormalBlock(position = (16, 12, 2))
block_3_13 = NormalBlock(position = (8, 13, 2))
block_3_14 = NormalBlock(position = (8, 14, -6))
block_3_15 = JumpBlock(position = (8, 12, -15))
block_3_16 = JumpBlock(position = (8, 35, -25))

finishBlock_3 = EndBlock(position = (8, 80, -10))

block_3_1.disable()
block_3_2.disable()
block_3_3.disable()
block_3_4.disable()
block_3_5.disable()
block_3_6.disable()
block_3_7.disable()
block_3_8.disable()
block_3_9.disable()
block_3_10.disable()
block_3_11.disable()
block_3_12.disable()
block_3_13.disable()
block_3_14.disable()
block_3_15.disable()
block_3_16.disable()
ground_3.disable()
finishBlock_3.disable()




#Level04

ground_4 = StartBlock()

block_4_1 = NormalBlock(position = (0, 1, 12))
block_4_2 = NormalBlock(position = (0, 2, 20))
block_4_3 = JumpBlock(position = (0, -49, 40))
block_4_4 = NormalBlock(position = (0, 50, 60))
block_4_5 = SpeedBlock(position = (0, 50, 93), scale = (3, 0.5, 50))
block_4_6 = JumpBlock(position = (0, 15, 163))

finishBlock_4 = EndBlock(position = (0, 20, 240))

ground_4.disable()
finishBlock_4.disable()
block_4_1.disable()
block_4_2.disable()
block_4_3.disable()
block_4_4.disable()
block_4_5.disable()
block_4_6.disable()




#Level05

ground_5 = StartBlock()

block_5_1 = NormalBlock(position = (0, 1, 10))
block_5_2 = NormalBlock(position = (-3, 1, 18), rotation = (0, 0, 30))
block_5_3 = NormalBlock(position = (3, 1, 26), rotation = (0, 0, -30))
block_5_4 = NormalBlock(position = (-3, 1, 34), rotation = (0, 0, 30))
block_5_5 = NormalBlock(position = (3, 1, 42), rotation = (0, 0, -30))
block_5_6 = NormalBlock(position = (-3, 1, 50), rotation = (0, 0, 30))
block_5_7 = NormalBlock(position = (3, 1, 58), rotation = (0, 0, -30))
block_5_8 = NormalBlock(position = (-3, 1, 66), rotation = (0, 0, 30))

block_5_9 = SpeedBlock(position = (0, 1, 78))
block_5_10 = WeirdBlock(position = (0, 1, 95))

finishBlock_5 = EndBlock(position = (0, 1, 112))

block_5_1.disable()
block_5_2.disable()
block_5_3.disable()
block_5_4.disable()
block_5_5.disable()
block_5_6.disable()
block_5_7.disable()
block_5_8.disable()
block_5_9.disable()
block_5_10.disable()
ground_5.disable()
finishBlock_5.disable()




#Level06

ground_6 = StartBlock()
block_6_1 = SpeedBlock(position = (0, 0, 13))
block_6_2 = SpeedBlock(position = (0, 0, 32))
block_6_3 = SpeedBlock(position = (0, 0, 58))
block_6_4 = SpeedBlock(position = (0, 0, 90))
block_6_5 = SpeedBlock(position = (0, 0, 130))
block_6_6 = SpeedBlock(position = (0, 0, 180))
block_6_7 = SpeedBlock(position = (0, 0, 240))
block_6_8 = SlowBlock(position = (0, 0, 300))

finishBlock_6 = EndBlock(position = (0, 0, 315))


ground_6.disable()
finishBlock_6.disable()
block_6_1.disable()
block_6_2.disable()
block_6_3.disable()
block_6_4.disable()
block_6_5.disable()
block_6_6.disable()
block_6_7.disable()
block_6_8.disable()




# Level07

ground_7 = StartBlock()

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

finishBlock_7 = EndBlock(position = (0, 1, 95))

block_7_1.disable()
block_7_2.disable()
block_7_3.disable()
block_7_4.disable()
block_7_5.disable()
block_7_6.disable()
block_7_7.disable()
block_7_8.disable()
block_7_9.disable()
block_7_10.disable()
block_7_11.disable()
block_7_12.disable()
block_7_13.disable()
ground_7.disable()
finishBlock_7.disable()




# Level08

ground_8 = StartBlock()

block_8_1 = NormalBlock(position = (0, 0, 13))
block_8_2 = NormalBlock(position = (0, -20, 19))
block_8_3 = SlowBlock(position = (0, -20, 31))
block_8_4 = NormalBlock(position = (0, -20, 43))
block_8_5 = NormalBlock(position = (0, -20, 50))
block_8_6 = NormalBlock(position = (0, -20, 57))
block_8_7 = NormalBlock(position = (0, -20, 64))
block_8_8 = NormalBlock(position = (0, -22, 72))
block_8_9 = NormalBlock(position = (0, -24, 80))
block_8_10 = NormalBlock(position = (0, -26, 88))
block_8_11 = SpeedBlock(position = (0, -26, 98))

finishBlock_8 = EndBlock(position = (0, -10, 350))


block_8_1.disable()
block_8_2.disable()
block_8_3.disable()
block_8_4.disable()
block_8_5.disable()
block_8_6.disable()
block_8_7.disable()
block_8_8.disable()
block_8_9.disable()
block_8_10.disable()
block_8_11.disable()
ground_8.disable()
finishBlock_8.disable()




# Level09
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

ground_9.disable()
finishBlock_9.disable()
block_9_1.disable()
block_9_2.disable()
block_9_3.disable()
block_9_4.disable()
block_9_5.disable()
block_9_6.disable()
block_9_7.disable()
block_9_8.disable()
block_9_9.disable()
block_9_10.disable()
block_9_11.disable()




# Level 10
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


ground_10.disable()
finishBlock_10.disable()
block_10_1.disable()
block_10_2.disable()
block_10_3.disable()
block_10_4.disable()
block_10_5.disable()
block_10_6.disable()
block_10_7.disable()
block_10_8.disable()
block_10_9.disable()
block_10_10.disable()
block_10_11.disable()
block_10_12.disable()
block_10_13.disable()
block_10_14.disable()
block_10_15.disable()
block_10_16.disable()
block_10_17.disable()
block_10_18.disable()
block_10_19.disable()
block_10_20.disable()
block_10_21.disable()
block_10_22.disable()
block_10_23.disable()
block_10_24.disable()
block_10_25.disable()




def destroyLevel01():
    block_1_1.disable()
    block_1_2.disable()
    block_1_3.disable()
    block_1_4.disable()
    block_1_5.disable()
    block_1_6.disable()
    block_1_7.disable()
    block_1_8.disable()
    block_1_9.disable()
    ground_1.disable()
    finishBlock_1.disable()

    ground_2.enable()
    finishBlock_2.enable()
    block_2_1.enable()
    block_2_2.enable()
    block_2_3.enable()
    block_2_4.enable()
    block_2_5.enable()
    block_2_6.enable()
    block_2_7.enable()
    player.SPEED = normalSpeed
    player.jump_height = normalJump



def destroyLevel02():
    block_2_1.disable()
    block_2_2.disable()
    block_2_3.disable()
    block_2_4.disable()
    block_2_5.disable()
    block_2_6.disable()
    block_2_7.disable()

    ground_2.disable()
    finishBlock_2.disable()

    ground_3.enable()
    finishBlock_3.enable()
    block_3_1.enable()
    block_3_2.enable()
    block_3_3.enable()
    block_3_4.enable()
    block_3_5.enable()
    block_3_6.enable()
    block_3_7.enable()
    block_3_8.enable()
    block_3_9.enable()
    block_3_10.enable()
    block_3_11.enable()
    block_3_12.enable()
    block_3_13.enable()
    block_3_14.enable()
    block_3_15.enable()
    block_3_16.enable()
    player.SPEED = normalSpeed
    player.jump_height = normalJump



def destroyLevel03():
    block_3_1.disable()
    block_3_2.disable()
    block_3_3.disable()
    block_3_4.disable()
    block_3_5.disable()
    block_3_6.disable()
    block_3_7.disable()
    block_3_8.disable()
    block_3_9.disable()
    block_3_10.disable()
    block_3_11.disable()
    block_3_12.disable()
    block_3_13.disable()
    block_3_14.disable()
    block_3_15.disable()
    block_3_16.disable()
    ground_3.disable()
    finishBlock_3.disable()

    ground_4.enable()
    finishBlock_4.enable()
    block_4_1.enable()
    block_4_2.enable()
    block_4_3.enable()
    block_4_4.enable()
    block_4_5.enable()
    block_4_6.enable()
    player.SPEED = normalSpeed
    player.jump_height = normalJump



def destroyLevel04():
    block_4_1.disable()
    block_4_2.disable()
    block_4_3.disable()
    block_4_4.disable()
    block_4_5.disable()
    block_4_6.disable()
    ground_4.disable()
    finishBlock_4.disable()

    ground_5.enable()
    finishBlock_5.enable()
    block_5_1.enable()
    block_5_2.enable()
    block_5_3.enable()
    block_5_4.enable()
    block_5_5.enable()
    block_5_6.enable()
    block_5_7.enable()
    block_5_8.enable()
    block_5_9.enable()
    block_5_10.enable()
    player.SPEED = normalSpeed
    player.jump_height = normalJump



def destroyLevel05():
    block_5_1.disable()
    block_5_2.disable()
    block_5_3.disable()
    block_5_4.disable()
    block_5_5.disable()
    block_5_6.disable()
    block_5_7.disable()
    block_5_8.disable()
    block_5_9.disable()
    block_5_10.disable()
    ground_5.disable()
    finishBlock_5.disable()

    ground_6.enable()
    finishBlock_6.enable()
    block_6_1.enable()
    block_6_2.enable()
    block_6_3.enable()
    block_6_4.enable()
    block_6_5.enable()
    block_6_6.enable()
    block_6_7.enable()
    block_6_8.enable()
    player.SPEED = normalSpeed
    player.jump_height = normalJump



def destroyLevel06():
    ground_6.disable()
    finishBlock_6.disable()
    block_6_1.disable()
    block_6_2.disable()
    block_6_3.disable()
    block_6_4.disable()
    block_6_5.disable()
    block_6_6.disable()
    block_6_7.disable()
    block_6_8.disable()
    player.SPEED = normalSpeed
    player.jump_height = normalJump

    block_7_1.enable()
    block_7_2.enable()
    block_7_3.enable()
    block_7_4.enable()
    block_7_5.enable()
    block_7_6.enable()
    block_7_7.enable()
    block_7_8.enable()
    block_7_9.enable()
    block_7_10.enable()
    block_7_11.enable()
    block_7_12.enable()
    block_7_13.enable()
    ground_7.enable()
    finishBlock_7.enable()

def destroyLevel07():
    block_7_1.disable()
    block_7_2.disable()
    block_7_3.disable()
    block_7_4.disable()
    block_7_5.disable()
    block_7_6.disable()
    block_7_7.disable()
    block_7_8.disable()
    block_7_9.disable()
    block_7_10.disable()
    block_7_11.disable()
    block_7_12.disable()
    block_7_13.disable()
    ground_7.disable()
    finishBlock_7.disable()

    block_8_1.enable()
    block_8_2.enable()
    block_8_3.enable()
    block_8_4.enable()
    block_8_5.enable()
    block_8_6.enable()
    block_8_7.enable()
    block_8_8.enable()
    block_8_9.enable()
    block_8_10.enable()
    block_8_11.enable()
    ground_8.enable()
    finishBlock_8.enable()

    player.SPEED = normalSpeed
    player.jump_height = normalJump

def destroyLevel08():
    block_8_1.disable()
    block_8_2.disable()
    block_8_3.disable()
    block_8_4.disable()
    block_8_5.disable()
    block_8_6.disable()
    block_8_7.disable()
    block_8_8.disable()
    block_8_9.disable()
    block_8_10.disable()
    block_8_11.disable()
    ground_8.disable()
    finishBlock_8.disable()
    
    block_9_1.enable()
    block_9_2.enable()
    block_9_3.enable()
    block_9_4.enable()
    block_9_5.enable()
    block_9_6.enable()
    block_9_7.enable()
    block_9_8.enable()
    block_9_9.enable()
    block_9_10.enable()
    block_9_11.enable()
    ground_9.enable()
    finishBlock_9.enable()

    player.SPEED = normalSpeed
    player.jump_height = normalJump


def destroyLevel09():
    block_9_1.disable()
    block_9_2.disable()
    block_9_3.disable()
    block_9_4.disable()
    block_9_5.disable()
    block_9_6.disable()
    block_9_7.disable()
    block_9_8.disable()
    block_9_9.disable()
    block_9_10.disable()
    block_9_11.disable()
    ground_9.disable()
    finishBlock_9.disable()


    ground_10.enable()
    finishBlock_10.enable()
    block_10_1.enable()
    block_10_2.enable()
    block_10_3.enable()
    block_10_4.enable()
    block_10_5.enable()
    block_10_6.enable()
    block_10_7.enable()
    block_10_8.enable()
    block_10_9.enable()
    block_10_10.enable()
    block_10_11.enable()
    block_10_12.enable()
    block_10_13.enable()
    block_10_14.enable()
    block_10_15.enable()
    block_10_16.enable()
    block_10_17.enable()
    block_10_18.enable()
    block_10_19.enable()
    block_10_20.enable()
    block_10_21.enable()
    block_10_22.enable()
    block_10_23.enable()
    block_10_24.enable()
    block_10_25.enable()

    player.SPEED = normalSpeed
    player.jump_height = normalJump


def destroyLevel10():
    ground_10.disable()
    finishBlock_10.disable()
    block_10_1.disable()
    block_10_2.disable()
    block_10_3.disable()
    block_10_4.disable()
    block_10_5.disable()
    block_10_6.disable()
    block_10_7.disable()
    block_10_8.disable()
    block_10_9.disable()
    block_10_10.disable()
    block_10_11.disable()
    block_10_12.disable()
    block_10_13.disable()
    block_10_14.disable()
    block_10_15.disable()
    block_10_16.disable()
    block_10_17.disable()
    block_10_18.disable()
    block_10_19.disable()
    block_10_20.disable()
    block_10_21.disable()
    block_10_22.disable()
    block_10_23.disable()
    block_10_24.disable()
    block_10_25.disable()

    block_1_1.enable()
    block_1_2.enable()
    block_1_3.enable()
    block_1_4.enable()
    block_1_5.enable()
    block_1_6.enable()
    block_1_7.enable()
    block_1_8.enable()
    block_1_9.enable()

    ground_1.enable()
    finishBlock_1.enable()

    MainMenu()

    player.SPEED = normalSpeed
    player.jump_height = normalJump
    player.disable()
    mouse.locked = False
    player.position = (0, 10, 0)

    
app.run()

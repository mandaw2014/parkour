from ursina import *
from player import Player
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

#Level01
block_1 = NormalBlock(position = (0, 1, 9))
block_1_1 = NormalBlock(position = (0, 2, 14))
block_1_2 = NormalBlock(position = (0, 3, 19))
block_1_3 = NormalBlock(position = (0, 4, 24))
block_1_4 = NormalBlock(position = (5, 5, 24))
block_1_5 = NormalBlock(position = (10, 6, 24))
block_1_6 = JumpBlock(position = (17, 2, 24))
block_1_7 = NormalBlock(position = (25, 10, 24))
block_1_8 = SpeedBlock(position = (25, 10, 33))

ground_1 = StartBlock()
finishBlock_1 = EndBlock(position = (25, 10, 50))

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
    
    if ground_1.enabled == True:
        if hit.entity == block_1_6:
            player.jump_height = 0.7
        elif hit.entity != block_1_6:
            player.jump_height = normalJump

        if hit.entity == block_1_8:
            player.SPEED = boostSpeed * 1.2
            invoke(speed, delay=3)

        if hit.entity == finishBlock_1:
            destroyLevel01()
            player.position = Vec3(0, 5, 0)
            player.SPEED = normalSpeed
            player.jump_height = normalJump
    
    if ground_2.enabled == True:
        if block_2_2.enabled == True:
            if hit.entity == block_2_2:
                player.jump_height = 1.2
            elif hit.entity != block_2_2:
                player.jump_height = normalJump

        if block_2_5.enabled == True:
            if hit.entity == block_2_5:
                player.SPEED = boostSpeed * 1.5
                invoke(speed, delay=3)

        if finishBlock_2.enabled == True:
            if hit.entity == finishBlock_2:
                destroyLevel02()
                player.SPEED = normalSpeed
                player.jump_height = normalJump
                player.position = Vec3(0, 5, 0)


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


    if ground_6.enabled == True:
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
        if hit.entity == finishBlock_6:
            destroyLevel06()
            player.position = (0, 5, 0)

    if ground_7.enabled == True:
        if hit.entity == block_7_12:
            camera.rotation_z = 180
        if hit.entity == finishBlock_7:
            camera.rotation = (0, 0, 0)
        if hit.entity == finishBlock_7:
            destroyLevel07()
            player.position = (0, 5, 0)

    
    if ground_8.enabled == True:
        if hit.entity == block_8_3:
            player.SPEED = 1
        if hit.entity == block_8_11:
            player.SPEED = boostSpeed * 5.5
            player.jump_height = 1.4

        if hit.entity == finishBlock_8:
            destroyLevel08()
            player.position = (0, 5, 0)


    if ground_9.enabled == True:
        if hit.entity == block_9_8:
            player.jump_height = 3
        elif hit.entity != block_9_8:
            player.jump_height = normalJump
        if hit.entity == block_9_11:
            player.SPEED = boostSpeed * 4
            player.jump_height = 2




#Level02

ground_2 = StartBlock()
finishBlock_2 = EndBlock(position = (0, 11, 73))

block_2 = NormalBlock(position = (0, 1, 9))
block_2_1 = NormalBlock(position = (0, 2, 15))
block_2_2 = JumpBlock(position = (0, -20, 25))
block_2_3 = NormalBlock(position = (0, 10, 30))
block_2_4 = NormalBlock(position = (0, 10, 37))
block_2_5 = SpeedBlock(position = (0, 10, 45))
block_2_6 = NormalBlock(position = (0, 11, 60))

ground_2.disable()
finishBlock_2.disable()
block_2.disable()
block_2_1.disable()
block_2_2.disable()
block_2_3.disable()
block_2_4.disable()
block_2_5.disable()
block_2_6.disable()



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

def destroyLevel01():
    block_1.disable()
    block_1_1.disable()
    block_1_2.disable()
    block_1_3.disable()
    block_1_4.disable()
    block_1_5.disable()
    block_1_6.disable()
    block_1_7.disable()
    block_1_8.disable()
    ground_1.disable()
    finishBlock_1.disable()

    ground_2.enable()
    finishBlock_2.enable()
    block_2.enable()
    block_2_1.enable()
    block_2_2.enable()
    block_2_3.enable()
    block_2_4.enable()
    block_2_5.enable()
    block_2_6.enable()
    player.SPEED = normalSpeed
    player.jump_height = normalJump

def destroyLevel02():
    block_2.disable()
    block_2_1.disable()
    block_2_2.disable()
    block_2_3.disable()
    block_2_4.disable()
    block_2_5.disable()
    block_2_6.disable()
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

    
app.run()

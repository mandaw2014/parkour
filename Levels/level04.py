from ursina import *
import sys
sys.path.append('../Parkour/')
from block import *

normalSpeed = 2
boostSpeed  = 5
normalJump = 0.3

# Level04
class Level04(Entity):
    def __init__(self):
        super().__init__()

        self.is_enabled = False
        self.on = False

        self.level = Entity(model = "lava_level_4.obj", color = "#454545", collider = "mesh", scale = (10, 10, 10))
        self.lava = Entity(model = "plane", color = "#ff6700", collider = "mesh", scale = (1000, 1, 1000), position = (0, -30, 0))

        self.block_4_1 = NormalBlock((5, 2, -128))
        self.block_4_2 = NormalBlock((5, 2, -112))
        self.block_4_3 = NormalBlock((5, 2, -96))
        self.block_4_4 = NormalBlock((5, 2, -80))
        self.block_4_5 = NormalBlock((5, 2, -64))
        self.block_4_6 = SpeedBlock((5, 2, -46))

        self.block_4_7 = NormalBlock((5, 2, -10))
        self.block_4_8 = NormalBlock((5, 2, 8))
        self.block_4_9 = NormalBlock((5, 2, 24))
        self.block_4_10 = NormalBlock((5, 2, 40))
        self.block_4_11 = JumpBlock((5, -20, 64))

        self.block_4_12 = NormalBlock((5, 6, 96))
        self.block_4_13 = SpeedBlock((5, 6, 115))
        self.block_4_14 = SpeedBlock((5, 6, 145))

        self.block_4_15 = NormalBlock((5, -25, 201))
        self.block_4_16 = NormalBlock((5, -25, 217))
        self.block_4_17 = JumpBlock((-8, -25, 217))
        self.block_4_18 = NormalBlock((-36, 18, 217))

        self.block_4_19 = SpeedBlock((-55, 18, 217), (0, 90, 0))
        self.block_4_20 = SpeedBlock((-85, 18, 217), (0, 90, 0))
        self.block_4_21 = SpeedBlock((-120, 18, 217), (0, 90, 0))
        self.block_4_22 = SpeedBlock((-165, 18, 217), (0, 90, 0))
        self.block_4_23 = SpeedBlock((-215, 18, 217), (0, 90, 0))

        self.block_4_24 = NormalBlock((-275, 18, 217))

        self.block_4_25 = JumpBlock((-275, -20, 190))
        self.block_4_26 = JumpBlock((-275, -20, 140))
        self.block_4_27 = JumpBlock((-275, -20, 90))
        self.block_4_28 = JumpBlock((-275, -20, 40))
        self.block_4_29 = JumpBlock((-275, -20, -10))
        self.block_4_30 = JumpBlock((-275, -20, -60))

        self.block_4_31 = NormalBlock((-275, 25, -89))
        self.block_4_32 = NormalBlock((-275, 20, -109))
        self.block_4_33 = NormalBlock((-275, 15, -129))
    
        self.finishBlock_4 = EndBlock((-275, 3, -161))

        self.secret_1 = NormalBlock((-50, 35, -156))
        self.secret_2 = NormalBlock((-100, 35, -156))
        self.secret_3 = NormalBlock((-150, 35, -156))
        self.secret_4 = NormalBlock((-200, 35, -156))

        self.player = None

        self.disable()

    def disable(self):
        self.is_enabled = False
        self.on = False

        self.level.disable()
        self.lava.disable()

        self.block_4_1.disable()
        self.block_4_2.disable()
        self.block_4_3.disable()
        self.block_4_4.disable()
        self.block_4_5.disable()
        self.block_4_6.disable()
        self.block_4_7.disable()
        self.block_4_8.disable()
        self.block_4_9.disable()
        self.block_4_10.disable()
        self.block_4_11.disable()
        self.block_4_12.disable()
        self.block_4_13.disable()
        self.block_4_14.disable()
        self.block_4_15.disable()
        self.block_4_16.disable()
        self.block_4_17.disable()
        self.block_4_18.disable()
        self.block_4_19.disable()
        self.block_4_20.disable()
        self.block_4_21.disable()
        self.block_4_22.disable()
        self.block_4_23.disable()
        self.block_4_24.disable()
        self.block_4_25.disable()
        self.block_4_26.disable()
        self.block_4_27.disable()
        self.block_4_28.disable()
        self.block_4_29.disable()
        self.block_4_30.disable()
        self.block_4_31.disable()
        self.block_4_32.disable()
        self.block_4_33.disable()

        self.secret_1.disable()
        self.secret_2.disable()
        self.secret_3.disable()
        self.secret_4.disable()

        self.finishBlock_4.disable()

    def enable(self):
        self.is_enabled = True
        self.on = True

        self.level.enable()
        self.lava.enable()

        self.block_4_1.enable()
        self.block_4_2.enable()
        self.block_4_3.enable()
        self.block_4_4.enable()
        self.block_4_5.enable()
        self.block_4_6.enable()
        self.block_4_7.enable()
        self.block_4_8.enable()
        self.block_4_9.enable()
        self.block_4_10.enable()
        self.block_4_11.enable()
        self.block_4_12.enable()
        self.block_4_13.enable()
        self.block_4_14.enable()
        self.block_4_15.enable()
        self.block_4_16.enable()
        self.block_4_17.enable()
        self.block_4_18.enable()
        self.block_4_19.enable()
        self.block_4_20.enable()
        self.block_4_21.enable()
        self.block_4_22.enable()
        self.block_4_23.enable()
        self.block_4_24.enable()
        self.block_4_25.enable()
        self.block_4_26.enable()
        self.block_4_27.enable()
        self.block_4_28.enable()
        self.block_4_29.enable()
        self.block_4_30.enable()
        self.block_4_31.enable()
        self.block_4_32.enable()
        self.block_4_33.enable()

        self.secret_1.enable()
        self.secret_2.enable()
        self.secret_3.enable()
        self.secret_4.enable()

        self.finishBlock_4.enable()

    def speed(self):
        self.player.SPEED = normalSpeed

    def update(self):
        if self.is_enabled == True:
            self.light = DirectionalLight()
            self.is_enabled = False
        else:
            self.light = None

        # Stops the player from falling forever
        if self.on == True and self.player.position.y <= -50:
            self.player.SPEED = normalSpeed
            self.player.jump_height = normalJump
            self.player.position = (5, 10, -150)
            self.player.rotation = (0, 0, 0)
            self.player.count = 0.0

        # Restart the level
        if self.on == True and held_keys["g"]:
            self.player.SPEED = normalSpeed
            self.player.jump_height = normalJump
            self.player.position = (5, 10, -150)
            self.player.rotation = (0, 0, 0)
            self.player.count = 0.0

        # What entity the player hits
        hit = raycast(self.player.position, self.player.down, distance = 2, ignore = [self.player, ])

        if hit.entity == self.lava:
            self.player.SPEED = normalSpeed
            self.player.jump_height = normalJump
            self.player.position = (5, 10, -150)
            self.player.rotation = (0, 0, 0)
            self.player.count = 0.0

        if hit.entity == self.level:
            self.player.jump_height = normalJump

        if hit.entity == self.block_4_6:
            self.player.SPEED = 5
        elif hit.entity == self.block_4_7:
            self.player.SPEED = normalSpeed
            self.player.jump_height = normalJump

        if hit.entity == self.block_4_11:
            self.player.jump_height = 1.2
        elif hit.entity == self.block_4_12:
            self.player.jump_height = normalJump
        elif hit.entity == self.block_4_13:
            self.player.jump_height = normalJump

        if hit.entity == self.block_4_13:
            self.player.SPEED = 4
        if hit.entity == self.block_4_14:
            self.player.SPEED = 5
        elif hit.entity == self.block_4_15:
            self.player.SPEED = normalSpeed
            self.player.jump_height = normalJump
        elif hit.entity == self.block_4_16:
            self.player.SPEED = normalSpeed
            self.player.jump_height = normalJump

        if hit.entity == self.block_4_17:
            self.player.jump_height = 1.2
        elif hit.entity == self.block_4_18:
            self.player.jump_height = normalJump

        if hit.entity == self.block_4_19:
            self.player.SPEED = 4
        if hit.entity == self.block_4_20:
            self.player.SPEED = 5
        if hit.entity == self.block_4_21:
            self.player.SPEED = 6.5
        if hit.entity == self.block_4_22:
            self.player.SPEED = 7
        if hit.entity == self.block_4_23:
            self.player.SPEED = 9
        elif hit.entity == self.block_4_24:
            self.player.SPEED = normalSpeed
            self.player.jump_height = normalJump
        
        if hit.entity == self.block_4_25:
            self.player.SPEED = normalSpeed
            self.player.jump_height = 1.2
        if hit.entity == self.block_4_26:
            self.player.SPEED = normalSpeed
            self.player.jump_height = 1.2
        if hit.entity == self.block_4_27:
            self.player.jump_height = 1.2
        if hit.entity == self.block_4_28:
            self.player.jump_height = 1.2
        if hit.entity == self.block_4_29:
            self.player.jump_height = 1.2
        if hit.entity == self.block_4_30:
            self.player.jump_height = 1.2
        elif hit.entity == self.block_4_31:
            self.player.jump_height = normalJump
            self.player.SPEED = normalSpeed
        if hit.entity == self.finishBlock_4:
            destroy(self.light)

from ursina import *
import sys
sys.path.append('../Parkour/')
from block import *

normalSpeed = 2
boostSpeed  = 5
normalJump = 0.3

# Level06
class Level06(Entity):
    def __init__(self):
        super().__init__()

        self.is_enabled = False
        self.on = False

        self.level = Entity(model = "lava_level_6.obj", color = "#454545", collider = "mesh", scale = (30, 30, 30))
        self.lava = Entity(model = "plane", color = "#ff6700", collider = "mesh", scale = (1000, 1, 1000), position = (0, -150, 0))

        self.block_6_1 = NormalBlock((130, -130, 0))
        self.block_6_2 = NormalBlock((116, -128, 0))
        self.block_6_3 = NormalBlock((102, -126, 0))
        self.block_6_4 = NormalBlock((88, -124, 0))
        self.block_6_5 = NormalBlock((74, -122, 0))
        self.block_6_6 = NormalBlock((60, -120, 0))
        self.block_6_7 = NormalBlock((46, -118, 0))
        
        self.block_6_8 = NormalBlock((46, -116, 14))
        self.block_6_9 = NormalBlock((46, -114, 28))
        self.block_6_10 = NormalBlock((32, -112, 28))
        self.block_6_11 = NormalBlock((32, -110, 42))
        self.block_6_12 = NormalBlock((18, -108, 42))
        self.block_6_13 = NormalBlock((4, -106, 42))

        self.block_6_14 = JumpBlock((-11, -106, 42))
        self.block_6_15 = NormalBlock((-20, -75, 42))
        self.block_6_16 = NormalBlock((-34, -73, 42))

        self.block_6_17 = SpeedBlock((-48, -73, 42), (0, -90, 0))
        self.block_6_18 = SpeedBlock((-78, -71, 42), (0, -90, 0))
        self.block_6_19 = SpeedBlock((-110, -69, 42), (0, -90, 0))
        
        self.block_6_20 = NormalBlock((-150, -69, 42))
        self.block_6_21 = NormalBlock((-150, -67, 28))
        self.block_6_22 = NormalBlock((-150, -65, 14))
        self.block_6_23 = NormalBlock((-150, -63, 0))

        self.block_6_24 = SpeedBlock((-132, -63, 0), (0, -90, 0))
        self.block_6_25 = SpeedBlock((-102, -61, 0), (0, -90, 0))
        self.block_6_26 = SpeedBlock((-67, -59, 0), (0, -90, 0))

        self.block_6_27 = JumpBlock((-33, -57, 0))
        self.block_6_28 = JumpBlock((-40, -26, 0))
        self.block_6_29 = JumpBlock((-33, 4, 0))

        self.block_6_30 = NormalBlock((-40, 34, 0))
        self.block_6_31 = JumpBlock((-50, 36, 0))

        self.finishBlock_6 = EndBlock((-4, 168.5, 0))

        self.player = None

        self.disable()

    def disable(self):
        self.is_enabled = False
        self.on = False

        self.level.disable()
        self.lava.disable()

        self.block_6_1.disable()
        self.block_6_2.disable()
        self.block_6_3.disable()
        self.block_6_4.disable()
        self.block_6_5.disable()
        self.block_6_6.disable()
        self.block_6_7.disable()
        self.block_6_8.disable()
        self.block_6_9.disable()
        self.block_6_10.disable()
        self.block_6_11.disable()
        self.block_6_12.disable()
        self.block_6_13.disable()
        self.block_6_14.disable()
        self.block_6_15.disable()
        self.block_6_16.disable()
        self.block_6_17.disable()
        self.block_6_18.disable()
        self.block_6_19.disable()
        self.block_6_20.disable()
        self.block_6_21.disable()
        self.block_6_22.disable()
        self.block_6_23.disable()
        self.block_6_24.disable()
        self.block_6_25.disable()
        self.block_6_26.disable()
        self.block_6_27.disable()
        self.block_6_28.disable()
        self.block_6_29.disable()
        self.block_6_30.disable()
        self.block_6_31.disable()

        self.finishBlock_6.disable()

    def enable(self):
        self.is_enabled = True
        self.on = True

        self.level.enable()
        self.lava.enable()

        self.block_6_1.enable()
        self.block_6_2.enable()
        self.block_6_3.enable()
        self.block_6_4.enable()
        self.block_6_5.enable()
        self.block_6_6.enable()
        self.block_6_7.enable()
        self.block_6_8.enable()
        self.block_6_9.enable()
        self.block_6_10.enable()
        self.block_6_11.enable()
        self.block_6_12.enable()
        self.block_6_13.enable()
        self.block_6_14.enable()
        self.block_6_15.enable()
        self.block_6_16.enable()
        self.block_6_17.enable()
        self.block_6_18.enable()
        self.block_6_19.enable()
        self.block_6_20.enable()
        self.block_6_21.enable()
        self.block_6_22.enable()
        self.block_6_23.enable()
        self.block_6_24.enable()
        self.block_6_25.enable()
        self.block_6_26.enable()
        self.block_6_27.enable()
        self.block_6_28.enable()
        self.block_6_29.enable()
        self.block_6_30.enable()
        self.block_6_31.enable()

        self.finishBlock_6.enable()

    def update(self):
        # Stops the player from falling forever
        if self.is_enabled == True and self.player.position.y <= -300:
            self.player.SPEED = normalSpeed
            self.player.jump_height = normalJump
            self.player.position = (130, -120, 0)
            self.player.rotation = (0, -90, 0)
            self.player.count = 0.0

        # Restart the level
        if self.is_enabled == True and held_keys["g"]:
            self.player.SPEED = normalSpeed
            self.player.jump_height = normalJump
            self.player.position = (130, -120, 0)
            self.player.rotation = (0, -90, 0)
            self.player.count = 0.0

        # What entity the player hits
        hit = raycast(self.player.position, self.player.down, distance = 2, ignore = [self.player, ])

        if hit.entity == self.lava:
            self.player.SPEED = normalSpeed
            self.player.jump_height = normalJump
            self.player.position = (130, -120, 0)
            self.player.rotation = (0, -90, 0)
            self.player.count = 0.0

        if hit.entity == self.block_6_14:
            self.player.jump_height = 1
        elif hit.entity == self.block_6_15:
            self.player.jump_height = normalJump
        elif hit.entity == self.block_6_16:
            self.player.jump_height = normalJump

        if hit.entity == self.block_6_17:
            self.player.SPEED = 4
        if hit.entity == self.block_6_18:
            self.player.SPEED = 5
        if hit.entity == self.block_6_19:
            self.player.SPEED = 6
        elif hit.entity == self.block_6_20:
            self.player.SPEED = normalSpeed
        elif hit.entity == self.block_6_21:
            self.player.SPEED = normalSpeed
        elif hit.entity == self.block_6_22:
            self.player.SPEED = normalSpeed
        elif hit.entity == self.block_6_23:
            self.player.SPEED = normalSpeed
        
        if hit.entity == self.block_6_24:
            self.player.SPEED = 4
        if hit.entity == self.block_6_25:
            self.player.SPEED = 5
        if hit.entity == self.block_6_26:
            self.player.SPEED = 6
        elif hit.entity == self.block_6_27:
            self.player.SPEED = normalSpeed
        if hit.entity == self.block_6_27:
            self.player.jump_height = 1
        if hit.entity == self.block_6_28:
            self.player.jump_height = 1
        if hit.entity == self.block_6_29:
            self.player.jump_height = 1
        elif hit.entity == self.block_6_30:
            self.player.jump_height = normalJump

        if hit.entity == self.block_6_31:
            self.player.jump_height = 2.3
from ursina import *
import sys
sys.path.append('../Parkour/')
from block import *

normalSpeed = 2
boostSpeed  = 5
normalJump = 0.3

# Level03
class Level03(Entity):
    def __init__(self):
        super().__init__()

        self.is_enabled = False

        self.mountain = Entity(model = "mountain_level_3.obj", texture = "mountain_level_3.png", collider = "mesh", scale = (70, 70, 70), position = (800, 0, 0))

        self.block_3_1 = NormalBlock((809, 4, 97))
        self.block_3_2 = NormalBlock((809, 6, 85))
        self.block_3_3 = NormalBlock((809, 8, 72))
        self.block_3_4 = NormalBlock((822, 10, 72))
        self.block_3_5 = NormalBlock((835, 12, 72))
        self.block_3_6 = NormalBlock((848, 14, 72))
        self.block_3_7 = NormalBlock((861, 16, 72))
        self.block_3_8 = NormalBlock((874, 18, 72))
        self.block_3_9 = NormalBlock((874, 20, 59))
        self.block_3_10 = NormalBlock((874, 22, 46))
        self.block_3_11 = NormalBlock((874, 24, 33))
        self.block_3_12 = NormalBlock((874, 26, 20))
        self.block_3_13 = NormalBlock((874, 28, 7))
        self.block_3_14 = NormalBlock((874, 30, -6))
        self.block_3_15 = NormalBlock((874, 32, -19))
        self.block_3_16 = NormalBlock((874, 34, -32))
        self.block_3_17 = NormalBlock((874, 36, -45))
        self.block_3_18 = NormalBlock((874, 38, -58))
        self.block_3_19 = JumpBlock((861, 40, -58))

        self.block_3_20 = NormalBlock((839, 96, -58))
        self.block_3_21 = NormalBlock((839, 98, -45))
        self.block_3_22 = NormalBlock((839, 100, -32))
        self.block_3_23 = NormalBlock((839, 102, -19))
        self.block_3_24 = NormalBlock((839, 104, -6))
        self.block_3_25 = NormalBlock((839, 106, 7))
        self.block_3_26 = NormalBlock((839, 108, 20))
        self.block_3_27 = NormalBlock((826, 110, 20))
        self.block_3_28 = JumpBlock((813, 112, 20))

        self.block_3_29 = NormalBlock((800, 155, -10))

        self.block_3_30 = SpeedBlock((784, 155, -10), (0, 270, 0))
        self.block_3_31 = SpeedBlock((755, 155, -10), (0, 270, 0))
        self.block_3_32 = SpeedBlock((720, 155, -10), (0, 270, 0))
        self.block_3_33 = SpeedBlock((680, 155, -10), (0, 270, 0))
        self.block_3_34 = SpeedBlock((630, 155, -10), (0, 270, 0))
        self.block_3_35 = SpeedBlock((570, 155, -10), (0, 270, 0))

        self.finishBlock_3 = EndBlock((507, 146, -9.5))

        self.player = None

        self.disable()

    def disable(self):
        self.is_enabled = False

        self.mountain.disable()
    
        self.block_3_1.disable()
        self.block_3_2.disable()
        self.block_3_3.disable()
        self.block_3_4.disable()
        self.block_3_5.disable()
        self.block_3_6.disable()
        self.block_3_7.disable()
        self.block_3_8.disable()
        self.block_3_9.disable()
        self.block_3_10.disable()
        self.block_3_11.disable()
        self.block_3_12.disable()
        self.block_3_13.disable()
        self.block_3_14.disable()
        self.block_3_15.disable()
        self.block_3_16.disable()
        self.block_3_17.disable()
        self.block_3_18.disable()
        self.block_3_19.disable()
        self.block_3_20.disable()
        self.block_3_21.disable()
        self.block_3_22.disable()
        self.block_3_23.disable()
        self.block_3_24.disable()
        self.block_3_25.disable()
        self.block_3_26.disable()
        self.block_3_27.disable()
        self.block_3_28.disable()
        self.block_3_29.disable()
        self.block_3_30.disable()
        self.block_3_31.disable()
        self.block_3_32.disable()
        self.block_3_33.disable()
        self.block_3_34.disable()
        self.block_3_35.disable()

        self.finishBlock_3.disable()

    def enable(self):
        self.is_enabled = True

        self.mountain.enable()

        self.block_3_1.enable()
        self.block_3_2.enable()
        self.block_3_3.enable()
        self.block_3_4.enable()
        self.block_3_5.enable()
        self.block_3_6.enable()
        self.block_3_7.enable()
        self.block_3_8.enable()
        self.block_3_9.enable()
        self.block_3_10.enable()
        self.block_3_11.enable()
        self.block_3_12.enable()
        self.block_3_13.enable()
        self.block_3_14.enable()
        self.block_3_15.enable()
        self.block_3_16.enable()
        self.block_3_17.enable()
        self.block_3_18.enable()
        self.block_3_19.enable()
        self.block_3_20.enable()
        self.block_3_21.enable()
        self.block_3_22.enable()
        self.block_3_23.enable()
        self.block_3_24.enable()
        self.block_3_25.enable()
        self.block_3_26.enable()
        self.block_3_27.enable()
        self.block_3_28.enable()
        self.block_3_29.enable()
        self.block_3_30.enable()
        self.block_3_31.enable()
        self.block_3_32.enable()
        self.block_3_33.enable()
        self.block_3_34.enable()
        self.block_3_35.enable()

        self.finishBlock_3.enable()

    def speed(self):
        self.player.SPEED = normalSpeed

    def update(self):
        # Stops the player from falling forever
        if self.is_enabled == True and self.player.position.y <= -50:
            self.player.SPEED = normalSpeed
            self.player.jump_height = normalJump
            self.player.position = (809, 4, 106)
            self.player.rotation = (0, 181, 0)
            self.player.count = 0.0

        # Restart the level
        if self.is_enabled == True and held_keys["g"]:
            self.player.SPEED = normalSpeed
            self.player.jump_height = normalJump
            self.player.position = (809, 4, 106)
            self.player.rotation = (0, 181, 0)
            self.player.count = 0.0

        # What entity the player hits
        hit = raycast(self.player.position, self.player.down, distance = 2, ignore = [self.player, ])

        if hit.entity == self.mountain:
            self.player.jump_height = 0.3
            self.player.SPEED = 2
        
        if hit.entity == self.block_3_19:
            self.player.jump_height = 1.5
        elif hit.entity == self.block_3_20:
            self.player.jump_height = normalJump
        elif hit.entity == self.block_3_21:
            self.player.jump_height = normalJump
        elif hit.entity == self.block_3_22:
            self.player.jump_height = normalJump
        if hit.entity == self.block_3_28:
            self.player.jump_height = 1.3
        elif hit.entity == self.block_3_29 or hit.entity == self.block_3_30:
            self.player.jump_height = normalJump
        if hit.entity == self.block_3_30:
            self.player.SPEED = 4
        if hit.entity == self.block_3_31:
            self.player.SPEED = 5
        if hit.entity == self.block_3_32:
            self.player.SPEED = 6
        if hit.entity == self.block_3_33:
            self.player.SPEED = 8
        if hit.entity == self.block_3_34:
            self.player.SPEED = 9
        if hit.entity == self.block_3_35:
            self.player.SPEED = 12

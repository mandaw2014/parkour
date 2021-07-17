from ursina import *
import sys
sys.path.append('../Parkour/')
from block import *

normalSpeed = 2
boostSpeed  = 5
normalJump = 0.3

# Level07
class Level07(Entity):
    def __init__(self):
        super().__init__()

        self.is_enabled = False

        self.block_7_1 = SkyNormalBlock((0, 0, 0))
        self.block_7_2 = SkyNormalBlock((0, 1, 18))
        self.block_7_3 = SkyNormalBlock((0, 2, 36))
        self.block_7_4 = SkyJumpBlock((0, 3, 54))

        self.block_7_5 = SkyNormalBlock((0, 50, 36))
        self.block_7_6 = SkyNormalBlock((0, 51, 18))

        self.block_7_7 = SkySpeedBlock((0, 51, -5), (0, 90, 0))
        self.block_7_8 = SkySpeedBlock((0, 51, -40), (0, 90, 0))
        self.block_7_9 = SkySpeedBlock((0, 51, -85), (0, 90, 0))

        self.block_7_10 = SkyJumpBlock((0, 40, -145))

        self.block_7_11 = SkyNormalBlock((0, 87, -163))
        self.block_7_12 = SkyNormalBlock((0, 88, -183))
        self.block_7_13 = SkyNormalBlock((0, 89, -203))
        self.block_7_14 = SkyNormalBlock((0, 90, -223))
        self.block_7_15 = SkyNormalBlock((0, 91, -243))
        self.block_7_16 = SkyNormalBlock((0, 92, -263))
        self.block_7_17 = SkyNormalBlock((0, 93, -283))

        self.block_7_18 = SkyNormalBlock((0, 94, -308), scale = (3, 3, 3))
        self.finishBlock_7 = EndBlock((0, 96, -308))

        self.disable()

        self.player = None

    def disable(self):
        self.is_enabled = False

        self.block_7_1.disable()
        self.block_7_2.disable()
        self.block_7_3.disable()
        self.block_7_4.disable()
        self.block_7_5.disable()
        self.block_7_6.disable()
        self.block_7_7.disable()
        self.block_7_8.disable()
        self.block_7_9.disable()
        self.block_7_10.disable()
        self.block_7_11.disable()
        self.block_7_12.disable()
        self.block_7_13.disable()
        self.block_7_14.disable()
        self.block_7_15.disable()
        self.block_7_16.disable()
        self.block_7_17.disable()
        self.block_7_18.disable()

        self.finishBlock_7.disable()

    def enable(self):
        self.is_enabled = True

        self.block_7_1.enable()
        self.block_7_2.enable()
        self.block_7_3.enable()
        self.block_7_4.enable()
        self.block_7_5.enable()
        self.block_7_6.enable()
        self.block_7_7.enable()
        self.block_7_8.enable()
        self.block_7_9.enable()
        self.block_7_10.enable()
        self.block_7_11.enable()
        self.block_7_12.enable()
        self.block_7_13.enable()
        self.block_7_14.enable()
        self.block_7_15.enable()
        self.block_7_16.enable()
        self.block_7_17.enable()
        self.block_7_18.enable()

        self.finishBlock_7.enable()

    def update(self):
        # Stops the player from falling forever
        if self.is_enabled == True and self.player.position.y <= -50:
            self.player.SPEED = normalSpeed
            self.player.jump_height = normalJump
            self.player.position = (0, 10, 0)
            self.player.rotation = (0, 0, 0)
            self.player.count = 0.0

        # Restart the level
        if self.is_enabled == True and held_keys["g"]:
            self.player.SPEED = normalSpeed
            self.player.jump_height = normalJump
            self.player.position = (0, 10, 0)
            self.player.rotation = (0, 0, 0)
            self.player.count = 0.0

        # What entity the player hits
        hit = raycast(self.player.position, self.player.down, distance = 2, ignore = [self.player, ])

        if hit.entity == self.block_7_4:
            self.player.jump_height = 1.3
        elif hit.entity == self.block_7_5:
            self.player.jump_height = normalJump

        if hit.entity == self.block_7_7:
            self.player.SPEED = 4
        if hit.entity == self.block_7_8:
            self.player.SPEED = 5
        if hit.entity == self.block_7_9:
            self.player.SPEED = 6
        elif hit.entity == self.block_7_10:
            self.player.SPEED = normalSpeed
            self.player.jump_height = 1.3
        elif hit.entity == self.block_7_11:
            self.player.jump_height = normalJump
        elif hit.entity == self.block_7_12:
            self.player.jump_height = normalJump  
        elif hit.entity == self.block_7_13:
            self.player.jump_height = normalJump
        elif hit.entity == self.block_7_14:
            self.player.jump_height = normalJump
        elif hit.entity == self.block_7_15:
            self.player.jump_height = normalJump
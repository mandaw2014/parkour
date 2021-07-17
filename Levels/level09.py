from ursina import *
import sys
sys.path.append('../Parkour/')
from block import *

normalSpeed = 2
boostSpeed  = 5
normalJump = 0.3

# Level09
class Level09(Entity):
    def __init__(self):
        super().__init__()

        self.is_enabled = False

        self.block_9_1 = SkyNormalBlock()
        self.block_9_2 = SkyNormalBlock((0, 1, 20))
        self.block_9_3 = SkyNormalBlock((0, 2, 40))

        self.block_9_4 = SkySpeedBlock((0, 2, 65), (0, 90, 0))
        self.block_9_5 = SkySpeedBlock((0, 2, 110), (0, 90, 0))
        self.block_9_6 = SkySpeedBlock((0, 2, 160), (0, 90, 0))
        self.block_9_7 = SkySpeedBlock((0, 2, 220), (0, 90, 0))
        self.block_9_8 = SkySpeedBlock((0, 2, 300), (0, 90, 0))
        self.block_9_9 = SkySpeedBlock((0, 2, 380), (0, 90, 0))
        self.block_9_10 = SkySpeedBlock((0, 2, 460), (0, 90, 0))
        self.block_9_11 = SkySpeedBlock((0, 2, 540), (0, 90, 0))
        self.block_9_12 = SkySpeedBlock((0, 2, 620), (0, 90, 0))
        self.block_9_13 = SkySpeedBlock((0, 2, 700), (0, 90, 0))
        self.block_9_14 = SkySpeedBlock((0, 2, 780), (0, 90, 0))
        self.block_9_15 = SkySpeedBlock((0, 2, 860), (0, 90, 0))
        self.block_9_16 = SkySpeedBlock((0, 2, 940), (0, 90, 0))
        self.block_9_17 = SkySpeedBlock((0, 2, 1020), (0, 90, 0))
        self.block_9_18 = SkySpeedBlock((0, 2, 1100), (0, 90, 0))
        self.block_9_19 = SkySpeedBlock((0, 2, 1180), (0, 90, 0))
        self.block_9_20 = SkySpeedBlock((0, 2, 1260), (0, 90, 0))

        self.block_9_21 = SkyNormalBlock((0, -4, 1452), scale = (2, 2, 2))
        self.finishBlock_9 = EndBlock((0, -2, 1452))

        self.player = None

        self.disable()

    def disable(self):
        self.is_enabled = False

        self.block_9_1.disable()
        self.block_9_2.disable()
        self.block_9_3.disable()
        self.block_9_4.disable()
        self.block_9_5.disable()
        self.block_9_6.disable()
        self.block_9_7.disable()
        self.block_9_8.disable()
        self.block_9_9.disable()
        self.block_9_10.disable()
        self.block_9_11.disable()
        self.block_9_12.disable()
        self.block_9_13.disable()
        self.block_9_14.disable()
        self.block_9_15.disable()
        self.block_9_16.disable()
        self.block_9_17.disable()
        self.block_9_18.disable()
        self.block_9_19.disable()
        self.block_9_20.disable()
        self.block_9_21.disable()

        self.finishBlock_9.disable()

    def enable(self):
        self.is_enabled = True

        self.block_9_1.enable()
        self.block_9_2.enable()
        self.block_9_3.enable()
        self.block_9_4.enable()
        self.block_9_5.enable()
        self.block_9_6.enable()
        self.block_9_7.enable()
        self.block_9_8.enable()
        self.block_9_9.enable()
        self.block_9_10.enable()
        self.block_9_11.enable()
        self.block_9_12.enable()
        self.block_9_13.enable()
        self.block_9_14.enable()
        self.block_9_15.enable()
        self.block_9_16.enable()
        self.block_9_17.enable()
        self.block_9_18.enable()
        self.block_9_19.enable()
        self.block_9_20.enable()
        self.block_9_21.enable()

        self.finishBlock_9.enable()

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

        if hit.entity == self.block_9_4:
            self.player.SPEED = 5
        if hit.entity == self.block_9_5:
            self.player.SPEED = 7
        if hit.entity == self.block_9_6:
            self.player.SPEED = 9
        if hit.entity == self.block_9_7:
            self.player.SPEED = 10.5
        if hit.entity == self.block_9_20:
            self.player.SPEED = 50
        elif hit.entity == self.block_9_21:
            self.player.SPEED = normalSpeed
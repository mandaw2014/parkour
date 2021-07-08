from ursina import *
import sys
sys.path.append('../Parkour/')
from block import *

normalSpeed = 2
boostSpeed  = 3
normalJump = 0.3

# Level10
class Level10(Entity):
    def __init__(self):
        super().__init__()

        self.block_10_1 = NormalBlock(position = (0, 1, 13))
        self.block_10_2 = SpeedBlock(position = (0, 1, 25))
        self.block_10_3 = JumpBlock(position = (0, -10, 70))
        self.block_10_4 = FakeBlock(position = (0, 10, 150))
        self.block_10_5 = NormalBlock(position = (0, 10, 160))
        self.block_10_6 = Wall(position = (0, 11, 165))
        self.block_10_7 = NormalBlock(position = (0, 10, 170))
        self.block_10_8 = Wall(position = (0, 11, 175))
        self.block_10_9 = NormalBlock(position = (0, 10, 180))
        self.block_10_10 = NormalBlock(position = (0, 10, 190))
        self.block_10_11 = NormalBlock(position = (-5, 11, 190))
        self.block_10_12 = NormalBlock(position = (-10, 12, 190))
        self.block_10_13 = NormalBlock(position = (-10, 13, 185))
        self.block_10_14 = NormalBlock(position = (-10, 14, 180))
        self.block_10_15 = NormalBlock(position = (-10, 15, 175))
        self.block_10_16 = NormalBlock(position = (-5, 16, 175))
        self.block_10_17 = NormalBlock(position = (0, 17, 175))
        self.block_10_18 = NormalBlock(position = (0, 18, 185))
        self.block_10_19 = NormalBlock(position = (0, 19, 195))
        self.block_10_20 = NormalBlock(position = (0, 20, 205))
        self.block_10_21 = WeirdBlock(position = (0, 20, 220))
        self.block_10_22 = NormalBlock(position = (0, 20, 233))
        self.block_10_23 = NormalBlock(position = (0, 20, 243))
        self.block_10_24 = NormalBlock(position = (0, 20, 253))
        self.block_10_25 = NormalBlock(position = (0, 20, 263))

        self.ground_10 = StartBlock()
        self.finishBlock_10 = EndBlock(position = (0, 20, 275))

        self.player = None

        self.disable()

    def speed(self):
        self.player.SPEED = normalSpeed

    def disable(self):
       self.block_10_1.disable()
       self.block_10_2.disable()
       self.block_10_3.disable()
       self.block_10_4.disable()
       self.block_10_5.disable()
       self.block_10_6.disable()
       self.block_10_7.disable()
       self.block_10_8.disable()
       self.block_10_9.disable()
       self.block_10_10.disable()
       self.block_10_11.disable()
       self.block_10_12.disable()
       self.block_10_13.disable()
       self.block_10_14.disable()
       self.block_10_15.disable()
       self.block_10_16.disable()
       self.block_10_17.disable()
       self.block_10_18.disable()
       self.block_10_19.disable()
       self.block_10_20.disable()
       self.block_10_21.disable()
       self.block_10_22.disable()
       self.block_10_23.disable()
       self.block_10_24.disable()
       self.block_10_25.disable()
       self.finishBlock_10.disable()
       self.ground_10.disable()

    def enable(self):
       self.block_10_1.enable()
       self.block_10_2.enable()
       self.block_10_3.enable()
       self.block_10_4.enable()
       self.block_10_5.enable()
       self.block_10_6.enable()
       self.block_10_7.enable()
       self.block_10_8.enable()
       self.block_10_9.enable()
       self.block_10_10.enable()
       self.block_10_11.enable()
       self.block_10_12.enable()
       self.block_10_13.enable()
       self.block_10_14.enable()
       self.block_10_15.enable()
       self.block_10_16.enable()
       self.block_10_17.enable()
       self.block_10_18.enable()
       self.block_10_19.enable()
       self.block_10_20.enable()
       self.block_10_21.enable()
       self.block_10_22.enable()
       self.block_10_23.enable()
       self.block_10_24.enable()
       self.block_10_25.enable()
       self.finishBlock_10.enable()
       self.ground_10.enable()

    def update(self):
        # What entity the player hits
        hit = raycast(self.player.position, self.player.down, distance = 2, ignore = [self.player, ])
        
        if self.ground_10.enabled == True:
            if hit.entity == self.block_10_2:
                self.player.SPEED = boostSpeed * 2.3
            if hit.entity == self.block_10_3:
                self.player.jump_height = 1.3
            elif hit.entity != self.block_10_3:
                self.player.jump_height = normalJump
            if hit.entity == self.block_10_5 or hit.entity == self.block_10_7 or hit.entity == self.block_10_9 or hit.entity == self.block_10_10 or hit.entity == self.block_10_11 or hit.entity == self.block_10_12 or hit.entity == self.block_10_13 or hit.entity == self.block_10_14 or hit.entity == self.block_10_15 or hit.entity == self.block_10_16 or hit.entity == self.block_10_17 or hit.entity == self.block_10_18 or hit.entity == self.block_10_19 or hit.entity == self.block_10_20:
                self.player.SPEED = normalSpeed
                self.player.jump_height = normalJump
            if hit.entity == self.block_10_21:
                camera.rotation_z = 180

            if hit.entity == self.finishBlock_10:
                camera.rotation_z = 0
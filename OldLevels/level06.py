from ursina import *
import sys
sys.path.append('../Parkour/')
from block import *

normalSpeed = 2
boostSpeed  = 3
normalJump = 0.3

# Level06
class Level06(Entity):
    def __init__(self):
        super().__init__()

        self.block_6_1 = SpeedBlock(position = (0, 0, 13))
        self.block_6_2 = SpeedBlock(position = (0, 0, 32))
        self.block_6_3 = SpeedBlock(position = (0, 0, 58))
        self.block_6_4 = SpeedBlock(position = (0, 0, 90))
        self.block_6_5 = SpeedBlock(position = (0, 0, 130))
        self.block_6_6 = SpeedBlock(position = (0, 0, 180))
        self.block_6_7 = SpeedBlock(position = (0, 0, 240))
        self.block_6_8 = SlowBlock(position = (0, 0, 300))

        self.ground_6 = StartBlock()
        self.finishBlock_6 = EndBlock(position = (0, 0, 315))

        self.player = None

        self.disable()

    def speed(self):
        self.player.SPEED = normalSpeed

    def disable(self):
       self.block_6_1.disable()
       self.block_6_2.disable()
       self.block_6_3.disable()
       self.block_6_4.disable()
       self.block_6_5.disable()
       self.block_6_6.disable()
       self.block_6_7.disable()
       self.block_6_8.disable()
       self.finishBlock_6.disable()
       self.ground_6.disable()

    def enable(self):
       self.block_6_1.enable()
       self.block_6_2.enable()
       self.block_6_3.enable()
       self.block_6_4.enable()
       self.block_6_5.enable()
       self.block_6_6.enable()
       self.block_6_7.enable()
       self.block_6_8.enable()
       self.finishBlock_6.enable()
       self.ground_6.enable()

    def update(self):
        # What entity the player hits
        hit = raycast(self.player.position, self.player.down, distance = 2, ignore = [self.player, ])
        
        if self.ground_6.enabled == True:
            if hit.entity == self.block_6_1:
                self.player.SPEED = boostSpeed * 1.5
            if hit.entity == self.block_6_2:
                self.player.SPEED = boostSpeed * 2
            if hit.entity == self.block_6_3:
                self.player.SPEED = boostSpeed * 2.5
            if hit.entity == self.block_6_4:
                self.player.SPEED = boostSpeed * 3.3
            if hit.entity == self.block_6_5:
                self.player.SPEED = boostSpeed * 4
            if hit.entity == self.block_6_6:
                self.player.SPEED = boostSpeed * 5
            if hit.entity == self.block_6_7:
                self.player.SPEED = boostSpeed * 5.3
            if hit.entity == self.block_6_8:
                self.player.SPEED = normalSpeed
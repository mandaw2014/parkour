from ursina import *
import sys
sys.path.append('../Parkour/')
from block import *

normalSpeed = 2
boostSpeed  = 3
normalJump = 0.3

# Level02
class Level02(Entity):
    def __init__(self):
        super().__init__()

        self.block_2_1 = NormalBlock(position = (0, 1, 12))
        self.block_2_2 = NormalBlock(position = (0, 2, 20))
        self.block_2_3 = JumpBlock(position = (0, -20, 30))
        self.block_2_4 = NormalBlock(position = (0, 10, 42))
        self.block_2_5 = NormalBlock(position = (0, 10, 50))
        self.block_2_6 = SpeedBlock(position = (0, 10, 62))
        self.block_2_7 = NormalBlock(position = (0, 11, 74))
        self.finishBlock_2 = EndBlock(position = (0, 11, 88))
        self.ground_2 = StartBlock()

        self.player = None

        self.disable()

    def speed(self):
        self.player.SPEED = normalSpeed

    def disable(self):
       self.block_2_1.disable()
       self.block_2_2.disable()
       self.block_2_3.disable()
       self.block_2_4.disable()
       self.block_2_5.disable()
       self.block_2_6.disable()
       self.block_2_7.disable()
       self.finishBlock_2.disable()
       self.ground_2.disable()

    def enable(self):
       self.block_2_1.enable()
       self.block_2_2.enable()
       self.block_2_3.enable()
       self.block_2_4.enable()
       self.block_2_5.enable()
       self.block_2_6.enable()
       self.block_2_7.enable()
       self.finishBlock_2.enable()
       self.ground_2.enable()

    def update(self):
        # What entity the player hits
        hit = raycast(self.player.position, self.player.down, distance = 2, ignore = [self.player, ])
        
        if self.ground_2.enabled == True:
            if hit.entity == self.block_2_3:
                self.player.jump_height = 1.2
            elif hit.entity != self.block_2_3:
                self.player.jump_height = normalJump

            if self.block_2_6.enabled == True:
                if hit.entity == self.block_2_6:
                    self.player.SPEED = boostSpeed * 1.5
                    invoke(self.speed, delay=3)
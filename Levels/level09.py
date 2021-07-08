from ursina import *
import sys
sys.path.append('../Parkour/')
from block import *

normalSpeed = 2
boostSpeed  = 3
normalJump = 0.3

# Level09
class Level09(Entity):
    def __init__(self):
        super().__init__()

        self.block_9_1 = NormalBlock(position = (0, 1, 13))
        self.block_9_2 = FakeBlock(position = (0, 1, 22))
        self.block_9_3 = NormalBlock(position = (-6, 1, 22))
        self.block_9_4 = NormalBlock(position = (6, 1, 22))
        self.block_9_5 = NormalBlock(position = (0, 1, 29))
        self.block_9_6 = FakeBlock(position = (0, 1, 40))
        self.block_9_7 = NormalBlock(position = (0, -49, 40))
        self.block_9_8 = JumpBlock(position = (0, -49, 51))
        self.block_9_9 = FakeBlock(position = (0, 100, 70))
        self.block_9_10 = NormalBlock(position = (0, 100, 80))
        self.block_9_11 = SpeedBlock(position = (0, 100, 90))

        self.ground_9 = StartBlock()
        self.finishBlock_9 = EndBlock(position = (0, 150, 300))

        self.player = None

        self.disable()

    def speed(self):
        self.player.SPEED = normalSpeed

    def disable(self):
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
       self.finishBlock_9.disable()
       self.ground_9.disable()

    def enable(self):
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
       self.finishBlock_9.enable()
       self.ground_9.enable()

    def update(self):
        # What entity the player hits
        hit = raycast(self.player.position, self.player.down, distance = 2, ignore = [self.player, ])
        
        if self.ground_9.enabled == True:
            if hit.entity == self.block_9_8:
                self.player.jump_height = 3
            elif hit.entity != self.block_9_8:
                self.player.jump_height = normalJump
            if hit.entity == self.block_9_11:
                self.player.SPEED = boostSpeed * 4
                self.player.jump_height = 2
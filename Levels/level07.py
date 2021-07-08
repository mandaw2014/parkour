from ursina import *
import sys
sys.path.append('../Parkour/')
from block import *

normalSpeed = 2
boostSpeed  = 3
normalJump = 0.3

# Level07
class Level07(Entity):
    def __init__(self):
        super().__init__()

        self.block_7_1 = NormalBlock(position = (0, 1, 10))
        self.block_7_2 = Wall(position = (0, 3, 15))
        self.block_7_3 = NormalBlock(position = (0, 1, 20))
        self.block_7_4 = Wall(position = (0, 3, 25))
        self.block_7_5 = NormalBlock(position = (0, 1, 30))
        self.block_7_6 = Wall(position = (0, 3, 35))
        self.block_7_7 = NormalBlock(position = (0, 1, 40))
        self.block_7_8 = Wall(position = (0, 3, 45))
        self.block_7_9 = NormalBlock(position = (0, 1, 50))
        self.block_7_10 = Wall(position = (0, 3, 55))
        self.block_7_11 = NormalBlock(position = (0, 1, 60))
        self.block_7_12 = WeirdBlock(position = (0, 1, 73))
        self.block_7_13 = NormalBlock(position = (0, 1, 85))

        self.ground_7 = StartBlock()
        self.finishBlock_7 = EndBlock(position = (0, 1, 95))

        self.player = None

        self.disable()

    def speed(self):
        self.player.SPEED = normalSpeed

    def disable(self):
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
       self.finishBlock_7.disable()
       self.ground_7.disable()

    def enable(self):
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
       self.finishBlock_7.enable()
       self.ground_7.enable()

    def update(self):
        # What entity the player hits
        hit = raycast(self.player.position, self.player.down, distance = 2, ignore = [self.player, ])
        
        if self.ground_7.enabled == True:
            if hit.entity == self.block_7_12:
                camera.rotation_z = 180
            if hit.entity == self.finishBlock_7:
                camera.rotation_z = 0
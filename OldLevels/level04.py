from ursina import *
import sys
sys.path.append('../Parkour/')
from block import *

normalSpeed = 2
boostSpeed  = 3
normalJump = 0.3

# Level04
class Level04(Entity):
    def __init__(self):
        super().__init__()

        self.block_4_1 = NormalBlock(position = (0, 1, 12))
        self.block_4_2 = NormalBlock(position = (0, 2, 20))
        self.block_4_3 = JumpBlock(position = (0, -49, 40))
        self.block_4_4 = NormalBlock(position = (0, 50, 60))
        self.block_4_5 = SpeedBlock(position = (0, 50, 93), scale = (3, 0.5, 50))
        self.block_4_6 = JumpBlock(position = (0, 15, 163))

        self.ground_4 = Entity(model = "cube", scale_x = 10, scale_z = 10, collider = "box", texture = "white_cube", color = "#CACACA")
        self.finishBlock_4 = Entity(model = "cube", scale_x = 10, scale_z = 10, collider = "box", texture = "white_cube", color = "#CACACA", position = (0, 20, 240))

        self.player = None

        self.disable()

    def speed(self):
        self.player.SPEED = normalSpeed

    def disable(self):
       self.block_4_1.disable()
       self.block_4_2.disable()
       self.block_4_3.disable()
       self.block_4_4.disable()
       self.block_4_5.disable()
       self.block_4_6.disable()
       self.finishBlock_4.disable()
       self.ground_4.disable()

    def enable(self):
       self.block_4_1.enable()
       self.block_4_2.enable()
       self.block_4_3.enable()
       self.block_4_4.enable()
       self.block_4_5.enable()
       self.block_4_6.enable()
       self.finishBlock_4.enable()
       self.ground_4.enable()

    def update(self):
        # What entity the player hits
        hit = raycast(self.player.position, self.player.down, distance = 2, ignore = [self.player, ])
        
        if self.ground_4.enabled == True:
            if hit.entity == self.block_4_3:
                self.player.jump_height = 2
            elif hit.entity != self.block_4_3:
                self.player.jump_height = normalJump

            if hit.entity == self.block_4_5:
                self.player.SPEED = boostSpeed * 2

            if hit.entity == self.block_4_6:
                self.player.jump_height = 1.3
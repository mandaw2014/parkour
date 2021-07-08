from ursina import *
import sys
sys.path.append('../Parkour/')
from block import *

normalSpeed = 2
boostSpeed  = 3
normalJump = 0.3

# Level05
class Level05(Entity):
    def __init__(self):
        super().__init__()

        self.block_5_1 = NormalBlock(position = (0, 1, 10))
        self.block_5_2 = NormalBlock(position = (-3, 1, 18), rotation = (0, 0, 30))
        self.block_5_3 = NormalBlock(position = (3, 1, 26), rotation = (0, 0, -30))
        self.block_5_4 = NormalBlock(position = (-3, 1, 34), rotation = (0, 0, 30))
        self.block_5_5 = NormalBlock(position = (3, 1, 42), rotation = (0, 0, -30))
        self.block_5_6 = NormalBlock(position = (-3, 1, 50), rotation = (0, 0, 30))
        self.block_5_7 = NormalBlock(position = (3, 1, 58), rotation = (0, 0, -30))
        self.block_5_8 = NormalBlock(position = (-3, 1, 66), rotation = (0, 0, 30))
        self.block_5_9 = SpeedBlock(position = (0, 1, 78))
        self.block_5_10 = WeirdBlock(position = (0, 1, 95))

        self.ground_5 = Entity(model = "cube", scale_x = 10, scale_z = 10, collider = "box", texture = "white_cube", color = "#CACACA")
        self.finishBlock_5 = Entity(model = "cube", scale_x = 10, scale_z = 10, collider = "box", texture = "white_cube", color = "#CACACA", position = (0, 1, 112))

        self.player = None

        self.disable()

    def speed(self):
        self.player.SPEED = normalSpeed

    def disable(self):
       self.block_5_1.disable()
       self.block_5_2.disable()
       self.block_5_3.disable()
       self.block_5_4.disable()
       self.block_5_5.disable()
       self.block_5_6.disable()
       self.block_5_7.disable()
       self.block_5_8.disable()
       self.block_5_9.disable()
       self.block_5_10.disable()
       self.finishBlock_5.disable()
       self.ground_5.disable()

    def enable(self):
       self.block_5_1.enable()
       self.block_5_2.enable()
       self.block_5_3.enable()
       self.block_5_4.enable()
       self.block_5_5.enable()
       self.block_5_6.enable()
       self.block_5_7.enable()
       self.block_5_8.enable()
       self.block_5_9.enable()
       self.block_5_10.enable()
       self.finishBlock_5.enable()
       self.ground_5.enable()

    def update(self):
        # What entity the player hits
        hit = raycast(self.player.position, self.player.down, distance = 2, ignore = [self.player, ])
        
        if self.ground_5.enabled == True:
            if hit.entity == self.block_5_9:
                self.player.SPEED = boostSpeed * 2
            elif hit.entity == self.block_5_9:
                invoke(self.speed, delay = 1)

            if hit.entity == self.block_5_10:
                camera.rotation_z = 180
        
            if hit.entity == self.finishBlock_5:
                camera.rotation_z = 0
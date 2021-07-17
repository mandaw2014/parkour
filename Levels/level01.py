from player import Player
from ursina import *
import sys
sys.path.append('../Parkour/')
from block import *

normalSpeed = 2
boostSpeed  = 5
normalJump = 0.3

#Level01
class Level01(Entity):
    def __init__(self):
        super().__init__()

        self.is_enabled = True

        self.player = None

        self.mountain = Entity(model = "mountain_level_1.obj", texture = "mountain_level_1.png", collider = "mesh", scale = (100, 100, 100), position = (800, 0, 0))

        self.block_1_1 = NormalBlock((881, 10, 9), (0, -141.3, 0))
        self.block_1_2 = NormalBlock((875, 12, 1.5), (0, -142, 0))
        self.block_1_3 = NormalBlock((867.5, 14, -8.3), (0, -142, 0))
        self.block_1_4 = NormalBlock((861, 16, -17), (0, -142, 0))
        self.block_1_5 = NormalBlock((855, 18, -25), (0, -142, 0))
        self.block_1_6 = NormalBlock((848, 20, -34), (0, -142, 0))
        self.block_1_7 = NormalBlock((838.5, 22, -42), (0, -124.8, 0))
        self.block_1_8 = NormalBlock((827.6, 24, -48), (0, -122.183, 0))

        self.block_1_9 = NormalBlock((787.3, 27, -96.4), (0, -179, 0))
        self.block_1_10 = SpeedBlock((787.3, 27, -113), (0, -179, 0))

        self.block_1_11 = NormalBlock((787.3, 27, -146), (0, -179, 0))
        self.block_1_12 = NormalBlock((787.5, 27.9, -159.6), (0, -179, 0))
        self.block_1_13 = NormalBlock((787.5, 29, -172.6), (0, -179, 0))
        self.block_1_14 = NormalBlock((787.5, 31, -185.6), (0, -179, 0))
        self.block_1_15 = JumpBlock((787.5, 27.3, -199.6), (0, -179, 0))

        self.block_1_16 = JumpBlock((757.7, 43, -199.2), (0, -179, 0))

        self.block_1_17 = NormalBlock((725.5, 86, -184.5), (0, -179, 0))
        self.block_1_18 = NormalBlock((714.3, 88, -184.5), (0, -179, 0))
        self.block_1_19 = NormalBlock((700.3, 90, -184.5), (0, -179, 0))
        self.block_1_20 = NormalBlock((700.4, 92, -172), (0, -179, 0))
        self.block_1_21 = NormalBlock((700.8, 94.7, -158.1), (0, -179, 0))
        self.block_1_22 = NormalBlock((686.9, 96, -158.1), (0, -179, 0))

        self.block_1_23 = JumpBlock((675.4, 96, -158.1), (0, -179, 0))

        self.block_1_24 = NormalBlock((675.4, 138, -120), (0, -179, 0))
        self.block_1_25 = NormalBlock((675.3, 140, -107), (0, -179, 0))

        self.block_1_26 = NormalBlock((675, 141, -90), scale = (10, 0.8, 10))
        self.finishBlock_1 = EndBlock((675, 143.5, -90))

        # self.disable()

    def disable(self):
        self.is_enabled = False

        self.mountain.disable()

        self.block_1_1.disable()
        self.block_1_2.disable()
        self.block_1_3.disable()
        self.block_1_4.disable()
        self.block_1_5.disable()
        self.block_1_6.disable()
        self.block_1_7.disable()
        self.block_1_8.disable()
        self.block_1_9.disable()
        self.block_1_10.disable()
        self.block_1_11.disable()
        self.block_1_12.disable()
        self.block_1_13.disable()
        self.block_1_14.disable()
        self.block_1_15.disable()
        self.block_1_16.disable()
        self.block_1_17.disable()
        self.block_1_18.disable()
        self.block_1_19.disable()
        self.block_1_20.disable()
        self.block_1_21.disable()
        self.block_1_22.disable()
        self.block_1_23.disable()
        self.block_1_24.disable()
        self.block_1_25.disable()
        self.block_1_26.disable()

        self.finishBlock_1.disable()
    
    def enable(self):
        self.is_enabled = True

        self.mountain.enable()

        self.block_1_1.enable()
        self.block_1_2.enable()
        self.block_1_3.enable()
        self.block_1_4.enable()
        self.block_1_5.enable()
        self.block_1_6.enable()
        self.block_1_7.enable()
        self.block_1_8.enable()
        self.block_1_9.enable()
        self.block_1_10.enable()
        self.block_1_11.enable()
        self.block_1_12.enable()
        self.block_1_13.enable()
        self.block_1_14.enable()
        self.block_1_15.enable()
        self.block_1_16.enable()
        self.block_1_17.enable()
        self.block_1_18.enable()
        self.block_1_19.enable()
        self.block_1_20.enable()
        self.block_1_21.enable()
        self.block_1_22.enable()
        self.block_1_23.enable()
        self.block_1_24.enable()
        self.block_1_25.enable()
        self.block_1_26.enable()

        self.finishBlock_1.disable()

    def speed(self):
        self.player.SPEED = normalSpeed

    def update(self):
        # Stops the player from falling forever
        if self.is_enabled == True and self.player.position.y <= -50:
            self.player.position = (888, 10, 18)
            self.player.rotation = (0, -142, 0)
            self.player.SPEED = normalSpeed
            self.player.jump_height = normalJump
            self.player.count = 0.0

        # Restart the level
        if self.is_enabled == True and held_keys["g"]:
            self.player.position = (888, 10, 18)
            self.player.rotation = (0, -142, 0)
            self.player.SPEED = normalSpeed
            self.player.jump_height = normalJump
            self.player.count = 0.0
            
        # What entity the player hits
        hit = raycast(self.player.position, self.player.down, distance = 2, ignore = [self.player, ])

        if hit.entity == self.block_1_10:
            self.player.SPEED = boostSpeed
        elif hit.entity == self.block_1_11:
            self.player.SPEED = normalSpeed
        elif hit.entity == self.mountain:
            self.player.SPEED = normalSpeed
            self.player.jump_height = normalJump
        
        if hit.entity == self.block_1_15:
            self.player.jump_height = 1
        if hit.entity == self.block_1_16:
            self.player.jump_height = 1.3
        elif hit.entity == self.block_1_17:
            self.player.jump_height = normalJump

        if hit.entity == self.block_1_23:
            self.player.jump_height = 1.3
        elif hit.entity == self.block_1_24:
            self.player.jump_height = normalJump

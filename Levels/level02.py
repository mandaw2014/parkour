from ursina import *
import sys
sys.path.append('../Parkour/')
from block import *

normalSpeed = 2
boostSpeed  = 5
normalJump = 0.3

# Level02
class Level02(Entity):
    def __init__(self):
        super().__init__()

        self.is_enabled = False

        self.mountain = Entity(model = "mountain_level_2.obj", texture = "mountain_level_2.png", collider = "mesh", scale = (50, 50, 50), position = (800, 0, 0))

        self.block_2_1 = NormalBlock((827, 14, 108))
        self.block_2_2 = NormalBlock((840, 16, 108))
        self.block_2_3 = NormalBlock((853, 18, 108))
        self.block_2_4 = NormalBlock((866, 20, 108))
        self.block_2_5 = NormalBlock((879, 22, 108))
        self.block_2_6 = NormalBlock((892, 24, 108))
        self.block_2_7 = NormalBlock((892, 26, 95)) 
        self.block_2_8 = NormalBlock((892, 28, 82)) 
        self.block_2_9 = NormalBlock((892, 30, 69)) 
        self.block_2_10 = NormalBlock((892, 32, 56)) 
        self.block_2_11 = NormalBlock((892, 34, 43)) 

        self.block_2_12 = JumpBlock((892, 28, 26))

        self.block_2_13 = NormalBlock((885, 46, -19))
        self.block_2_14 = SpeedBlock((885, 46, -35))

        self.block_2_15 = NormalBlock((870, 45, -60))
        self.block_2_16 = NormalBlock((860, 46, -68))
        self.block_2_17 = JumpBlock((848, 46, -68))

        self.block_2_18 = NormalBlock((815.6, 100.5, -44.5))
        self.block_2_19 = JumpBlock(((805, 100.5, -44.5)))
        self.block_2_20 = NormalBlock((790, 112, -44.5))
        self.block_2_21 = NormalBlock((777, 112, -44.5))
        self.block_2_22 = NormalBlock((764, 114, -44.5))
        self.block_2_23 = NormalBlock((751, 114, -44.5))
        self.block_2_24 = JumpBlock((751, 116, -31.5))

        self.block_2_25 = NormalBlock((768, 135, 42))
        self.block_2_26 = NormalBlock((781, 137, 42))
        self.block_2_27 = NormalBlock((794, 139, 42))
        self.block_2_28 = NormalBlock((807, 141, 42))
        self.block_2_29 = NormalBlock((820, 143, 42))
        self.block_2_30 = NormalBlock((833, 145, 42))
        self.block_2_31 = NormalBlock((846, 147, 42))
        self.block_2_32 = JumpBlock((846, 147, 29))
        self.block_2_33 = JumpBlock((846, 179, 6))

        self.block_2_34 = NormalBlock((829, 212, 6))
        self.block_2_35 = NormalBlock((809, 213, 6), scale = (10, 0.8, 10))
        
        self.finishBlock_2 = EndBlock((809, 215, 6))

        self.player = None

        self.disable()

    def disable(self):
        self.is_enabled = False

        self.mountain.disable()

        self.block_2_1.disable()
        self.block_2_2.disable()
        self.block_2_3.disable()
        self.block_2_4.disable()
        self.block_2_5.disable()
        self.block_2_6.disable()
        self.block_2_7.disable()
        self.block_2_8.disable()
        self.block_2_9.disable()
        self.block_2_10.disable()
        self.block_2_11.disable()
        self.block_2_12.disable()
        self.block_2_13.disable()
        self.block_2_14.disable()
        self.block_2_15.disable()
        self.block_2_16.disable()
        self.block_2_17.disable()
        self.block_2_18.disable()
        self.block_2_19.disable()
        self.block_2_20.disable()
        self.block_2_21.disable()
        self.block_2_22.disable()
        self.block_2_23.disable()
        self.block_2_24.disable()
        self.block_2_25.disable()
        self.block_2_26.disable()
        self.block_2_27.disable()
        self.block_2_28.disable()
        self.block_2_29.disable()
        self.block_2_30.disable()
        self.block_2_31.disable()
        self.block_2_32.disable()
        self.block_2_33.disable()
        self.block_2_34.disable()
        self.block_2_35.disable()

        self.finishBlock_2.disable()
    
    def enable(self):
        self.is_enabled = True

        self.mountain.enable()

        self.block_2_1.enable()
        self.block_2_2.enable()
        self.block_2_3.enable()
        self.block_2_4.enable()
        self.block_2_5.enable()
        self.block_2_6.enable()
        self.block_2_7.enable()
        self.block_2_8.enable()
        self.block_2_9.enable()
        self.block_2_10.enable()
        self.block_2_11.enable()
        self.block_2_12.enable()
        self.block_2_13.enable()
        self.block_2_14.enable()
        self.block_2_15.enable()
        self.block_2_16.enable()
        self.block_2_17.enable()
        self.block_2_18.enable()
        self.block_2_19.enable()
        self.block_2_20.enable()
        self.block_2_21.enable()
        self.block_2_22.enable()
        self.block_2_23.enable()
        self.block_2_24.enable()
        self.block_2_25.enable()
        self.block_2_26.enable()
        self.block_2_27.enable()
        self.block_2_28.enable()
        self.block_2_29.enable()
        self.block_2_30.enable()
        self.block_2_31.enable()
        self.block_2_32.enable()
        self.block_2_33.enable()
        self.block_2_34.enable()
        self.block_2_35.enable()

        self.finishBlock_2.enable()

    def speed(self):
        self.player.SPEED = normalSpeed

    def update(self):
        # Stops the player from falling forever
        if self.is_enabled == True and self.player.position.y <= -50:
            self.player.position = (811, 14, 108)
            self.player.rotation = (0, -267, 0)
            self.player.SPEED = normalSpeed
            self.player.jump_height = normalJump
            self.player.count = 0.0

        # Restart the level
        if self.is_enabled == True and held_keys["g"]:
            self.player.position = (811, 14, 108)
            self.player.rotation = (0, -267, 0)
            self.player.SPEED = normalSpeed
            self.player.jump_height = normalJump
            self.player.count = 0.0

        # What entity the player hits
        hit = raycast(self.player.position, self.player.down, distance = 2, ignore = [self.player, ])

        if hit.entity == self.mountain:
            self.player.jump_height = 0.3
            self.player.SPEED = 2

        if hit.entity == self.block_2_12:
            self.player.jump_height = 0.8
        elif hit.entity == self.block_2_11:
            self.player.jump_height = normalJump
        if hit.entity == self.block_2_14:
            self.player.SPEED = 5
        elif hit.entity == self.block_2_15:
            self.player.SPEED = normalSpeed
        elif hit.entity == self.block_2_16:
            self.player.SPEED = normalSpeed
        if hit.entity == self.block_2_17:
            self.player.jump_height = 1.5
        elif hit.entity == self.block_2_18:
            self.player.jump_height = normalJump
        if hit.entity == self.block_2_19:
            self.player.jump_height = 0.7
        elif hit.entity == self.block_2_20:
            self.player.jump_height = normalJump
        if hit.entity == self.block_2_24:
            self.player.jump_height = 0.8
        if hit.entity == self.block_2_32:
            self.player.jump_height = 1
        if hit.entity == self.block_2_33:
            self.player.jump_height = 1.2
        elif hit.entity == self.block_2_34 or hit.entity == self.block_2_35:
            self.player.jump_height = normalJump
            
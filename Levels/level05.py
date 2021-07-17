from ursina import *
import sys
sys.path.append('../Parkour/')
from block import *

normalSpeed = 2
boostSpeed  = 5
normalJump = 0.3

# Level05
class Level05(Entity):
    def __init__(self):
        super().__init__()

        self.is_enabled = False
        self.on = False

        self.level = Entity(model = "lava_level_5.obj", color = "#454545", collider = "mesh", scale = (10, 10, 10))
        self.lava = Entity(model = "plane", color = "#ff6700", collider = "mesh", scale = (1000, 1, 1000), position = (0, -15, 0))

        self.block_5_1 = NormalBlock((-1, -8, 15))
        self.block_5_2 = NormalBlock((-1, -6, 0))
        self.block_5_3 = NormalBlock((-1, -4, -15))
        self.block_5_4 = NormalBlock((-1, -2, -30))
        self.block_5_5 = NormalBlock((-1, 0, -45))
        self.block_5_6 = NormalBlock((-1, 2, -60))
        self.block_5_7 = NormalBlock((-1, 4, -75))
        self.block_5_8 = NormalBlock((-1, 6, -90))
        self.block_5_9 = JumpBlock((-1, 6, -105))

        self.block_5_10 = NormalBlock((-1, 20, -129))

        self.block_5_11 = SpeedBlock((-1, -9, -160))
        self.block_5_12 = SpeedBlock((-1, -9, -190))
        self.block_5_13 = SpeedBlock((-1, -9, -220))
        self.block_5_14 = SpeedBlock((-1, -9, -260))
        
        self.block_5_15 = EndBlock((-1, -9, -313))

        self.block_5_16 = NormalBlock((-1, 15, -320))
        self.finishBlock_5 = EndBlock((-1, 16, -334))

        self.player = None

        self.disable()

    def disable(self):
        self.is_enabled = False
        self.on = False

        self.level.disable()
        self.lava.disable()

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
        self.block_5_11.disable()
        self.block_5_12.disable()
        self.block_5_13.disable()
        self.block_5_14.disable()
        self.block_5_15.disable()
        self.block_5_16.disable()

        self.finishBlock_5.disable()

    def enable(self):
        self.is_enabled = True
        self.on = True

        self.level.enable()
        self.lava.enable()

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
        self.block_5_11.enable()
        self.block_5_12.enable()
        self.block_5_13.enable()
        self.block_5_14.enable()
        self.block_5_15.enable()
        self.block_5_16.enable()

        self.finishBlock_5.enable()

    def speed(self):
        self.player.SPEED = normalSpeed

    def update(self):
        # Stops the player from falling forever
        if self.on == True and self.player.position.y <= -50:
            self.player.SPEED = normalSpeed
            self.player.jump_height = normalJump
            self.player.position = (-1, -5, 34)
            self.player.rotation = (0, -180, 0)
            self.player.count = 0.0

        # Restart the level
        if self.on == True and held_keys["g"]:
            self.player.SPEED = normalSpeed
            self.player.jump_height = normalJump
            self.player.position = (-1, -5, 34)
            self.player.rotation = (0, -180, 0)
            self.player.count = 0.0

        # What entity the player hits
        hit = raycast(self.player.position, self.player.down, distance = 2, ignore = [self.player, ])

        if hit.entity == self.level:
            self.player.SPEED = normalSpeed
            self.player.jump_height = normalJump

        if hit.entity == self.lava:
            self.player.position = (-1, -9, 34)
            self.player.rotation = (0, 180, 0)
            self.player.SPEED = normalSpeed
            self.player.jump_height = normalJump
            self.player.count = 0.0

        if hit.entity == self.block_5_9:
            self.player.jump_height = 0.8
        elif hit.entity == self.block_5_10:
            self.player.jump_height = normalJump
        
        if hit.entity == self.block_5_11:
            self.player.jump_height = normalJump
            self.player.SPEED = 4
        if hit.entity == self.block_5_12:
            self.player.SPEED = 5
        if hit.entity == self.block_5_13:
            self.player.SPEED = 5
        if hit.entity == self.block_5_14:
            self.player.SPEED = 6

        if hit.entity == self.block_5_15:
            self.player.jump_height = 0.85
        elif hit.entity == self.block_5_16:
            self.player.jump_height = normalJump

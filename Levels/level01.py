from ursina import *
import sys
sys.path.append('../Parkour/')
from block import *

normalSpeed = 2
boostSpeed  = 3
normalJump = 0.3

#Level01
class Level01(Entity):
    def __init__(self):
        super().__init__()
        self.block_1_1 = NormalBlock((0, 1, 12))
        self.block_1_2 = NormalBlock((0, 2, 20))
        self.block_1_3 = NormalBlock((0, 3, 28))
        self.block_1_4 = NormalBlock((0, 4, 36))
        self.block_1_5 = NormalBlock((8, 5, 36))
        self.block_1_6 = NormalBlock((16, 6, 36))
        self.block_1_7 = JumpBlock((24, 2, 36))
        self.block_1_8 = NormalBlock((32, 10, 36))
        self.block_1_9 = SpeedBlock((32, 10, 46))

        self.ground_1 = StartBlock()
        self.finishBlock_1 = EndBlock((32, 10, 62))

        self.player = None

    def speed(self):
        self.player.SPEED = normalSpeed

    def disable(self):
       self.block_1_1.disable()
       self.block_1_2.disable()
       self.block_1_3.disable()
       self.block_1_4.disable()
       self.block_1_5.disable()
       self.block_1_6.disable()
       self.block_1_7.disable()
       self.block_1_8.disable()
       self.block_1_9.disable()
       self.finishBlock_1.disable()
       self.ground_1.disable()

    def enable(self):
       self.block_1_1.enable()
       self.block_1_2.enable()
       self.block_1_3.enable()
       self.block_1_4.enable()
       self.block_1_5.enable()
       self.block_1_6.enable()
       self.block_1_7.enable()
       self.block_1_8.enable()
       self.block_1_9.enable()
       self.finishBlock_1.enable()
       self.ground_1.enable()

    def update(self):
        # Stops the player from falling forever
        if self.player.position.y <= -50:
            self.player.position = Vec3(0, 5, 0)
            self.player.SPEED = normalSpeed
            self.player.jump_height = normalJump
            camera.rotation = (0, 0, 0)

        # Restart the level
        if held_keys["g"]:
            self.player.position = Vec3(0, 5, 0)
            self.player.SPEED = normalSpeed
            self.player.jump_height = normalJump
            camera.rotation = (0, 0, 0)

        # What entity the player hits
        hit = raycast(self.player.position, self.player.down, distance = 2, ignore = [self.player, ])
        
        if self.ground_1.enabled == True:
            if hit.entity == self.block_1_7:
                self.player.jump_height = 0.7
            elif hit.entity != self.block_1_7:
                self.player.jump_height = normalJump

            if hit.entity == self.block_1_9:
                self.player.SPEED = boostSpeed * 1.2
                invoke(self.speed, delay=3)

            if hit.entity == self.finishBlock_1:
                pass
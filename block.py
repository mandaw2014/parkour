from ursina import *

# Normal Block Class
class NormalBlock(Entity):
    def __init__(self, position = (0, 0, 0), rotation = (0, 0, 0)):
        super().__init__(
            model = "cube",
            scale = Vec3(5, 0.8, 5),
            color = "#AFFF3C",
            collider = "box",
            texture = "white_cube",
            position = position,
            rotation = rotation,
        )

# Jump Block Class
class JumpBlock(Entity):
    def __init__(self, position = (0, 0, 0), rotation = (0, 0, 0)):
        super().__init__(
            model = "cube",
            scale = Vec3(5, 0.8, 5),
            color = "#FF8B00",
            collider = "box",
            texture = "white_cube",
            position = position,
            rotation = rotation
        )

# Speed Block Class
class SpeedBlock(Entity):
    def __init__(self, position = (0, 0, 0), rotation = (0, 0, 0), scale = (5, 0.5, 10)):
        super().__init__(
            model = "cube",
            scale = scale,
            color = "#53FFF5",
            collider = "box",
            texture = "white_cube",
            position = position,
            rotation = rotation
        )

# Slow Block Class
class SlowBlock(Entity):
    def __init__(self, position = (0, 0, 0), rotation = (0, 0, 0)):
        super().__init__(
            model = "cube",
            scale = Vec3(5, 0.5, 15),
            color = "#FF453F",
            collider = "box",
            texture = "white_cube",
            position = position,
            rotation = rotation
        )

class WeirdBlock(Entity):
    def __init__(self, position = (0, 0, 0), rotation = (0, 0, 0)):
        super().__init__(
            model = "cube",
            scale = Vec3(5, 0.5, 15),
            color = "#7116FE",
            collider = "box",
            texture = "white_cube",
            position = position,
            rotation = rotation
        )

class Wall(Entity):
    def __init__(self, position = (0, 0, 0), rotation = (0, 0, 90)):
        super().__init__(
            model = "cube",
            scale = (5, 4, 1),
            color = "#AFFF3C",
            collider = "box",
            texture = "white_cube",
            position = position,
            rotation = rotation,
        )

class MovingBlock(Entity):
    def __init__(self, position = (0, 0, 0), rotation = (0, 0, 0)):
        super().__init__(
            model = "cube",
            scale = Vec3(5, 0.8, 5),
            color = "#2D49FB",
            collider = "box",
            texture = "white_cube",
            position = position,
            rotation = rotation
        )
    
class FakeBlock(Entity):
    def __init__(self, position = (0, 0, 0), rotation = (0, 0, 0)):
        super().__init__(
            model = "cube",
            scale = Vec3(5, 0.8, 5),
            color = "#25B701",
            texture = "white_cube",
            position = position,
            rotation = rotation
        )

class StartBlock(Entity):
    def __init__(self, position = (0, 0, 0), rotation = (0, 0, 0)):
        super().__init__(
            model = "cube",
            scale_x = 10,
            scale_z = 10,
            color = "#CACACA",
            collider = "box",
            texture = "white_cube",
            position = position,
            rotation = rotation
        )

class EndBlock(Entity):
    def __init__(self, position = (0, 0, 0), rotation = (0, 0, 0)):
        super().__init__(
            model = "cube",
            scale = (5, 5, 5),
            color = "#2D49FB",
            collider = "box",
            texture = "white_cube",
            position = position,
            rotation = rotation
        )

from ursina import *
import math

sign = lambda x: -1 if x < 0 else (1 if x > 0 else 0)

class Player(Entity):
    def __init__(self, model, position, collider, scale = (1, 1, 1), SPEED = 2, MAXSPEED = 3, velocity = (0, 0, 0), MAXJUMP = 1, gravity = 1, controls = "wasd", **kwargs):
        super().__init__(
            model = "cube", 
            position = position,
            scale = (1, 1, 1), 
            visible_self = False
        )

        self.collider = BoxCollider(self, center = Vec3(0, 1, 0), size = Vec3(1, 2, 1))
        mouse.locked = True
        camera.parent = self
        camera.position = (0, 2, 0)
        camera.rotation = (0, 0, 0)
        camera.fov = 100
        self.velocity_x, self.velocity_y, self.velocity_z = velocity
        self.SPEED = SPEED
        self.MAXJUMP = MAXJUMP
        self.jump_count = 0
        self.gravity = gravity
        self.jump_height = 0.3
        self.slope = 40
        self.controls = controls
        self.sensibility = 70
        self.momentum = 0

        self.time_running = False
        self.count = 0.0
        self.time = Text(text = str(round(self.count)), origin = (0, 0), size = 0.05, position = Vec2(-0.73, 0.44))
        self.time.disable()
        
        for key, value in kwargs.items():
            try:
                setattr(self, key, value)
            except:
                print(key, value)

    def jump(self):
        self.velocity_y = self.jump_height * 40
        self.jump_count += 1

    def update(self):
        if self.time_running:
            self.time.enable()
            self.count += time.dt
            self.time.text = str(round(self.count, 1))

        ray = raycast(self.position, self.down, distance = 2, ignore = [self, ])

        y_movement = self.velocity_y * time.dt

        direction = (0, sign(y_movement), 0)
        yRay = boxcast(origin = self.world_position, direction=direction,
                        distance=self.scale_y/2+abs(y_movement), ignore=[self, ])
        if yRay.hit:
            move = False
            self.jump_count = 0
            self.velocity_y = 0
        else :
            self.y += y_movement
            self.velocity_y -= self.gravity * time.dt * 25

        x_movement = (self.forward[0] * held_keys[self.controls[0]] +
                      self.left[0] * held_keys[self.controls[1]] +
                      self.back[0] *  held_keys[self.controls[2]] +
                      self.right[0] * held_keys[self.controls[3]]) * time.dt * 6 * self.SPEED

        z_movement = (self.forward[2] * held_keys[self.controls[0]] +
                      self.left[2] * held_keys[self.controls[1]] +
                      self.back[2] * held_keys[self.controls[2]] +
                      self.right[2] * held_keys[self.controls[3]]) * time.dt * 6 * self.SPEED

        if x_movement != 0:
            direction = (1, 0, 0)

            if x_movement < 0:
                direction = (-1, 0, 0)

            xRay = boxcast(origin=self.world_position, direction=direction,
                            distance=self.scale_x / 2 + abs(x_movement), ignore=[self, ])
            move = True

            if xRay.hit:
                move = False
            if move:
                self.x += x_movement
            
            else:
                BottomXRay = raycast(origin = self.world_position + (self.scale_x / 2 * direction[0], -self.scale_y / 2, 0), direction = direction,
                                        distance = abs(x_movement), ignore = [self, ])
                if BottomXRay.hit:
                    TopXRay = raycast(origin = self.world_position + (self.scale_x / 2 * direction[0], -self.scale_y / 2 + 0.1, 0), distance = max(
                        x_movement, self.scale_x), direction = direction, ignore = [self, ]
                    )

                    if TopXRay.hit:
                        if TopXRay.distance - BottomXRay.distance + 0.00001 >= 0.1 / math.tan(math.radians(self.slope)):
                            self.x += x_movement
                            HeightRay = raycast(origin = self.world_position + (self.scale_x / 2 * direction[0], self.scale_y / 2, 0), direction = (
                                0, -1, 0), distance = self.scale_y, ignore = [self, ])
                            if HeightRay.hit:
                                self.y += round(self.scale_y - HeightRay.distance + 0.000005, 5)
                    else:
                        self.x += x_movement
                        HeightRay = raycast(origin = self.world_position+(self.scale_x / 2 * direction[0], self.scale_y / 2, 0), direction = (0, -1, 0), distance = self.scale_y, ignore = [self, ])
                        
                        if HeightRay.hit:
                            self.y += round(self.scale_y - HeightRay.distance + 0.000005, 5)

        if z_movement != 0:
            direction = (0, 0, 1)
            if z_movement < 0:
                direction = (0, 0, -1)

            zRay = boxcast(origin = self.world_position, direction = direction, distance = self.scale_z / 2 + abs(z_movement), ignore = [self, ])
            
            move = True

            if zRay.hit:
                move = False
            if move:
                self.z += z_movement
            else:
                BottomZRay = raycast(origin = self.world_position + (0, -self.scale_y / 2, self.scale_z / 2 * direction[2]), direction = direction, distance = abs(z_movement), ignore = [self, ])
                
                if BottomZRay.hit:
                    TopZRay = raycast(origin = self.world_position + (0, -self.scale_y / 2 + 0.1, self.scale_z / 2 * direction[2]), distance = max(z_movement, self.scale_z), direction = direction, ignore = [self, ])
                    
                    if TopZRay.hit:
                        if TopZRay.distance - BottomZRay.distance + 0.00001 >= 0.1 / math.tan(math.radians(self.slope)):
                            self.z += z_movement

                            HeightRay = raycast(origin = self.world_position + (0, self.scale_y / 2, self.scale_z / 2 * direction[2]), direction = (0, -1, 0), distance = self.scale_y, ignore = [self, ])
                            
                            if HeightRay.hit:
                                self.y += round(self.scale_y - HeightRay.distance + 0.000005, 5)
                    else:
                        self.z += z_movement
                        HeightRay = raycast(origin = self.world_position + (0, self.scale_y / 2, self.scale_z / 2 * direction[2]), direction = (0, -1, 0), distance = self.scale_y, ignore = [self, ])
                        
                        if HeightRay.hit:
                            self.y += round(self.scale_y - HeightRay.distance + 0.000005, 5)


        camera.rotation_x -= mouse.velocity[1] * self.sensibility
        self.rotation_y += mouse.velocity[0] * self.sensibility
        camera.rotation_x = min(max(-80, camera.rotation_x), 80)

    def input(self, key):
        if key == "space":
            if self.jump_count < self.MAXJUMP:
                self.jump()

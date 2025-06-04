import pymunk
import pymunk.pygame_util
import numpy as np

class HillClimbGame:
    def __init__(self):
        self.space = pymunk.Space()
        self.space.gravity = (0, -900)
        self.create_terrain()
        self.create_vehicle()

    def create_terrain(self):
        self.terrain_points = [(x, 100 + 50 * np.sin(x * 0.1)) for x in range(0, 1000, 20)]
        for i in range(len(self.terrain_points) - 1):
            segment = pymunk.Segment(self.space.static_body, self.terrain_points[i], self.terrain_points[i+1], 2)
            segment.friction = 1.0
            self.space.add(segment)

    def create_vehicle(self):
        mass, radius = 5, 15
        moment = pymunk.moment_for_circle(mass, 0, radius)
        self.wheel1 = pymunk.Body(mass, moment)
        self.wheel1.position = 100, 200
        self.wheel2 = pymunk.Body(mass, moment)
        self.wheel2.position = 150, 200
        self.space.add(self.wheel1, self.wheel2)

        s1 = pymunk.Circle(self.wheel1, radius)
        s2 = pymunk.Circle(self.wheel2, radius)
        for s in (s1, s2):
            s.friction = 1.5
            self.space.add(s)

        self.chassis = pymunk.Body(10, 1000)
        self.chassis.position = 125, 220
        shape = pymunk.Poly.create_box(self.chassis, (60, 20))
        self.space.add(self.chassis, shape)

        # Constraints (like springs)
        for a, b in [(self.chassis, self.wheel1), (self.chassis, self.wheel2)]:
            c = pymunk.DampedSpring(a, b, (0, 0), (0, 0), 30, 300, 10)
            self.space.add(c)

    def update(self, dt=1/60.0):
        self.space.step(dt)

    def get_state(self):
        return {
            "wheel1": self.wheel1.position,
            "wheel2": self.wheel2.position,
            "chassis": self.chassis.position,
        }

from manimlib.imports import *

class test(Scene):
    def construct(self):
        plane = ComplexPlane(unit_size = 2)
        plane.add_coordinates()
        self.add(plane)
        self.t_offset = 0
        dot = Dot()
        rate = 0.25
        orbit = Circle(redius = 2)
        def around_circle(mob, dt):
            self.t_offset += (dt * rate)
            mob.move_to(orbit.point_from_prodot.add_updater(around_circle))
        self.add(dot)
        self.wait(5)

test = test()
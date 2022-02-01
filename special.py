from blackhole import Black_Hole
from mobilesimulton import Mobile_Simulton
from random import random

class Special(Black_Hole,Mobile_Simulton):
    def __init__(self,x,y):
        Black_Hole.__init__(self, x, y)
        Mobile_Simulton.__init__(self, x, y, Black_Hole.radius, Black_Hole.radius, 0, 5)
        self.randomize_angle()
        
    def update(self,model):
        Black_Hole.update(self,model)
        x=random()
        if x<.1:
            self.move()
        else:
            y=random()-.2
            z=random()-.5
            if self._speed+y < 4 or self._speed+y > 12:
                self.set_speed(self._speed-y)
            else:
                self.set_speed(self._speed+y)
            self.set_angle(self._angle+z)
            self.move()
            
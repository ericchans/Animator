# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage

from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random


class Floater(Prey): 
    radius=5
    def __init__(self,x,y):
        Prey.__init__(self,x,y,10,10,0,5)
        self.randomize_angle()
    
    def update(self,model):
        x=random()
        if x<.7:
            self.move()
        else:
            y=random()-.5
            z=random()-.5
            if self._speed+y < 3 or self._speed+y > 7:
                self.set_speed(self._speed-y)
            else:
                self.set_speed(self._speed+y)
            self.set_angle(self._angle+z)
            self.move()
    
    def display(self,canvas):
        canvas.create_oval(self._x - Floater.radius, self._y - Floater.radius, self._x + Floater.radius, self._y + Floater.radius, fill='red')

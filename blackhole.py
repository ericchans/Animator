    # Black_Hole is derived from Simulton: i.e., it updates by finding and removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey


class Black_Hole(Simulton):
    radius=10
    def __init__(self,x,y):
        Simulton.__init__(self,x,y,20,20)
        
    def contains(self,xy):
        return self._height/2 >= self.distance(xy)
    
    def update(self,model):
        instance_obj=model.find(lambda x : isinstance(x,Prey))
        inside_obj=model.find(lambda x : self.contains(x.get_location()))
        result=set()
        for i in instance_obj:
            if i in inside_obj:
                result.add(i)
        for i in result:
            model.remove(i)
        return result
    
    def display(self,canvas):
        canvas.create_oval(self._x - self._width/2, self._y - self._height/2, self._x + self._width/2, self._y + self._height/2, fill='black')

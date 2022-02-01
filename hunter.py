# Hunter is derived from the Mobile_Simulton/Pulsator classes: i.e., it updates
#   like a Pulsator, but it also moves (either in a straight line
#   or in pursuit of Prey), and displays as a Pulsator.


from prey import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2


class Hunter(Pulsator, Mobile_Simulton):
    range=200
    def __init__(self,x,y):
        Pulsator.__init__(self, x, y)
        Mobile_Simulton.__init__(self, x, y, Pulsator.radius*2, Pulsator.radius*2, 0, 5)
        self.randomize_angle()
    
    def update(self,model):
        Pulsator.update(self,model)
        instance_obj=model.find(lambda x : isinstance(x,Prey))
        within_range=model.find(lambda x : self.distance(x.get_location()) < Hunter.range)
        prey_in_range=set()
        current=None
        for i in instance_obj:
            if i in within_range:
                prey_in_range.add(i)

        if prey_in_range!= set():
            for i in prey_in_range:
                if current==None:
                    current=i
                elif self.distance(i.get_location())<self.distance(current.get_location()):
                    current=i
            new_ang = atan2(current.get_location()[1] - self.get_location()[1], current.get_location()[0] - self.get_location()[0])
            self.set_angle(new_ang)
        self.move()
            
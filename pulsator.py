# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions


from blackhole import Black_Hole


class Pulsator(Black_Hole): 
    no_eat_counter=30
    def __init__(self,x,y):
        Black_Hole.__init__(self,x,y)
        self.eat_counter=0
    def update(self,model):
        self.eat_counter += 1
        destroyed_obj = Black_Hole.update(self,model)
        if destroyed_obj != set():
            self.eat_counter = 0
            self.change_dimension(len(destroyed_obj),len(destroyed_obj))
        elif self.eat_counter == Pulsator.no_eat_counter:
            self.change_dimension(-1,-1)
            self.eat_counter = 0
        if self._height == 0:
            model.remove(self)
            self.eat_counter = 0
        return destroyed_obj
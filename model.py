import controller, sys
import model   # We need a reference to this module to pass it to update methods

from ball      import Ball
from floater   import Floater
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter
from special import Special

# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
running = False
objects = set()
cycle_count = 0 
saved_item = None

#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running,cycle_count,objects
    running = False
    cycle_count = 0
    objects = set()


#start running the simulation
def start():
    global running
    running = True

#stop running the simulation (freezing it)
def stop():
    global running 
    running = False


#step just one update in the simulation
def step():
    global running
    running=True
    update_all()
    running = False
    


#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global saved_item
    saved_item = kind

#add the kind of remembered object to the simulation (or remove all objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    global saved_item
    if saved_item=='Remove':
        for i in find(lambda a : a.contains((x,y))):
            remove(i)
    elif saved_item!=None:
        add(eval(f'{saved_item}({x},{y})'))


#add simulton s to the simulation
def add(s):
    global objects
    objects.add(s)
    

# remove simulton s from the simulation    
def remove(s):
    global objects
    objects.discard(s)
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    global objects
    result=set()
    for i in objects:
        if p(i):
            result.add(i)
    return result


#call update for every simulton in the simulation (pass each model)
#this function should loop over one set containing all the simultons
#  and should not call type or isinstance: let each simulton do the
#  right thing for itself, without this function knowing what kinds of
#  simultons are in the simulation

def update_all():
    global running, cycle_count,stepping
    if running:
        cycle_count+=1
        current=list(objects)
        for i in current:
            if i in objects:
                i.update(model)

        
#delete every simulton being simulated from the canvas; next call display on every
#  simulton being simulated to add it back to the canvas, possibly in a new location, to
#  animate it; also, update the progress label defined in the controller
#this function should loop over one set containing all the simultons
#  and should not call type or isinstance: let each simulton do the
#  right thing for itself, without this function knowing what kinds of
#  simultons are in the simulation
def display_all():
    global objects
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)
    
    for b in objects:
        b.display(controller.the_canvas)
    
    controller.the_progress.config(text=f'{len(objects)} updates / {cycle_count} cycles')

  

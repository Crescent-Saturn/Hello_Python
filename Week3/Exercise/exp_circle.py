# Expanding circle by timer

###################################################
# Student should add code where relevant to the following.

import simplegui 

WIDTH = 200
HEIGHT = 200
radius = 1


# Timer handler
def tick():
    global radius
    radius += 1    
    if radius >= (WIDTH):
        radius = 1
    
# Draw handler
def draw(canvas):
    canvas.draw_circle((100, 100), 2, radius, 'Red')
        
# Create frame and timer
f = simplegui.create_frame("Expanding circle", WIDTH, HEIGHT)
t = simplegui.create_timer(100,tick)
f.set_draw_handler(draw)

# Start timer
f.start()
t.start()

# template for "Stopwatch: The Game"
import simplegui

# define global variables
t = 0  # Time
x = 0  # number of stops for integer(as 1.0, 2.0, etc.)
y = 0  # Total number of stops

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    a = t//600
    b = (t-a*600)//100
    c = (t-a*600-b*100)//10
    d = t%10
    return str(a)+":"+str(b)+str(c)+"."+str(d)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    #global counter
    timer.start()
        
def stop():
    global y, t, x
    if timer.is_running():
        y += 1
        if (t%10 == 0):
            x += 1
    timer.stop()
#    if (t%10 == 0):
#        x += 1
        
def reset():
    global t
    t = 0
    timer.stop()

# define event handler for timer with 0.1 sec interval

def tick():
    global t
    t += 1    

# define draw handler
def draw(canvas):
    canvas.draw_text(format(t), (50,115), 36, "Red")
    canvas.draw_text("Stops: "+str(x)+"/"+str(y), (75,25), 20, "Red")
    
# create frame
frame = simplegui.create_frame("Stopwatch", 200, 200)
timer = simplegui.create_timer(100, tick)

# register event handlers
frame.set_draw_handler(draw)

frame.add_button("Start",start,100)
frame.add_button("Stop", stop,100)
frame.add_button("Reset",reset,100)

# start frame
frame.start()
timer.stop()

# Please remember to review the grading rubric

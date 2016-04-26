# implementation of card game - Memory

import simplegui
import random
    
cards = range(8)
cards.extend(range(8))

w =50
h =100

exposed = range(16)
for i in exposed:
    exposed[i] = False

# helper function to initialize globals
def new_game():
    pass

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    pass
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global cards, exposed
#    random.shuffle(cards)
    for n in range(len(cards)):
        n_p = w*n+10		# number position
        c_p = [(n*w,0),((n+1)*w,0),((n+1)*w,h),(n*w,h)]		# card position
        if exposed[n]:
            canvas.draw_text(str(cards[n]), [n_p,70], 50, "White")
        else:
            canvas.draw_polygon(c_p, 2, 'White','Green')
        
#    random.shuffle(cards)
    
    

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric

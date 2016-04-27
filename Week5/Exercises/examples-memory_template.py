# implementation of card game - Memory

import simplegui
import random
    
cards = range(8)
cards.extend(range(8))
random.shuffle(cards)

w =50
h =100

set_text = 0

# helper function to initialize globals
def new_game():
    global state,exposed,set_text
    state = 0
    set_text = 0
    exposed = range(16)
    for i in exposed:
        exposed[i] = False

# define event handlers
def mouseclick(pos):
    # add game state logic here
    global exposed, state, set_text, c1, c2  
    if state == 0:
        ind = pos[0]//w
        if not exposed[ind]:
            exposed[ind] = True
            c1 = ind
        else:
            pass  

        state = 1
        
    elif state == 1:
        ind = pos[0]//w
        if not exposed[ind]:
            exposed[ind] = True
            c2 = ind
        else:
            pass   
        
        state = 2
      
    else:
        ind = pos[0]//w
        
        if not exposed[ind]:
            if cards[c1] != cards[c2]:
                exposed[c1] = False
                exposed[c2] = False  
            exposed[ind] = True
            c1 = ind
        else:
            pass
        
        set_text += 1
        label.set_text("Turns = "+str(set_text))
        state = 1
        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global cards, exposed

    for n in range(len(cards)):
        n_p = w*n+10		# number position
        c_p = [(n*w,0),((n+1)*w,0),((n+1)*w,h),(n*w,h)]		# card position
        if exposed[n]:
            canvas.draw_text(str(cards[n]), [n_p,70], 50, "White")
        else:
            canvas.draw_polygon(c_p, 2, 'White','Green')
        

    

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

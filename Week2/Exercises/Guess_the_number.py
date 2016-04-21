# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number,n
    range100()
    # remove this when you add your code    
    


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global secret_number, n
    secret_number = random.randrange(0,100)
    # 2**n>=high-low+1
    n = math.log(101,2)
    n = int(math.ceil(n))
    print "New game, range is (0,100)."
    print "Number of remaining guesses is ", n
    print ""
    # remove this when you add your code    
    

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global secret_number, n
    secret_number = random.randrange(0,1000)
    # 2**n>=high-low+1
    n = math.log(1001,2)
    n = int(math.ceil(n))
    print "New game, range is (0,1000)."
    print "Number of remaining guesses is ", n
    print ""
    
    
def input_guess(guess):
    # main game logic goes here
    global secret_number, n
    it_g = int(guess)
    print "Guess was ", it_g
    n = n-1
    print "Number of remaining guesses is ", n
    # remove this when you add your code
    if secret_number < it_g:
        print "Lower!"
    elif secret_number > it_g:
        print "Higher!"
    else:
        print "Correct!"   
    print ""
    if n <= 0:
        print "Out of guess!"
        print "Thanks for tring again!"
    
# create frame
f = simplegui.create_frame("Guess Number",200,200)

# register event handlers for control element and start frame
f.add_button("Range is [0,100)", range100,200)
f.add_button("Range is [0,1000)", range1000,200)
f.add_input("Input the guess:", input_guess,200)

# call new_game 
new_game()
f.start()


# always remember to check your completed program against the grading rubric

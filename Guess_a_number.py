# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random
import simplegui
import math

# initialize global variables used in your code
hidden=0
low =0
high=0
counter=0
# helper function to start and restart the game
def new_game():
    # remove this when you add your code    
    frame.start()

# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    new_game()
    global counter
    counter=7
    print "New game. Range is from 0 to 100"
    print "Number of remaining guesses is: ", counter,"\n"
    global hidden 
    hidden=random.randint(0,100)


def range1000():
    new_game()
    global counter
    counter=10
    # button that changes range to range [0,1000) and restarts
    print "New game. Range is from 0 to 1000"
    print "Number of remaining guesses is: ", counter
    global hidden 
    hidden=random.randint(0,1000)
    
def input_guess(guess):
    a=int(guess)
    # main game logic goes here	
    print "Guess was: ",a
    
    global counter 
    global hidden
    counter= counter-1
    if(counter<0):
        print "You are out of guesses. The correct number is: ",hidden
    else:    
        print "Number of remaining guesses is: ",counter
        if(a<hidden):
            print "Higher!\n"
        elif(a>hidden):
            print "Lower!\n"          
        elif(a==hidden):
            print "Correct!\n"
           
# create frame
frame=simplegui.create_frame("Guess Number",400,300)

# register event handlers for control elements
frame.add_button("Range is [0,1000)",range1000,200)
frame.add_button("Range is [0,100)",range100,200)
frame.add_input("Enter a number",input_guess,100)


# call new_game and start frame

new_game()

# always remember to check your completed program against the grading rubric
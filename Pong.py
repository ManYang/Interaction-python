# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2


# initialize ball_pos and ball_vel for new bal in middle of table
ball_pos = [WIDTH/2, HEIGHT/2]
ball_vel=[1,1]

paddle1_vel=0
paddle2_vel=0

paddle1_pos=HEIGHT/2 -HALF_PAD_HEIGHT
paddle2_pos=HEIGHT/2 -HALF_PAD_HEIGHT

score1=score2=0
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    ball_vel=[1,1]

    if direction == 'RIGHT':
        ball_vel = [float((random.randrange(12, 24)/7)), 
                    -float((random.randrange(8, 18))/7)]
        print ball_vel
    elif direction == 'LEFT':
        ball_vel = [-float((random.randrange(12, 24)/7)), 
                    -float((random.randrange(8, 18)/7))]
        print ball_vel
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1=score2=0
    spawn_ball('LEFT')

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel,paddle1_vel,paddle2_vel
 
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0]+=ball_vel[0]
    ball_pos[1]+=ball_vel[1]    
    # draw ball
    c.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")

    # calculate ball position

    #top and bottom walls collide    
    if ball_pos[1]<=BALL_RADIUS:
        ball_vel[1]=-ball_vel[1]
    if ball_pos[1]>=HEIGHT-1-BALL_RADIUS:
        ball_vel[1]=-ball_vel[1]
        
    #right side
    if ball_pos[0]+BALL_RADIUS+PAD_WIDTH>=WIDTH:
        #check whether hits on paddle
        if paddle2_pos<=ball_pos[1]<=paddle2_pos+PAD_HEIGHT:
            ball_vel[0]=-ball_vel[0] 
            ball_vel[0]*=1.1
        else:
            spawn_ball('LEFT')
            score1+=1
    #left side    
    if   ball_pos[0]-BALL_RADIUS-PAD_WIDTH<=0:
        if paddle1_pos<=ball_pos[1]<=paddle1_pos+PAD_HEIGHT:
            ball_vel[0]=-ball_vel[0] 
            ball_vel[0]*=1.1
        else:
            spawn_ball('RIGHT')
            score2+=1
            
    # draw ball
    c.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")
    
    # update paddle's vertical position, keep paddle on the screen    
    paddle1_pos+=paddle1_vel
    paddle2_pos+=paddle2_vel
    
    if paddle1_pos<=0 or paddle1_pos+ PAD_HEIGHT>=HEIGHT:
        paddle1_vel=0
 
    if paddle2_pos<=0 or paddle2_pos+PAD_HEIGHT	>=HEIGHT:
        paddle2_vel=0        
    # draw paddles, right is yellow
    c.draw_line([HALF_PAD_WIDTH,paddle1_pos],
                [HALF_PAD_WIDTH,paddle1_pos+PAD_HEIGHT],
                PAD_WIDTH, "White")
    c.draw_line([WIDTH-HALF_PAD_WIDTH,paddle2_pos],
                [WIDTH-HALF_PAD_WIDTH,paddle2_pos+PAD_HEIGHT],
                PAD_WIDTH, "yellow")    

    # draw scores
    c.draw_text("score "+str(score1),(70,40),32,'white')
    c.draw_text("score "+str(score2),(370,40),32,'white')    
def keydown(key):
    global paddle1_vel, paddle2_vel

    #left paddle
    if key==simplegui.KEY_MAP["up"]:
        paddle2_vel-=5        
    if key==simplegui.KEY_MAP["down"]:
        paddle2_vel+=5
        
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel-=5        
    if key==simplegui.KEY_MAP["s"]:
        paddle1_vel+=5   

        
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["up"]:
        paddle2_vel=0        
    if key==simplegui.KEY_MAP["down"]:
        paddle2_vel=0
        
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel=0        
    if key==simplegui.KEY_MAP["s"]:
        paddle1_vel=0           


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.add_button("restart",new_game)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
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
LEFT = False
RIGHT = True

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel, time # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
#    ball_vel = [0,3]
    ball_vel = [random.randrange(120,240) / 60, random.randrange(-180,-60) / 60]
    if direction == LEFT:
        ball_vel[0] = - ball_vel[0]
        
  

# define event handlers


def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    spawn_ball(RIGHT)
    paddle1_pos = HEIGHT / 2
    paddle2_pos = HEIGHT / 2
    paddle1_vel = 0
    paddle2_vel = 0
    score1 = 0
    score2 = 0

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] +=   ball_vel[0]
    ball_pos[1] +=  ball_vel[1]
        
        #Top/Bottom collide
    if ball_pos[1] >= HEIGHT - BALL_RADIUS - 0:
        ball_vel[1] = - ball_vel[1]
    elif ball_pos[1] <= 0 + BALL_RADIUS + 0:
        ball_vel[1] = - ball_vel[1]
            
        #Gutter collide
    if ball_pos[0] >= WIDTH - BALL_RADIUS - 1:
        if ball_pos[1] >= paddle1_pos - PAD_HEIGHT / 2 - BALL_RADIUS and ball_pos[1] <= paddle1_pos + PAD_HEIGHT / 2 + BALL_RADIUS:
            ball_vel[0] = - ball_vel[0] * 1.1
            #print ball_vel[0]
        else:
            score1 += 1
            spawn_ball(LEFT)
            
            
    elif ball_pos[0] <= 0 + BALL_RADIUS + 1:
        if ball_pos[1] >= paddle2_pos - PAD_HEIGHT / 2 - BALL_RADIUS / 2 and ball_pos[1] <= paddle2_pos + PAD_HEIGHT / 2 + BALL_RADIUS:
            ball_vel[0] = - ball_vel[0] * 1.1
        else:
            score2 += 1
            spawn_ball(RIGHT)
            
            
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "RED", "RED")
    # update paddle's vertical position, keep paddle on the screen
    
    # draw paddles
    if paddle1_pos > 0 + PAD_HEIGHT / 2 and paddle1_pos < HEIGHT - PAD_HEIGHT / 2:
        paddle1_pos += paddle1_vel
    if paddle2_pos > 0 + PAD_HEIGHT / 2 and paddle2_pos < HEIGHT - PAD_HEIGHT / 2:
        paddle2_pos += paddle2_vel
    
    canvas.draw_polygon([(WIDTH , paddle1_pos + PAD_HEIGHT / 2), 
                         (WIDTH , paddle1_pos - PAD_HEIGHT / 2),
                        (WIDTH - PAD_WIDTH, paddle1_pos - PAD_HEIGHT / 2),
                        (WIDTH - PAD_WIDTH, paddle1_pos + PAD_HEIGHT / 2)], 
                        1, "WHITE", "RED")
    canvas.draw_polygon([(0, paddle2_pos + PAD_HEIGHT / 2), 
                         (0, paddle2_pos - PAD_HEIGHT / 2),
                        (PAD_WIDTH, paddle2_pos - PAD_HEIGHT / 2),
                        (PAD_WIDTH, paddle2_pos + PAD_HEIGHT / 2)], 
                        1, "WHITE", "RED")
        
    
    # draw scores
    canvas.draw_text(str(score1), [WIDTH / 4, HEIGHT / 3],40,"GREY")
    canvas.draw_text(str(score2), [3 * WIDTH / 4, HEIGHT / 3],40,"GREY")
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    acc = 3
    if key == simplegui.KEY_MAP["up"]:
        paddle1_vel -= acc
    elif key == simplegui.KEY_MAP["down"]:
        paddle1_vel += acc
    elif key == simplegui.KEY_MAP["w"]:
        paddle2_vel -= acc
    elif key == simplegui.KEY_MAP["s"]:
        paddle2_vel += acc
        

   
def keyup(key):
    global paddle1_vel, paddle2_vel, paddle1_pos, paddle2_pos
    if key == simplegui.KEY_MAP["up"]:
        paddle1_vel = 0
        paddle1_pos += 3
    elif key == simplegui.KEY_MAP["down"]:
        paddle1_vel = 0
        paddle1_pos -= 3
    elif key == simplegui.KEY_MAP["w"]:
        paddle2_vel = 0
        paddle2_pos += 3
    elif key == simplegui.KEY_MAP["s"]:
        paddle2_vel = 0
        paddle2_pos -= 3
    


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

btnNew = frame.add_button('Restart', new_game)


# start frame
new_game()
frame.start()


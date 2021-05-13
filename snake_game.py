import turtle

import time
import random



WIDTH=600
HEIGHT=600

FOOD_SIZE=10
SQUARE_SIZE=20
stepsize=20
delay=100
score=0
highscore=0

segments=[]

def move_snake():
    
    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)
        segments[index].showturtle()
    

    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)
        segments[0].showturtle()
    if head.direction=="up":
        head.sety(head.ycor()+stepsize)

    elif head.direction=="down":
        head.sety(head.ycor()-stepsize)
    
    elif head.direction=="left":
        head.setx(head.xcor()-stepsize)
    
    elif head.direction=="right":
        head.setx(head.xcor()+stepsize)

def go_up():
    if head.direction !="down":
        head.direction="up"

def go_down():
    if head.direction !="up":
        head.direction="down"

def go_right():
    if head.direction !="left":
        head.direction="right"

def go_left():
    if head.direction !="right":
        head.direction="left"


def check_food():
    global score,highscore
    if head.distance(food)<stepsize:
        x=random.randint(-WIDTH/2+FOOD_SIZE,WIDTH/2-FOOD_SIZE)
        y=random.randint(-HEIGHT/2+FOOD_SIZE,HEIGHT/2-FOOD_SIZE)
        food.goto(x,y)
        
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        #new_segment.hideturtle()
        new_segment.shape("square")
        new_segment.color("cyan")
        new_segment.penup()
        
        segments.append(new_segment)
        score +=1
        if score>highscore:
            highscore=score
        pen.clear()
        pen.write(f"Score:{score}  HighScore:{highscore}",align="center", font=("arial",24,"bold"))

def check_body_collision():
    global score
    self_collision=False
    for segment in segments:
        if segment.distance(head)<stepsize:
            head.goto(0,0)
            head.direction="stop"
            self_collision=True

    if head.xcor()<-WIDTH//2 or head.xcor()>WIDTH//2 or head.ycor()<-HEIGHT//2 or head.ycor()>HEIGHT//2:
        self_collision=True
    if self_collision:
        score=0
        newgame()

def play():
    move_snake()
    check_body_collision()
    check_food()
    wn.update()
    turtle.ontimer(play,delay)


def newgame():
    global head, food, segments, pen 

    wn.clear()
    wn.bgcolor("yellow")
    wn.listen()
    wn.onkey(go_up,"Up")
    wn.onkey(go_down,"Down")
    wn.onkey(go_right,"Right")
    wn.onkey(go_left,"Left")


    head=turtle.Turtle()
    head.speed(0)
    head.shape("square")
    head.color("black")
    head.penup()
    head.goto(0,0)
    head.direction="up"

    food=turtle.Turtle()
    food.speed(0)
    food.shape("triangle")
    food.color("red")
    food.penup()
    food.shapesize(FOOD_SIZE/SQUARE_SIZE)
    food.goto(100,100)

    segments=[]
    



wn=turtle.Screen()
wn.title("Snake Game")

wn.setup(WIDTH,HEIGHT)
newgame()

pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score:0  HighScore: 0",align="center", font=("arial",24,"bold"))



play()

turtle.done()

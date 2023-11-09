import turtle

#screen
screen=turtle.Screen()
screen.title("MSK PING PONG GAME")
screen.setup(width=1000,height=600)

#paddle1
paddle1=turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("blue")
paddle1.penup()
paddle1.shapesize(stretch_wid=6,stretch_len=2)
paddle1.goto(-400,0)

#paddle2
paddle2=turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("red")
paddle2.penup()
paddle2.shapesize(stretch_wid=6,stretch_len=2)
paddle2.goto(400,0)

#ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("green")
ball.penup()
ball.goto(0,0)
ball.dx=2
ball.dy=-2

#scoreboard
player1=0
player2=0
score=turtle.Turtle()
score.speed(0)
score.penup()
score.goto(0,260)
score.hideturtle()
score.write("Player 1 : 0 Player 2 : 0",align="center",font=("Arial",20,"bold"))

#paddle move functions
def moveup1():
    y=paddle1.ycor()
    y+=15
    paddle1.sety(y)

def movedown1():
    y=paddle1.ycor()
    y-=15
    paddle1.sety(y)

def moveup2():
    y=paddle2.ycor()
    y+=15
    paddle2.sety(y)

def movedown2():
    y=paddle2.ycor()
    y-=15
    paddle2.sety(y)

screen.listen()
screen.onkeypress(moveup1,"w")
screen.onkeypress(movedown1,"s")
screen.onkeypress(moveup2,"Up")
screen.onkeypress(movedown2,"Down")

#game
while True:
    screen.update()

    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #ball boundary
    if ball.ycor()>280:
        ball.sety(280)
        ball.dy*=-1
    if ball.ycor()<-280:
        ball.sety(-280)
        ball.dy*=-1
    
    if ball.xcor()>480 or ball.xcor()<-480:
        if ball.xcor()>480:
            player1+=1
        else:
            player2+=1
        ball.goto(0,0)
        ball.dx*=-1
        ball.dy*=-1
        score.clear()
        score.write("Player 1 : {} Player 2 : {}".format(player1,player2),align="center",font=("Arial",20,"bold"))

    #ball hit the paddle or not
    if (ball.xcor()<-360 and ball.xcor()>-370) and (paddle1.ycor()+50>ball.ycor()>paddle1.ycor()-50):
        player1+=1
        score.clear()
        score.write("Player 1 : {} Player 2 : {}".format(player1,player2),align="center",font=("Arial",20,"bold"))
        ball.setx(-360)
        ball.dx*=-1
    
    if ball.dy>0 and ball.dy<7:
        ball.dy+=1
    elif ball.dy<0 and ball.dy>-7:
        ball.dy-=1

    if (ball.xcor()>360 and ball.xcor()<370) and (paddle2.ycor()+50>ball.ycor()>paddle2.ycor()-50):
        player2+=1
        score.clear()
        score.write("Player 1 : {} Player 2 : {}".format(player1,player2),align="center",font=("Arial",20,"bold"))
        ball.setx(360)
        ball.dx*=-1
    
    if ball.dy>0 and ball.dy<7:
        ball.dy+=1
    elif ball.dy<0 and ball.dy>-7:
        ball.dy-=1
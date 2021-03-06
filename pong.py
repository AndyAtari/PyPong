import turtle

# window screen
window = turtle.Screen()
window.title("Pong by AndyAtari")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# player 1
paddle_one = turtle.Turtle()
paddle_one.speed(0)
paddle_one.shape("square")
paddle_one.shapesize(stretch_wid=5, stretch_len=1)
paddle_one.color("red")
paddle_one.penup()
paddle_one.goto(-350, 0)

# player 2
paddle_two = turtle.Turtle()
paddle_two.speed(0)
paddle_two.shape("square")
paddle_two.shapesize(stretch_wid=5, stretch_len=1)
paddle_two.color("blue")
paddle_two.penup()
paddle_two.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.15
ball.dy = 0.15

# score card
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.color("white")
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player One: 0  Player Two: 0", align="center", font=("Courier", 24, "normal"))

# score logic
score_one = 0
score_two = 0

# player movement 
def paddle_one_up():
    y = paddle_one.ycor()
    y += 20
    if y >= 250:
        y = 250
    paddle_one.sety(y)

def paddle_one_down():
    y = paddle_one.ycor()
    y -= 20
    if y <= -250:
        y = -250
    paddle_one.sety(y)

def paddle_two_up():
    y = paddle_two.ycor()
    y += 20
    if y >= 250:
        y = 250
    paddle_two.sety(y)

def paddle_two_down():
    y = paddle_two.ycor()
    y -= 20
    if y <= -250:
        y = -250
    paddle_two.sety(y)

# event listeners 
window.listen()
window.onkeypress(paddle_one_up, "w")
window.onkeypress(paddle_one_down, "s")
window.onkeypress(paddle_two_up, "Up")
window.onkeypress(paddle_two_down, "Down")

# game loop
while True:
    window.update() 

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # ball boundaries 
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_one += 1
        pen.clear()
        pen.write(f"Player One: {score_one}  Player Two: {score_two}", align="center", font=("Courier", 24, "normal"))

    
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_two += 1
        pen.clear()
        pen.write(f"Player One: {score_one}  Player Two: {score_two}", align="center", font=("Courier", 24, "normal"))


    # paddle collisions
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_two.ycor() + 50 and ball.ycor() > paddle_two.ycor() -50):
        ball.setx(340)
        ball.dx *= -1

    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_one.ycor() + 50 and ball.ycor() > paddle_one.ycor() -50):
        ball.setx(-340)
        ball.dx *= -1
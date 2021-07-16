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

window.listen()
window.onkeypress(paddle_one_up, "w")
window.onkeypress(paddle_one_down, "s")


while True:
    window.update() 
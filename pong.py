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
paddle_one.color("white")
paddle_one.penup()
paddle_one.goto(-350, 0)



# player 2


while True:
    window.update() 
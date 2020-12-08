# ------------------------------------
# This the famous game "snake"
# ------------------------------------

import turtle
import time
import random

delay=0.1 #ritardo di 0.1 sec per l'aggiornamento della finestra

score = 0
high_score = 0



# ------------------------------------
# set up dello screen
# ------------------------------------
win= turtle.Screen()
win.title("Snake")
win.bgcolor("green")
win.setup(width=600, height=600)


# ------------------------------------
# Creare la testa dello snake
# ogni forma della penna Turtle ha dimensioni standard 20x20 pixels 
# ------------------------------------
head=turtle.Turtle()
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction ="stop"

# ------------------------------------
# Creazione lista per i pezzi del corpo dello snake
# inizialmente vuota
# ------------------------------------
body_snake = []

# ------------------------------------
# Creazione testo per scoring 
# ------------------------------------
penna_score=turtle.Turtle()
penna_score.speed(0)
penna_score.shape("square")
penna_score.color("white")
penna_score.penup()
penna_score.hideturtle()
penna_score.goto(0,260)
penna_score.write("Score: 0    High Score: 0", align="center", font=("Courier", 24, "normal"))



# ------------------------------------
# Creare il cibo per lo snake
# ------------------------------------

food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(100,100)


# ------------------------------------
# Funzioni usate nel main loop
# ------------------------------------

def go_up():
    if head.direction != "down":
        head.direction="up"
    
def go_down():
    if head.direction != "up":
        head.direction="down"

def go_left():
    if head.direction != "right":
        head.direction="left"

def go_right():
    if head.direction != "left":
        head.direction="right"

def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)        
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)
        




# ------------------------------------
# Keyboard bindings (associazione eventi con tastiera)
# ------------------------------------

win.listen()
win.onkeypress(go_up, "w")
win.onkeypress(go_down, "s")
win.onkeypress(go_left, "a")
win.onkeypress(go_right, "d")

# ------------------------------------
# Main game loop
# ------------------------------------

while True:
    # win.update() aggiorna la finestra, altrimenti non risponde più nel ciclo infinito
    win.update()


    # controllo delle collisioni con il bordo della finestra
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"

        # cancella il corpo dello snake
        for new_body in body_snake:
            new_body.goto(1000,1000)
        body_snake.clear()

        #reset dello score
        score=0
        penna_score.clear()
        penna_score.write("Score: {}    High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

   
    # controllo della collisione con il cibo
    if head.distance(food) <20:
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)
        
        new_body=turtle.Turtle()
        new_body.shape("square")
        new_body.color("grey")
        new_body.penup()
        body_snake.append(new_body)
        speed_snake=score/10
        win.tracer(speed_snake)

        #incrementa lo score
        score = score + 10
        if score > high_score:
            high_score = score
        penna_score.clear()
        penna_score.write("Score: {}    High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))


    # movimento dello snake
    # sposta ogni elemento del body nella posizione di quello che lo precede
    for index in range(len(body_snake)-1, 0, -1):
        x=body_snake[index-1].xcor()
        y=body_snake[index-1].ycor()
        body_snake[index].goto(x,y)

    # sposta elemento 0 del body nella posizione della head
    if len(body_snake) >0:
        x=head.xcor()
        y=head.ycor()
        body_snake[0].goto(x,y)


    move()
           
    # controllo della collisione snake su se stesso
    for new_body in body_snake:
        if new_body.distance(head) <20:
            #time.sleep(1)
            head.goto(0,0)
            head.direction ="stop"
            # cancella il corpo dello snake
            for new_body in body_snake:
                new_body.goto(1000,1000)
            body_snake.clear()

            #reset dello score
            score=0
            penna_score.clear()
            penna_score.write("Score: {}    High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

win.mainloop()

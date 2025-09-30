import turtle
import random

# 🐍 Game settings
delay = 150  # Initial delay in milliseconds
score = 0
high_score = 0

# 🎨 Setup screen
win = turtle.Screen()
win.title("🐍 Jeu du Serpent")
win.bgcolor("#1e1e1e")
win.setup(width=600, height=600)
win.tracer(0)

# 🐢 Snake head
head = turtle.Turtle()
head.shape("square")
head.color("#00ff00")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# 🍎 Food
food = turtle.Turtle()
food.shape("circle")
food.color("#ff3333")
food.penup()
food.goto(0, 100)

segments = []

# 🧾 Score display
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  Meilleur: 0", align="center", font=("Courier", 24, "bold"))

# 🎮 Movement functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    elif head.direction == "down":
        head.sety(head.ycor() - 20)
    elif head.direction == "left":
        head.setx(head.xcor() - 20)
    elif head.direction == "right":
        head.setx(head.xcor() + 20)

# ⌨️ Keyboard bindings (AZERTY)
win.listen()
win.onkey(go_up, "z")
win.onkey(go_down, "s")
win.onkey(go_left, "q")
win.onkey(go_right, "d")

# 🔁 Main game loop
def game_loop():
    global score, high_score, delay

    win.update()

    # 🚧 Wall collision
    if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
        reset_game()

    # 🍽️ Food collision
    if head.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("#66ff66")
        new_segment.penup()
        segments.append(new_segment)

        score += 10
        if score > high_score:
            high_score = score

        pen.clear()
        pen.write(f"Score: {score}  Meilleur: {high_score}", align="center", font=("Courier", 24, "bold"))

        delay = max(50, 150 - len(segments) * 2)  # 🐇 Speed up as snake grows

    # 🧩 Move segments
    for i in range(len(segments)-1, 0, -1):
        segments[i].goto(segments[i-1].xcor(), segments[i-1].ycor())
    if segments:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    # 💥 Self collision
    for seg in segments:
        if seg.distance(head) < 20:
            reset_game()
            break

    win.ontimer(game_loop, delay)

# 🔄 Reset function
def reset_game():
    global score, delay
    head.goto(0, 0)
    head.direction = "stop"
    for seg in segments:
        seg.goto(1000, 1000)
    segments.clear()
    score = 0
    delay = 150
    pen.clear()
    pen.write(f"Score: {score}  Meilleur: {high_score}", align="center", font=("Courier", 24, "bold"))

# 🚀 Start the game
game_loop()
win.mainloop()

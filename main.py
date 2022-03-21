from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

# Initialize and set up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Python Snake Game")
screen.tracer(0)

# Creates snake from Snake Class with 3 segments
snake = Snake()

# Creates food from Food Class
food = Food()

# Creates score from ScoreBoard Class
scoreboard = ScoreBoard()

# Start listening to keystrokes
screen.listen()

# Snake movements
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_is_on = True

while game_is_on:
    # How often to refresh the drawings after positions are updated from Snake class
    screen.update()
    time.sleep(0.1)

    # Move function from Snake Class to actually make snake move on screen
    snake.move()

    # Detect collision with food, update score, write new score
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset_scoreboard()
        snake.reset_snake()

    # Detect collision with tail
    for body in snake.body[1:]:
        if snake.head.distance(body) < 10:
            scoreboard.reset_scoreboard()
            snake.reset_snake()

screen.exitonclick()

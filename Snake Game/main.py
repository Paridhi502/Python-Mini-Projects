from turtle import *
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect if the snake hit the food
    if snake.head.distance(food) < 13:
        food.relocate()
        snake.snake_extend()
        score.update_score()

    # detection with walls
    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() > 280
        or snake.head.ycor() < -280
    ):
        game_is_on = False
        score.game_over()

    #detect collision with the snake itself

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) <10:
            game_is_on = False
            score.game_over()


screen.exitonclick()

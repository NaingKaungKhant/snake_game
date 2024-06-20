# My childhood favourite turtle game
import time
from turtle import Screen
from snake import Snake
from food import Food
from score_board import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = Scoreboard()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.speedUp, "s")
screen.onkey(snake.speedUp, "S")
screen.onkey(snake.changeColor, "c")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.18)
    snake.move()

    # Detect collision with the food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.increase_score()


    # Detect collision with the wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -280 or snake.head.ycor() > 300 or snake.head.ycor() < -280:
        """game_is_on = False
        score_board.game_over()"""
        score_board.reset()
        snake.reset()

    # Detect collision with the tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            """game_is_on = False
            score_board.game_over()"""
            score_board.reset()
            snake.reset()


screen.exitonclick()

#sanke game has been done by Naing 06/15/2024
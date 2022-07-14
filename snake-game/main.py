from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
# 关闭屏幕更新
screen.tracer(0)

# create snake, food and score board
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

# control snake
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

# move snake
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #   detect the distance
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    #   detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        # game_is_on = False
        scoreboard.reset_game()
        snake.reset_snake()

    # detect collision with tail
    #    1.regular
    #    for segment in snake.segments:
    #        if segment == snake.head:
    #            pass
    #        elif snake.head.distance(segment) < 10:
    #            game_is_on = False
    #            scoreboard.game_over()

    #   2.slice method
    #   [start : end : step]
    #   [: : -1] reverse

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            scoreboard.reset_game()
            snake.reset_snake()

screen.exitonclick()

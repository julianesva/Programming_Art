from random import randrange, choice
from random import randrange
from turtle import *

from freegames import square, vector

"""The color assignment of the food and the snake is done randomly in a range of 5 different colors and at the same time the logic makes it possible for the food and the snake to always have different colors among the random ones."""
colors = ['blue', 'green', 'yellow', 'purple', 'orange']
snake_color = choice(colors)
food_color = choice([color for color in colors if color != snake_color])

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190

"""======================Function to move the food location in a random way. Without getting itself out of the grid."""
def move_food():
    """Move the food one step in a random direction."""
    directions = [vector(10, 0), vector(-10, 0), vector(0, 10), vector(0, -10)]
    move_direction = choice(directions)
    
    # Computing the new position.
    new_food_position = food + move_direction
    
    # Move the food to the new dirrection only if the new direction is inside the grid.
    if inside(new_food_position):
        food.move(move_direction)


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, snake_color)
              
    move_food()   
    square(food.x, food.y, 9, food_color)
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
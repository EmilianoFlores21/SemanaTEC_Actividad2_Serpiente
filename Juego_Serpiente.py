from turtle import *

from random import random, randrange, randint, choice

from freegames import square, vector

food = vector(randrange(-18,18)*10,randrange(-18,18)*10)
snake = [vector(10, 0)]
aim = vector(0, -10)
color= ["black", "yellow", "blue", "green", "purple"]
r = randint(0,4)
def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)
    global r
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        
        if abs(food.x)<180 and abs(food.x)<180:
            food.x=choice([food.x-10,food.x+10])
            food.y=choice([food.y-10,food.y+10])
        else:
            if(food.x>=180):
                food.x=food.x-10
            elif(food.x<=180):
                food.x=food.x+10
            if(food.y>=180):
                food.y=food.y-10
            elif(food.y<=180):
                food.y=food.y+10

    else:
        snake.pop(0)

    clear()

    for body in snake:    
        
        square(body.x, body.y, 9, color[r])

    square(food.x, food.y, 9, 'green')
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
from graphics import *
from random import *

WINDOW_W = 480

WINDOW_H = 620

SNOWFLAKES = 800

window = GraphWin("Winter wonderland", WINDOW_W, WINDOW_H)

window.setBackground('black')

snowflakes = [None ] * SNOWFLAKES
velocities = [None ] * SNOWFLAKES
for i in range(SNOWFLAKES):
    where = Point(
        random() * WINDOW_W,
        random() * WINDOW_H
    )
    snowflakes[i] = Circle(where, randrange(6, 12))

for snowflake in snowflakes:
    pass


while True:
    snowflake.move(0, 0.01)

    if snowflake.getCenter().y > 700:
        snowflake.move(0, -720)
    

window.getKey()
window.close()
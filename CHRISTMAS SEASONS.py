from graphics import *
from random   import *

COLORS = [
    "white"
    "red"
    "green"
    "blue"
    "magenta"
    "cyan"
    "yellow"
    "pink"
    "purple"
]

WINDOW_W   = 640
WINDOW_H   = 480
SNOWFLAKES = 420

# setup window
window = GraphWin("Winter Wonderland", WINDOW_W, WINDOW_H, False)
window.setBackground("black")

#setup snowflakes
snowflakes = [ None ] * SNOWFLAKES
velocities = [ None ] * SNOWFLAKES
colors     = [ None ] * SNOWFLAKES

for i in range(SNOWFLAKES):
  where = Point(
    random() * WINDOW_W,
    random() * WINDOW_H
  )
  snowflakes[i] = Circle(where, randrange(2, 6))
  snowflakes[i].setOutline("white")
  snowflakes[i].setFill("white")

  velocities[i] = snowflakes[i].getRadius() / 6

while True:
    for i, snowflake in enumerate (snowflakes):
        snowflake.undraw()
        snowflake.move(0, velocities[i])
        if snowflake.getCenter().y > WINDOW_H +6:
            snowflake.move(0, - WINDOW_H - 12)
        snowflake.draw(window)
    update(60)


window.getKey()
window.close()
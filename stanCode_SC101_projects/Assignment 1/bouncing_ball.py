"""
File: Bouncing Balls
Name: Will
-------------------------
TODO: Bounces a ball
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

vy = 0
window = GWindow(800, 500, title='bouncing_ball.py')
switch = True
count = 1
immune = True
bounce_ball = GOval(SIZE, SIZE)


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    window.add(bounce_ball, START_X, START_Y)
    bounce_ball.filled = True
    bounce_ball.color = 'black'
    global immune
    global vy
    onmouseclicked(start)
    counter = 1
    while counter <= 3:
        pause(DELAY)
        if not immune:
            vy += GRAVITY
            bounce_ball.move(VX, vy)  # heading upwards
            if bounce_ball.y + bounce_ball.height >= window.height:  # floor defined
                vy = -vy
                vy *= REDUCE
            elif bounce_ball.x + bounce_ball.width >= window.width:
                immune = True
                window.add(bounce_ball, START_X, START_Y)
                vy = 0
                counter += 1


def start(event):
    global immune
    immune = False


if __name__ == "__main__":
    main()

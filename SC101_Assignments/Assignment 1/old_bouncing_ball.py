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

vy = VX
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
    onmouseclicked(start)
    global bounce_ball
    window.add(bounce_ball, START_X, START_Y)
    bounce_ball.filled = True
    bounce_ball.color = 'black'


def start(event):
    global bounce_ball
    global count
    global switch
    global vy
    global immune
    if immune:
        print("immune on")
        while switch:
            immune = False
            pause(DELAY)
            if bounce_ball.y <= window.height:  # ceiling defined
                vy += GRAVITY
                bounce_ball.move(VX, vy)  # heading downwards
            if bounce_ball.y + bounce_ball.height >= window.height:  # floor defined
                vy = -vy
                vy += GRAVITY
                vy *= REDUCE
                bounce_ball.move(VX, vy)  # heading upwards
            elif bounce_ball.x + bounce_ball.width >= window.width:
                switch = False
        if count < 3:
            window.add(bounce_ball, START_X, START_Y)
            print("bounce " + str(count))  # check bounce session no.
            switch = True
            count += 1
            immune = True
            print("immune off")  # check if immunity on during bounce session
        else:
            print("bounce 3 complete: switch off")  # switch off entire program
            window.add(bounce_ball, START_X, START_Y)


if __name__ == "__main__":
    main()

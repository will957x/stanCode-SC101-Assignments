"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.gui.events.mouse import onmousemoved, onmousedragged, onmouseclicked
from campy.graphics.gobjects import GOval, GRect, GLabel

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3  # Number of attempts


def main():
    graphics = BreakoutGraphics()

    # Add the animation loop here!
    graphics.set_lives(NUM_LIVES)
    while True:
        score = graphics.get_score()
        pause(FRAME_RATE)
        if graphics.ball.y >= graphics.window.height:
            if graphics.get_lives() > 0:
                graphics.reset_ball()
            if graphics.get_lives() == 0 or score >= 1000:  # break point either no lives or no bricks left
                graphics.reset_ball()
                break
        graphics.ball.move(graphics.get_velocity_x(), graphics.get_velocity_y())
        graphics.ball_hit()
        # bounce off left (ball.x <= 0) or right of zone (ball.x >= window width)
        if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
            graphics.set_velocity_x(-graphics.get_velocity_x())
        if graphics.ball.y <= 0:  # bounce off top of zone only
            graphics.set_velocity_y(-graphics.get_velocity_y())


if __name__ == '__main__':
    main()

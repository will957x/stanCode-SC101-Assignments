"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40  # Height of a brick (in pixels)
BRICK_HEIGHT = 15  # Height of a brick (in pixels)
BRICK_ROWS = 10  # Number of rows of bricks
BRICK_COLS = 10  # Number of columns of bricks
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10  # Radius of the ball (in pixels)
PADDLE_WIDTH = 75  # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels)
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 3  # Initial vertical speed for the ball
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):
        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # W code

        # sizes
        self.brick_rows = brick_rows
        self.brick_cols = brick_cols

        # labels
        self.__score = 0
        self.score_label = GLabel("Score: " + str(self.__score))
        self.window.add(self.score_label, x=self.window.width - self.score_label.width - 20,
                        y=self.score_label.height + 10)
        self.__lives = 0
        self.lives_label = GLabel("Lives Remaining: " + str(self.__lives))
        self.window.add(self.lives_label, x=10,
                        y=self.lives_label.height + 10)

        # add bricks
        self.bricks = GRect(BRICK_WIDTH, BRICK_HEIGHT)
        self.bricks_init()

        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height,
                            x=(self.window.width - paddle_width) / 2,
                            y=(self.window.height - paddle_offset))
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = True

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        self.reset_ball()

        # 1 Move paddle function
        onmousemoved(self.paddle_move)

        # 2 click
        onmouseclicked(self.start_velocity)  # set only if dx dy == 0

    # variable naming shorthand: (m)oving (o)bject, (t)op or (b)ottom, (l)eft or (r)ight
    # e.g. motl: moving object top left
    def ball_hit(self):
        motl = self.window.get_object_at(self.ball.x, self.ball.y)
        motr = self.window.get_object_at(BALL_RADIUS * 2 + self.ball.x, self.ball.y)
        mobl = self.window.get_object_at(self.ball.x, BALL_RADIUS * 2 + self.ball.y)
        mobr = self.window.get_object_at(BALL_RADIUS * 2 + self.ball.x, BALL_RADIUS * 2 + self.ball.y)
        if motl is not None:
            if motl is not self.paddle and motl is not self.score_label and motl is not self.lives_label:  # checks if object is paddle or score or lives
                self.window.remove(motl)
                self.__score += 10
                self.__dy *= -1
        elif motr is not None:
            if motr is not self.paddle and motr is not self.score_label and motr is not self.lives_label:  # checks if object is paddle or score or lives
                self.window.remove(motr)
                self.__score += 10
                self.__dy *= -1
                # self.change_paddle()
        elif mobl is not None:
            if mobl is not self.paddle and mobl is not self.score_label and mobl is not self.lives_label:  # checks if object is paddle or score or lives
                self.window.remove(mobl)
                self.__score += 10
                self.__dy *= -1
            else:  # switch to only up for paddle
                if self.__dy > 0:  # switch to only negative
                    self.__dy = -self.__dy
        elif mobr is not None:  # checks if there is object
            if mobr is not self.paddle and mobr is not self.score_label and mobr is not self.lives_label:  # checks if object is paddle or score or lives
                self.window.remove(mobr)
                self.__score += 10
                self.__dy *= -1
            else:  # switch to only up for paddle
                if self.__dy > 0:
                    self.__dy = -self.__dy
        self.score_label.text = "Score: " + str(self.__score)
        self.lives_label.text = "Lives Remaining: " + str(self.__lives)

    # score getter
    def get_score(self):
        return self.__score

    # score setting
    def set_score(self, new_score):
        self.__score = new_score

    # lives getter
    def get_lives(self):
        return self.__lives

    # lives setter
    def set_lives(self, new_lives):
        self.__lives = new_lives

    # velocity getter for dx
    def get_velocity_x(self):
        return self.__dx

    def get_velocity_y(self):
        return self.__dy

    # velocity setter
    def set_velocity_x(self, new_velocity_x):
        self.__dx = new_velocity_x

    def set_velocity_y(self, new_velocity_y):
        self.__dy = new_velocity_y

    def start_velocity(self, event):
        if self.__dy == 0 and self.__dx == 0:  # checks if ball is not moving, ipso facto, ball at starting position
            self.set_ball_velocity()

    # sets ball starting position
    def ball_position(self):
        self.ball.x = ((self.window.width - self.ball.width) / 2)  # sets ball to middle
        self.ball.y = ((self.window.height - self.ball.height) / 2)  # sets ball to middle

    # Returns ball to init position
    def reset_ball(self):
        # self.window.add(self.lives_label, x=10, y=self.lives_label.height + 10)
        self.ball_position()
        self.__dx = 0
        self.__dy = 0
        self.window.add(self.ball)
        if self.__lives == 0:
            pass
        else:
            self.__lives -= 1
            self.lives_label.text = "Lives Remaining: " + str(self.__lives)


    # Sets ball velocity
    def set_ball_velocity(self):
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = -self.__dx

    # Move paddle
    def paddle_move(self, event):
        left_edge = event.x - self.paddle.width / 2
        right_edge = self.window.width - self.paddle.width / 2
        if left_edge >= 0 and event.x <= right_edge:
            self.window.add(self.paddle,
                            x=event.x - self.paddle.width / 2,
                            y=(self.window.height - PADDLE_OFFSET))

    # Draw bricks
    def bricks_init(self):
        for i in range(self.brick_rows):
            for j in range(self.brick_cols):
                self.bricks = GRect(
                    BRICK_WIDTH, BRICK_HEIGHT,
                    x=i * (BRICK_WIDTH + BRICK_SPACING),
                    y=j * (BRICK_HEIGHT + BRICK_SPACING) + BRICK_OFFSET)
                if j == 0 or j == 1:
                    self.bricks.fill_color = 'red'
                elif j == 2 or j == 3:
                    self.bricks.fill_color = 'orange'
                elif j == 4 or j == 5:
                    self.bricks.fill_color = 'yellow'
                elif j == 6 or j == 7:
                    self.bricks.fill_color = 'green'
                elif j == 8 or j == 9:
                    self.bricks.fill_color = 'blue'
                self.bricks.filled = True
                self.window.add(self.bricks)

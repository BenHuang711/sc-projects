"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao


Eliminating the bricks with only three lives. This is the place where all the magic happened.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40  # Height of a brick (in pixels).
BRICK_HEIGHT = 15  # Height of a brick (in pixels).
BRICK_ROWS = 10  # Number of rows of bricks.
BRICK_COLS = 10  # Number of columns of bricks.
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10  # Radius of the ball (in pixels).
PADDLE_WIDTH = 75  # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels).
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball.

NUM_LIVES = 3  # Number of attempts

GAME_ON = 0


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):
        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.window.add(self.paddle, x=(window_width - paddle_width) / 2, y=window_height - paddle_offset)

        # Center a filled ball in the graphical window
        self.ball = GOval(width=ball_radius * 2, height=ball_radius * 2)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.window.add(self.ball, x=(window_width - ball_radius * 2) / 2, y=(window_height - ball_radius * 2) / 2)
        self.dx = MAX_X_SPEED
        self.dy = INITIAL_Y_SPEED
        self.moving = False

        # Initialize our mouse listeners
        onmouseclicked(self.ball_move)
        onmousemoved(self.paddlemove)
        color = 'red'
        # Draw bricks
        for i in range(BRICK_COLS):
            for j in range(BRICK_ROWS):
                if j < BRICK_ROWS / 5:
                    color = 'red'
                if j >= BRICK_ROWS / 5:
                    color = 'orange'
                if (BRICK_ROWS / 5) * 2 <= j < (BRICK_ROWS / 5) * 3:
                    color = 'yellow'
                if (BRICK_ROWS / 5) * 3 <= j < (BRICK_ROWS / 5) * 4:
                    color = 'green'
                if (BRICK_ROWS / 5) * 4 <= j:
                    color = 'blue'
                self.bricks = GRect(width=BRICK_WIDTH, height=BRICK_HEIGHT)
                self.bricks.filled = True
                self.bricks.fill_color = color
                self.bricks.color = color
                self.window.add(self.bricks, 0 + (BRICK_SPACING + BRICK_WIDTH) * i,
                                BRICK_OFFSET + (BRICK_SPACING + BRICK_HEIGHT) * j)

    # let the paddle to move along the mouse
    def paddlemove(self, mouse):
        if 0 + self.paddle.width < mouse.x + self.paddle.width / 2 < self.window.width:
            self.paddle.x = mouse.x - self.paddle.width / 2
            self.paddle.y = self.paddle.y

    # set the call to the center of the window and set the speed of the ball
    # Default initial velocity for the ball
    def ball_set(self):
        self.window.add(self.ball, x=(self.window.width - self.ball.width) / 2,
                        y=(self.window.height - self.ball.height) / 2)
        if self.ball.x == self.window.width - self.ball.width * 2:
            self.dx = random.randint(1, MAX_X_SPEED)
            if (random.random() > 0.5):
                self.dx = -self.dx
            self.dy = INITIAL_Y_SPEED


    # let the ball move with the set speed
    def ball_move(self):
        self.moving = True
        self.ball.move(self.dx, self.dy)

    # check if there are bricks in front of the ball, if there are bricks the bricks will be removed.
    def check_things(self):

        # check the top left corner
        check_things = self.window.get_object_at(self.ball.x, self.ball.y)
        if check_things is not None:
            if check_things is not self.paddle:
                self.window.remove(check_things)
                self.dy = - self.dy
            elif check_things is self.paddle:
                if self.dy > 0:
                    self.dy = -self.dy

        # check the top right corner
        check_things_ru = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        if check_things_ru is not None:
            if check_things_ru is not self.paddle:
                self.window.remove(check_things_ru)
                self.dy = - self.dy

        # check the bottom left corner
        check_things_3 = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)
        if check_things_3 is not None:
            if check_things_3 is not self.paddle:
                self.window.remove(check_things_3)
                self.dy = - self.dy
            elif check_things_3 is self.paddle:
                if self.dy > 0:
                    self.dy = -self.dy

        # check the bottom right corner
        check_things_4 = self.window.get_object_at(self.ball.x + self.ball.width,
                                                   self.ball.y + self.ball.height)
        if check_things_4 is not None:
            if check_things_4 is not self.paddle:
                self.window.remove(check_things_4)
                self.dy = - self.dy

    #when the ball fall out from the window, the ball will be relocated the ball to the center
    def ball_start(self):
        self.ball.x = (self.window.width - self.ball.width * 2) / 2
        self.ball.y = (self.window.height - self.ball.height * 2) / 2

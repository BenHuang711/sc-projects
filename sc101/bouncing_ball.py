"""
File: 
Name:
-------------------------
TODO: simulating a ball bounce till ball can not be seen on the screen three times
while it will not be interrupted by clicking the mouse.
"""

from campy.graphics.gobjects import GOval, GLabel
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
count = 0

window = GWindow(800, 500, title='bouncing_ball.py')

ball = GOval(SIZE, SIZE)
ball.filled = True
ball.fill_color = 'black'
window.add(ball, x=START_X, y=START_Y)


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    onmouseclicked(bouncing)


def bouncing(mouse):
    """
    the ball bounce at certain location and there a counter counts everytime the ball bounces
    out from the screen. With the counter counts to three the whole program stops and during the
    movement, it will not be interfered by clicking the mouse.
    """

    global REDUCE, count
    if ball.x == START_X and ball.y == START_Y:
        vy = 0
        while count < 3:
            ball.move(VX, vy)
            vy += GRAVITY
            if ball.y + SIZE >= window.height:
                vy = -REDUCE * vy
            if ball.x+SIZE >= window.width:
                count += 1
                window.add(ball, START_X, START_Y)
                vy = 0
            pause(DELAY)
    else:
        pass


if __name__ == "__main__":
    main()

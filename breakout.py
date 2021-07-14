"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

Eliminating the bricks with only three lives.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.gui.events.mouse import onmouseclicked

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3  # Number of attempts

graphics = BreakoutGraphics()


def main():
    life = NUM_LIVES
    while life >0:
        graphics.ball_move()
        # check the surrounding and if there's wall it will bounce back with -v
        if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
            graphics.dx = -graphics.dx
        if graphics.ball.y <= 0:
            graphics.dy = -graphics.dy

        # if the ball fall out from the bottom of the window, one life will be eliminated
        # and ball will be relocated to the center.
        if graphics.ball.y + graphics.ball.height >= graphics.window.height:
            life -= 1
            graphics.ball_set()

        # check if there's brick. if there's brick, the brick will be removed and the ball will bounce back.
        graphics.check_things()
        pause(10)

    # when three lives turn to zero, game over and ball will be removed.
    graphics.window.remove(graphics.ball)


if __name__ == '__main__':
    main()

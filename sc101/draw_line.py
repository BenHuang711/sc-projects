"""
File: draw_line
Name: Ben Huang
-------------------------
TODO: Clicking the mouse to create 1st circle following by clicking the mouse again to create
a line while the 1st disappear. The same pattern happens again while clicking again.
"""
from PIL.XVThumbImagePlugin import b
from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 15
window = GWindow(800, 500, title='draw_line.py')
count = 0
first_circle = 0

def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw_line)


def draw_line(event):
    """
    :param event: the x,y of the tip of the mouse
    This function will add one count and create a circle.
    If the count is bigger than 2 than the two point will be linked and the initial circle will be
    removed.
    """
    global count, first_circle
    if count < 1:
        circle = GOval(SIZE, SIZE)
        circle.filled = True
        circle.fill_color = 'white'
        circle.color = 'black'
        window.add(circle, event.x - SIZE / 2, event.y - SIZE / 2)
        first_circle = event
        count += 1
    else:
        line = GLine(event.x, event.y, first_circle.x, first_circle.y)
        maybe_object = window.get_object_at(first_circle.x,first_circle.y)
        if maybe_object is not None:
            window.remove(maybe_object)
        window.add(line)
        count = 0


if __name__ == "__main__":
    main()

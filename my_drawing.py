"""
File: my_drawing
Name: Ben Huang
----------------------
TODO: Drawing Davinci human diagram
"""

from campy.graphics.gobjects import GOval, GRect, GLine, GPolygon, GArc
from campy.graphics.gwindow import GWindow


def main():
    """
    TODO: using different class in gobjects to create graphics.
    """
    window = GWindow(500, 500)
    rect1 = GRect(355, 355, x=73, y=94)
    circle1 = GOval(427, 427, x=37, y=22)
    face = GOval(32, 36, x=234, y=108)
    body = GRect(79,124,x=211,y=144)

    # hangs
    left_hand = GRect(137, 24, x=74, y=152)
    right_hand = GRect(137, 24, x=290, y=152)

    #upper hands
    left_hand1 = GLine(219,145,93,95)
    left_hand2 = GLine(175,152,83,105)
    right_hand1 = GLine(287,143,407,95)
    right_hand2 = GLine(324,154,422,107)

    #leg
    left_feel = GRect(32,180,x=218,y=269)
    right_feet = GRect(32,180,x=251,y=269)

    # left upper leg
    left_line1 = GLine(211,265,135,413)
    left_line2 = GLine(218,317,159,427)

    #right upper leg
    right_line1 = GLine(288,269,360,418)
    right_line2 = GLine(284,332,334,430)

    #add on window
    window.add(right_line1)
    window.add(right_line2)
    window.add(left_line2)
    window.add(left_line1)
    window.add(right_feet)
    window.add(left_hand)
    window.add(right_hand)
    window.add(left_feel)
    window.add(body)
    window.add(face)
    window.add(rect1)
    window.add(circle1)
    window.add(left_hand1)
    window.add(left_hand2)
    window.add(right_hand1)
    window.add(right_hand2)


if __name__ == '__main__':
    main()

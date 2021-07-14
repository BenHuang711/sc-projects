"""
File: sierpinski.py
Name: 
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""
#
# from campy.graphics.gwindow import GWindow
# from campy.graphics.gobjects import GLine
# from campy.gui.events.timer import pause
#
# # Constants
# ORDER = 6  # Controls the order of Sierpinski Triangle
# LENGTH = 600  # The length of order 1 Sierpinski Triangle
# UPPER_LEFT_X = 150  # The upper left x coordinate of order 1 Sierpinski Triangle
# UPPER_LEFT_Y = 100  # The upper left y coordinate of order 1 Sierpinski Triangle
# WINDOW_WIDTH = 950  # The width of the GWindow
# WINDOW_HEIGHT = 700  # The height of the GWindow
#
# # Global Variable
# window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():


#
#     number_list = [1,2,5]
#     print(can_make_sum(number_list, 3))
#
# def can_make_sum(lst, target):
#     ans_lst = []
#     can_make_sum_helper(lst, target, [], ans_lst)
#     return sum(ans_lst) >=1
#
# def can_make_sum_helper(lst,target,current, ans_lst):
#     if len(lst) ==0:
#         if sum(current) == target:
#             ans_lst.append(1)
#         else:
#             ans_lst.append(0)
#
#     else:
#         ele = lst.pop()
#         current.append(ele)
#         can_make_sum_helper(lst,target,current,ans_lst)
#         current.pop()
#         can_make_sum_helper(lst,target,current,ans_lst)
#         lst.append(ele)



    """
	TODO: using recursion to draw triangles
	"""
    sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
    """
	:param order: constant, how many levels of the recursion
	:param length: int, the length of triangle
	:param upper_left_x: int, the initial x of the triangle
	:param upper_left_y: int, the initial y of the triangle
	:return: pictures!
	"""
    if order == 0:
        #	base case
        pass
    else:
        # recursion
        # 左上三角
        sierpinski_triangle(order - 1, length * 0.5, upper_left_x, upper_left_y)
        line_bottom = GLine(upper_left_x, upper_left_y, upper_left_x + length, upper_left_y)
        line_left = GLine(upper_left_x, upper_left_y, upper_left_x + length * 0.5, upper_left_y + length * 0.866)
        line_right = GLine(upper_left_x + length, upper_left_y, upper_left_x + length * 0.5,
                           upper_left_y + length * 0.866)
        window.add(line_bottom)
        window.add(line_left)
        window.add(line_right)
        # 右上三角
        sierpinski_triangle(order - 1, length * 0.5, upper_left_x + length * 0.5, upper_left_y)
        line_bottom = GLine(upper_left_x, upper_left_y, upper_left_x + length, upper_left_y)
        line_left = GLine(upper_left_x, upper_left_y, upper_left_x + length * 0.5, upper_left_y + length * 0.866)
        line_right = GLine(upper_left_x + length, upper_left_y, upper_left_x + length * 0.5,
                           upper_left_y + length * 0.866)
        window.add(line_bottom)
        window.add(line_left)
        window.add(line_right)
        # 中下三角
        sierpinski_triangle(order - 1, length * 0.5, upper_left_x + length * 0.25, upper_left_y + length * 0.433)
        line_bottom = GLine(upper_left_x, upper_left_y, upper_left_x + length, upper_left_y)
        line_left = GLine(upper_left_x, upper_left_y, upper_left_x + length * 0.5, upper_left_y + length * 0.866)
        line_right = GLine(upper_left_x + length, upper_left_y, upper_left_x + length * 0.5,
                           upper_left_y + length * 0.866)
        window.add(line_bottom)
        window.add(line_left)
        window.add(line_right)


if __name__ == '__main__':
    main()

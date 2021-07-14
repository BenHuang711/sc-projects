"""
File: stanCodoshop.py
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

-----------------------------------------------

TODO: Photoshop and make the person disappear in the photo!
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): color distance between red, green, and blue pixel values

    """
    # caculate the distance of the value from the color of the pixel
    color_distance = ((red - pixel.red) ** 2 + (green - pixel.green) ** 2 + (blue - pixel.blue) ** 2) ** 0.5
    return color_distance


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    red = 0
    blue = 0
    green = 0
    color_num = 0

    # calculate the average value of R,G,B of particular pixel by using for loop
    for pixel in pixels:
        red += pixel.red
        blue += pixel.blue
        green += pixel.green
        color_num += 1
    average = [red / color_num, blue / color_num, green / color_num]
    return average


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    color_avg = get_average(pixels)
    pixel_list = []

    # add all the color in the list
    for pixel in pixels:
        pixel_dist = get_pixel_dist(pixel, color_avg[0], color_avg[1], color_avg[2])
        pixel_list.append(pixel_dist)

    # set the value of best_pixel as 0 and assign a random variable
    # in pixel_list as the one which is the minimal value
    best_pixel = 0
    mini_dis = pixel_list[0]
    for i in range(len(pixel_list)):
        if pixel_list[i] < mini_dis:
            mini_dis = pixel_list[i]
            best_pixel = i
    return pixels[best_pixel]


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    ######## YOUR CODE STARTS HERE #########
    # Write code to populate image and create the 'ghost' effect
    # create a empty list and put all the pixel in the list by using for loop
    pixel_list = []
    for x in range(width):
        for y in range(height):
            for img in images:
                pixel = img.get_pixel(x, y)
                pixel_list.append(pixel)

            # start picking the best pixel based on the functions built before and assign the best pixel to the list
            best_pixel = get_best_pixel(pixel_list)
            result_pixel = result.get_pixel(x, y)
            result_pixel.red = best_pixel.red
            result_pixel.blue = best_pixel.blue
            result_pixel.green = best_pixel.green

            # clear the list and start the next cycle
            pixel_list = []
    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()

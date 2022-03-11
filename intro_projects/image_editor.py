# Write a program that processes an image, and outputs a processed image.
# It will take in as command line parameters the path of the image (should just be a file on the local machine), the type of processing to perform, and the name of the output image.

# python3 ./image_processor.py <image_path> <transformation_type> <output_image_path>

# Example:

# python3 ./image_processor.py image.png blue_channel newimage.png

# This will open the image image.png, will process it such that only the blue channel remains, and will write the result to a new image called newimage.png.

# Types of processing that you should implement:

# red_channel
# blue_channel
# green_channel
# These leave only the specified color channel in the image, removing other color channels.

# grayscale
# This grayscales the image.

# invert
# This inverts the colors in the image (see attached image for example).

# half_size
# This reduces the image dimensions by half. For example, a 1200x1600 image will become a 600x800 image.

# mirror_vertical
# Takes the left half of the image (when dividing vertically), and mirrors it onto the right half.

# mirror_horizontal
# Takes the top half of the image (when dividing horizontally), and mirrors it onto the bottom half.

# tile_100
# Takes the top-left 100x100 section of the image, and repeatedly tiles it into a 5x5 arrangement (the output image will have a size of 500x500).

# tile_50
# Takes the bottom-left 50x50 section of the image, and repeatedly tiles it into a 8x8 arrangement (the output image will have a size of 400x400).

# tile_150_100
# Takes the top-right 150x100 section of the image, and repeatedly tiles it into a 3x5 arrangement (the output image will have a size of 450x500).

# average_color
# Computes the average color of the image, and creates a new 100x100 image that contains just that color.

# color_palette
# Given a following color palette of 64 colors[1], replace each color in the image with a color from the palette that is closest to the original color. The distance between two colors is defined as the average of the differences of the RGB color values.

# For example:
# The distance between RGB(10, 10, 10) and (12, 12, 15) is 3.
# The distance between RGB(10, 10, 10) and (14, 14, 17) is 5.
# Therefore (12,12,15) is closer to (10,10,10) than (14,14,17) is.

# Use the attached palette (color_palette.txt), which contains a list of 64 colors in RGB format.


from operator import imod
import sys
import PIL
import os

from PIL import Image, ImageOps
im = Image.open(sys.argv[1])
name = sys.argv[1]
transform = sys.argv[2]
output_name = sys.argv[3]

# im = Image.open("new_image.png")
# print(im.format, im.size, im.mode)
# im.show()
# print(im.getpixel( (0,0) ))
# im.putpixel( (0, 0), (0, 0 ,0) )
# im.show()

def red_channel(image):
    image = name
    [xs, ys] = im.size
    for x in range(0, xs):
        for y in range(0, ys):
            color = im.getpixel( (x,y) )
            im.putpixel((x, y), (color[0], 0 ,0))
    im.save(output_name + ".png")
    new_red_image = output_name + ".png"
    new_red_im = Image.open(new_red_image)
    im.show()

def green_channel(image):
    image = name
    [xs, ys] = im.size
    for x in range(0, xs):
        for y in range(0, ys):
            color = im.getpixel( (x,y) )
            im.putpixel( (x, y), (0, color[1], 0) )
    im.save(output_name + ".png")
    new_green_image = output_name + ".png"
    new_green_im = Image.open(new_green_image)
    im.show()

def blue_channel(image):
    image = name
    [xs, ys] = im.size
    for x in range(0, xs):
        for y in range(0, ys):
            color = im.getpixel( (x,y) )
            im.putpixel( (x, y), (0, 0 , color[2]) )
    im.save(output_name + ".png")
    new_blue_image = output_name + ".png"
    new_blue_im = Image.open(new_blue_image)
    im.show()

def grayscale(image):
    # gray_image = ImageOps.grayscale(im)
    image = name
    [xs, ys] = im.size
    for x in range(0, xs):
        for y in range(0, ys):
            color = im.getpixel((x,y))
            grey_value = int(((color[0] + color[1] + color[2])/ 3))
            im.putpixel( (x, y), (grey_value, grey_value, grey_value) )
    im.save(output_name + ".png")
    new_name = output_name + ".png"
    nim = Image.open(new_name)
    nim.show()

def invert(image):
    image = name
    [xs, ys] = im.size
    for x in range(0, xs):
        for y in range(0, ys):
            color = im.getpixel((x,y))
            im.putpixel( (x, y), ((255-color[0]), (255-color[1]), (255-color[2])) )
    im.save(output_name + ".png")
    new_inv_image = output_name + ".png"
    new_inv_im = Image.open(new_inv_image)
    im.show()

def half_size(image):
    image = name
    size = im.size
    bic = Image.BICUBIC
    resized_og_im = im.resize((round(size[0] * .5), round(size[1] * .5)), bic)
    resized_og_im.save(output_name + ".png")
    resize_im_name = output_name + ".png"
    resize_im = Image.open(resize_im_name)
    resize_im.show()

def flip_vert(image):
    image = name
    flipped_vert = im.transpose(Image.FLIP_LEFT_RIGHT)
    flip_vert_rename = (output_name + ".png")
    flipped_vert.save(flip_vert_rename)
    flip_vert_new = Image.open(flip_vert_rename)
    flip_vert_new.show()


if transform == "grayscale":
    grayscale(im)
elif transform == "red_channel":
    red_channel(im)
elif transform == "blue_channel":
    blue_channel(im)
elif transform == "green_channel":
    green_channel(im)
elif transform == "invert":
    invert(im)
elif transform == "half_size":
    half_size(im)
elif transform == "mirror_vertical":
    flip_vert(im)
else:
    print("Error")
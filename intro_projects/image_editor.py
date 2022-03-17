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

from PIL import Image, ImageOps, PngImagePlugin
image_obj = Image.open(sys.argv[1])
image_name = sys.argv[1]
transform = sys.argv[2]
output_image_filename = sys.argv[3]

# im = Image.open("intro_projects/image.png")
print(image_obj.format, image_obj.size, image_obj.mode)
# im.show()
# print(im.getpixel( (0,0) ))
# im.putpixel( (0, 0), (0, 0 ,0) )
# im.show()

def show_image(input_image):
    input_image.show()

def red_channel(input_image: PIL.PngImagePlugin.PngImageFile, output_filename):
    # image = image_name
    (xs, ys) = input_image.size
    for x in range(0, xs):
        for y in range(0, ys):
            color = input_image.getpixel( (x,y) )
            input_image.putpixel((x, y), (color[0], 0 ,0))
    # input_image.save(output_name + ".png")
    input_image.save(output_filename)
    input_image.show()


# def add(x: int, y: int):
#     return x + y

def green_channel(input_image, output_image_filename):
    # image = image_name
    (xs, ys) = input_image.size
    for x in range(0, xs):
        for y in range(0, ys):
            color = image_obj.getpixel( (x,y) )
            image_obj.putpixel( (x, y), (0, color[1], 0) )
    image_obj.save(output_filename)
    image_obj.show()

def blue_channel(image):
    image = image_name
    [xs, ys] = image_obj.size
    for x in range(0, xs):
        for y in range(0, ys):
            color = image_obj.getpixel( (x,y) )
            image_obj.putpixel( (x, y), (0, 0 , color[2]) )
    image_obj.save(output_image_filename + ".png")
    new_blue_image = output_image_filename + ".png"
    new_blue_im = Image.open(new_blue_image)
    image_obj.show()

def grayscale(image):
    # gray_image = ImageOps.grayscale(im)
    image = image_name
    [xs, ys] = image_obj.size
    for x in range(0, xs):
        for y in range(0, ys):
            color = image_obj.getpixel((x,y))
            grey_value = int(((color[0] + color[1] + color[2])/ 3))
            image_obj.putpixel( (x, y), (grey_value, grey_value, grey_value) )
    image_obj.save(output_image_filename + ".png")
    new_name = output_image_filename + ".png"
    nim = Image.open(new_name)
    nim.show()

def invert(image):
    image = image_name
    [xs, ys] = image_obj.size
    for x in range(0, xs):
        for y in range(0, ys):
            color = image_obj.getpixel((x,y))
            image_obj.putpixel( (x, y), ((255-color[0]), (255-color[1]), (255-color[2])) )
    image_obj.save(output_image_filename + ".png")
    new_inv_image = output_image_filename + ".png"
    new_inv_im = Image.open(new_inv_image)
    image_obj.show()

def half_size(image):
    image = image_name
    size = image_obj.size
    bic = Image.BICUBIC
    resized_og_im = image_obj.resize((round(size[0] * .5), round(size[1] * .5)), bic)
    resized_og_im.save(output_image_filename + ".png")
    resize_im_name = output_image_filename + ".png"
    resize_im = Image.open(resize_im_name)
    resize_im.show()

def flip_vert(image):
    og = image_obj
    flipped_v = Image.new("RGB", og.size)
    for y in range (og.size[1]):
        for x in range (0, og.size[0] // 2):
            new_x = og.size[0] - x
            pixel = og.getpixel((x,y))
            flipped_v.putpixel((new_x-1, y-1),pixel)
    for y in range (og.size[1]):
        for x in range (0, og.size[0] // 2 + 1):
            pixel = og.getpixel((x,y))
            flipped_v.putpixel((x-1, y-1),pixel)
    flipped_v_name = output_image_filename + ".png"
    flipped_v.save(flipped_v_name)
    flipped_vim = Image.open(flipped_v_name)
    flipped_vim.show()

def flip_h(input_image, output_filename):
    og = image_obj
    flipped_h = Image.new("RGB", og.size)
    for x in range(og.size[0]):
        for y in range(0, og.size[1] // 2):
            new_y = og.size[1] - y
            pixel = og.getpixel((x,y))
            flipped_h.putpixel((x-1, new_y-1),pixel)
    for x in range(og.size[0]):
        for y in range (0, og.size[1] // 2 + 1):
            new_y = og.size[1] - y
            pixel = og.getpixel((x,y))
            flipped_h.putpixel((x-1, y-1),pixel)
    flipped_h.save(output_filename + ".png")
    flipped_h.show()

def print_pixel(input_image, output_image, x_start, y_start, x_end, y_end, loc_x, loc_y):
    input_image = image_obj
    # one_hund = Image.new("RGB", (x_size,y_size))
    for y in range (y_start,y_end):
        for x in range (x_start,x_end):
            pixel = input_image.getpixel((x,y))
            output_image.putpixel((loc_x + (x - x_start),loc_y + (y - y_start)), pixel)
    # one_hund.save(output_filename + ".png")
    # input_image.show()

def print_five_hund(input_image, output_filename):
    input_image = image_obj
    five_hund = Image.new("RGB", (500,500))
    for y in range (0, 500, 100):
        for x in range (0, 500, 100):
            print_pixel(input_image, five_hund, 0, 0, 100, 100, x, y)
    five_hund.save(output_filename + ".png")
    five_hund.show()

def print_four_hund(input_image, output_filename):
    input_image = image_obj
    [width, height] = input_image.size
    four_hund = Image.new("RGB", (400,400))
    for y in range (0, 400, 50):
        for x in range (0, 400, 50):
            print_pixel(input_image, four_hund, 0, (height - 50), 50, (height), x, y)
    four_hund.save(output_filename + ".png")
    four_hund.show()

    # print_pixel(input_image, five_hund, 0, 0, 100, 100, 0, 0)
    # print_pixel(input_image, five_hund, 0, 0, 100, 100, 100, 0)
    # print_pixel(input_image, five_hund, 0, 0, 100, 100, 200, 0)
    # print_pixel(input_image, five_hund, 0, 0, 100, 100, 300, 0)
    # print_pixel(input_image, five_hund, 0, 0, 100, 100, 400, 0)
    # print_pixel(input_image, five_hund, 0, 0, 100, 100, 0, 100)
    # print_pixel(input_image, five_hund, 0, 0, 100, 100, 100, 0)

# flip_vert(image_obj)
    
    # [xs, ys] = im.size
    # flipped_vert = im.transpose(Image.FLIP_LEFT_RIGHT)
    # flip_vert_rename = (output_name + ".png")
    # flipped_vert.save(flip_vert_rename)
    # flip_vert_new = Image.open(flip_vert_rename)
    # flip_vert_new.show()


if transform == "grayscale":
    grayscale(image_obj)
elif transform == "red_channel":
    red_channel(image_obj, output_image_filename)
elif transform == "blue_channel":
    blue_channel(image_obj)
elif transform == "green_channel":
    green_channel(image_obj)
elif transform == "invert":
    invert(image_obj)
elif transform == "half_size":
    half_size(image_obj)
elif transform == "mirror_vertical":
    flip_vert(image_obj)
elif transform == "mirror_horizontal":
    flip_h(image_obj, output_image_filename)
elif transform == "100_cut":
    print_pixel(image_obj, image_obj, 0, 0, 100, 100, 100, 100)
elif transform == "tile_100":
    print_five_hund(image_obj, output_image_filename)
elif transform == "tile_50":
    print_four_hund(image_obj, output_image_filename)
else:
    print("Error")

# image_100 = Image.open("new_100.png")
# print(image_100.size)
from PIL import Image
import numpy as np


def get_square_grayness(inp_arr, square_side_size, y_square, x_square):
    res = 0
    for y in range(y_square, y_square + square_side_size):
        for x in range(x_square, x_square + square_side_size):
            res += (int(inp_arr[y][x][0]) + int(inp_arr[y][x][1]) + int(inp_arr[y][x][2])) // 3
    return int(res // 100)


def fill_square(inp_array, new_color, inp_square_side_size, inp_grayscale_step, y_square, x_square):
    for y in range(y_square, y_square + inp_square_side_size):
        for x in range(x_square, x_square + inp_square_side_size):
            inp_array[y][x][0] = int(new_color // inp_grayscale_step) * inp_grayscale_step
            inp_array[y][x][1] = int(new_color // inp_grayscale_step) * inp_grayscale_step
            inp_array[y][x][2] = int(new_color // inp_grayscale_step) * inp_grayscale_step


def filter_the_image(inp_arr, inp_max_y, inp_max_x, inp_square_side_size, inp_grayscale_steps):
    grayscale_step = 255 // inp_grayscale_steps
    y_square = 0
    while y_square < inp_max_y:
        x_square = 0
        while x_square < inp_max_x:
            square_grayness = get_square_grayness(inp_arr, inp_square_side_size, y_square, x_square)
            fill_square(inp_arr, square_grayness, inp_square_side_size, grayscale_step, y_square, x_square)
            x_square = x_square + inp_square_side_size
        y_square = y_square + inp_square_side_size


img = Image.open("img2.jpg")
arr = np.array(img)
max_y = len(arr)
max_x = len(arr[1])
square_side_size = 10
grayscale_steps = 5
filter_the_image(arr, max_y, max_x, square_side_size, grayscale_steps)
res = Image.fromarray(arr)
res.save('res.jpg')

from PIL import Image
import numpy as np

img = Image.open("img2.jpg")
pixels = np.array(img)
width = len(pixels)
height = len(pixels[1])
mosaic_size = int(input("Размер мозаики: "))
color_amount = int(input("Кол-во оттенков серого: "))


def find_average(x, y):
    s = 0
    for n in range(x, min(x + mosaic_size, width)):
        for m in range(y, min(y + mosaic_size, height)):
            r = pixels[n][m][0]
            g = pixels[n][m][1]
            b = pixels[n][m][2]
            brightness = r / 3 + g / 3 + b / 3
            s += brightness
    return int(s // mosaic_size ** 2)


def change_pixels(x, y, average):
    gray_step = 255 // (color_amount - 1)
    for n in range(x, min(x + mosaic_size, width)):
        for m in range(y, min(y + mosaic_size, height)):
            pixels[n][m][0] = int(average // gray_step) * gray_step
            pixels[n][m][1] = int(average // gray_step) * gray_step
            pixels[n][m][2] = int(average // gray_step) * gray_step


def process_pixels():
    for x in range(0, width, mosaic_size):
        for y in range(0, height, mosaic_size):
            average = find_average(x, y)
            change_pixels(x, y, average)


process_pixels()
res = Image.fromarray(pixels)
res.save('res.jpg')

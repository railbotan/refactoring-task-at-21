from PIL import Image
import numpy as np

img = Image.open("img2.jpg")
pixels = np.array(img)
height = len(pixels)
width = len(pixels[1])
mosaic_size = int(input("Размер мозаики: "))
color_amount = int(input("Кол-во оттенков серого: "))


def find_average(x, y):
    return np.average(pixels[x:x + mosaic_size, y:y + mosaic_size])


def change_pixels(x, y, average):
    gray_step = 255 // (color_amount - 1)
    pixels[x:x + mosaic_size, y:y + mosaic_size] = int(average // gray_step) * gray_step


def process_pixels():
    for x in range(0, width, mosaic_size):
        for y in range(0, height, mosaic_size):
            average = find_average(x, y)
            change_pixels(x, y, average)


process_pixels()
res = Image.fromarray(pixels)
res.save('res.jpg')

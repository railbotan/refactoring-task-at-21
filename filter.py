from PIL import Image
import numpy as np


def main():
    url = input("Название изображения: ")
    name = input("Имя результата обработки: ")
    img = Image.open(url)
    pixels = np.array(img)
    mosaic_size = int(input("Размер мозаики: "))
    color_amount = int(input("Кол-во оттенков серого: "))
    pixels = process_pixels(pixels, mosaic_size, color_amount)
    res = Image.fromarray(pixels)
    res.save(name)


def process_pixels(pixels, mosaic_size, color_amount):
    height = len(pixels)
    width = len(pixels[1])
    gray_step = 255 // (color_amount - 1)
    for x in range(0, width, mosaic_size):
        for y in range(0, height, mosaic_size):
            average = find_average(pixels, x, y, mosaic_size)
            pixels = change_pixels(pixels, x, y, average, mosaic_size, gray_step)

    return pixels


def find_average(pixels, x, y, length):
    return np.average(pixels[x:x + length, y:y + length])


def change_pixels(pixels, x, y, average, length, gray_step):
    pixels[x:x + length, y:y + length] = int(average // gray_step) * gray_step
    return pixels


main()

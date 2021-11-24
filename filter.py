from PIL import Image
import numpy as np
img = Image.open("img2.jpg")
rgb_table = np.array(img)
height = len(rgb_table)
width = len(rgb_table[1])
mosaic_size = int(input("Enter the mosaic size "))
grayscale_value = int(input("Enter the grayscale value "))


def count_average_brightness(_i, _j):
        average_brightness = 0
        for n in range(_i, _i + mosaic_size):
            for n1 in range(_j, _j + mosaic_size):
                r = int(rgb_table[n][n1][0])
                g = int(rgb_table[n][n1][1])
                b = int(rgb_table[n][n1][2])
                average_brightness += r//3 + g//3 + b//3
        return int(average_brightness // (mosaic_size * mosaic_size))


def applying_the_filter(_i, _j, _average_brightness):
        for n in range(_i, _i + mosaic_size):
            for n1 in range(_j, _j + mosaic_size):
                rgb_table[n][n1][0] = int(_average_brightness // grayscale_value) * grayscale_value
                rgb_table[n][n1][1] = int(_average_brightness // grayscale_value) * grayscale_value
                rgb_table[n][n1][2] = int(_average_brightness // grayscale_value) * grayscale_value


for i in range(0, height, mosaic_size):
    for j in range(0, width, mosaic_size):
        applying_the_filter(i, j, count_average_brightness(i, j))
res = Image.fromarray(rgb_table)
res.save('res.jpg')

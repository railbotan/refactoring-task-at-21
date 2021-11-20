from PIL import Image
import numpy as np

img = Image.open("img2.jpg")
arr = np.array(img)

length = len(arr)
length_first = len(arr[1])
size = int(input("Введите размер мозайки >> "))
gray = int(input("Введите режим градации серого >> "))

i = 0

def sumColor():
    global n, n1, sum_color
    for n in range(i, i + size):
        for n1 in range(j, j + size):
            r = int(arr[n][n1][0])
            g = int(arr[n][n1][1])
            b = int(arr[n][n1][2])
            sum_color += r + g + b
    sum_color = int(sum_color // 100)

def grayColor   ():
    global n, n1
    for n in range(i, i + size):
        for n1 in range(j, j + size):
            arr[n][n1][0] = int(sum_color // 50) * 50 // gray
            arr[n][n1][1] = int(sum_color // 50) * 50 // gray
            arr[n][n1][2] = int(sum_color // 50) * 50 // gray

while i < length - 1:
    j = 0
    while j < length_first - 1:
        sum_color = 0
        sumColor()
        grayColor()
        j = j + size
    i = i + size
    
res = Image.fromarray(arr)
res.show()
res.save('res.jpg')
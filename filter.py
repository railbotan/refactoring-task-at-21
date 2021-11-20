from PIL import Image
import numpy as np

img = Image.open("img2.jpg")
arr = np.array(img)

length = len(arr)
size = int(input("Введите размер мозайки >> "))
gray = int(input("Введите режим градации серого >> "))

i = 0

def sumColor():
    global n, n1, sum_color
    for n in range(i, i + size):
       sum_color += np.sum(arr[n][j:j+size][:])
    sum_color = sum_color // 100

def grayColor   ():
    global n, n1
    for n in range(i, i + size):
       arr[n][j:j+size][:] = int(sum_color // 50) * 50 // gray

while i < length - 1:
    j = 0
    while j < length - 1:
        sum_color = 0
        sumColor()
        grayColor()
        j = j + size
    i = i + size
    
res = Image.fromarray(arr)
res.show()
res.save('res.jpg')
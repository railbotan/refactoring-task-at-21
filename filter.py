from PIL import Image
import numpy as np

imgURL = input("Укажите название исходного изображения >> ")
imgSave = input("Укажите как сохранить изображение >> ")
img = Image.open(imgURL)

arrImages = np.array(img)
height = len(arrImages)
width = len(arrImages[0])

size = int(input("Введите размер мозайки >> "))
gray = int(input("Введите режим градации серого >> "))
stepGrey = 256 // (gray - 1)

def sumColor(arr, size, x, y):
    return np.average(arr[x: x + size, y:y+size])

def grayColor(arr, size, x, y, sum_color, stepGrey):
    arr[x: x + size, y:y+size] = int(sum_color // stepGrey) * stepGrey # sum_color - sum_color % gray_step

for x in range(0, width, size):
    for y in range(0, height, size):
        sum_color = sumColor(arrImages, size, x, y)
        grayColor(arrImages, size, x, y, sum_color, stepGrey)
    
res = Image.fromarray(arrImages)
res.save(imgSave)
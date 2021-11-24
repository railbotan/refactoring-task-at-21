from PIL import Image
import numpy as np
img = Image.open("img2.jpg")
arr = np.array(img)
a = len(arr)
a1 = len(arr[1])
i = 0
while i < a - 1:
    j = 0
    
    # если остаются необработанные 10 пикселей снизу и справа, то здесь должно быть "j < a1 - 1",
    # а не "j < a1 - 11". Но тогда у меня возникает ошибка IndexError в цикле с итератором "j". Что странно, 
    # потому что с итератором "i" таких проблем не возникает. Думаю, что проблема будет решена на этапе 
    # замены циклов матричными преобразованиями
    while j < a1 - 11:
        s = 0
        for n in range(i, i + 10):
            for n1 in range(j, j + 10):
                r = int(arr[n][n1][0])
                g = int(arr[n][n1][1])
                b = int(arr[n][n1][2])
                s += r + g + b
        s = int(s // 100)
        for n in range(i, i + 10):
            for n1 in range(j, j + 10):
                arr[n][n1][0] = int(s // 3)
                arr[n][n1][1] = int(s // 3)
                arr[n][n1][2] = int(s // 3)
        j = j + 10
    i = i + 10
res = Image.fromarray(arr)
res.save('res.jpg')

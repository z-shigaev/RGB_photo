from PIL import Image
import numpy as np

pSize = 30
N = 6

p000 = Image.open('000.jpg')
p001 = Image.open('001.jpg')
p010 = Image.open('010.jpg')
p011 = Image.open('011.jpg')
p100 = Image.open('100.jpg')
p101 = Image.open('101.jpg')
p110 = Image.open('110.jpg')
p111 = Image.open('111.jpg')

img = Image.open('start.jpg')
Nx = int(img.size[0]/N)
Ny = int(img.size[1]/N)
img = img.resize((Nx, Ny), Image.ANTIALIAS)

matrix = np.zeros(shape=(Nx, Ny))

product = Image.new('RGB', (pSize*Nx, pSize*Ny), 'black')

for i in range(0, Nx):
    for j in range(0, Ny):
        RGB = img.getpixel((i, j))
        RGB_code = [0, 0, 0]
        if RGB[0] >= 127:
            RGB_code[0] = 1
        if RGB[1] >= 127:
            RGB_code[1] = 1
        if RGB[2] >= 127:
            RGB_code[2] = 1
        value = None

        if RGB_code[0] == 1:
            if RGB_code[1] == 1:
                if RGB_code[2] == 1:
                    value = p111
                elif RGB_code[2] == 0:
                    value = p110
            elif RGB_code[1] == 0:
                if RGB_code[2] == 1:
                    value = p101
                elif RGB_code[2] == 0:
                    value = p100
        elif RGB_code[0] == 0:
            if RGB_code[1] == 1:
                if RGB_code[2] == 1:
                    value = p011
                elif RGB_code[2] == 0:
                    value = p010
            elif RGB_code[1] == 0:
                if RGB_code[2] == 1:
                    value = p001
                elif RGB_code[2] == 0:
                    value = p000

        product.paste(value, (i*pSize, j*pSize))

product.save('picture.jpg')









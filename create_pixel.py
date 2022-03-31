from PIL import Image
import numpy as np
Nx = 3
Ny = 3
pSize = 10
pR = Image.open('red.jpg')
pG = Image.open('green.jpg')
pB = Image.open('blue.jpg')
pR = pR.resize((pSize, pSize), Image.ANTIALIAS)
pG = pG.resize((pSize, pSize), Image.ANTIALIAS)
pB = pB.resize((pSize, pSize), Image.ANTIALIAS)
matrix = np.zeros(shape=(Nx, Ny))
# for i in range(0, Nx):
#     for j in range(0, Ny):
#         print((i+j) % 2)
#         if (i+j) % 2 == 0:
#             matrix[i][j] = 1
#         else:
#             matrix[i][j] = 2
for i in range(0, Nx):
    matrix[0][i] = 1
    matrix[1][i] = 2
    matrix[2][i] = 0
img = Image.new('RGB', (pSize*Nx, pSize*Ny), 'black')
for i in range(0, Nx):
    for j in range(0, Ny):
        if matrix[i][j] == 1:
            img.paste(pR, (i*pSize, j*pSize))
        elif matrix[i][j] == 2:
            img.paste(pG, (i*pSize, j*pSize))
        elif matrix[i][j] == 3:
            img.paste(pB, (i * pSize, j * pSize))
        else:
            pass
img.show()
img.save('110.jpg')
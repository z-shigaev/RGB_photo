# # lesson 1
# img = Image.open('blue.jpg')

# img.show()
# print(img.format)
# print(img.mode)
# print(img.size)
# print(img.filename)
# r, g, b = img.split()
# histogram = img.histogram()
# print(histogram)

# img = img.resize((1000, 1000), Image.ANTIALIAS)
# img.save('blue_2.jpg')

# img = Image.open('blue_2.jpg')
# img.show()

# from PIL import Image, ImageDraw, ImageFont
# img = Image.new('RGB', (200, 200), 'black')
# idraw = ImageDraw.Draw(img)
# idraw.rectangle((0, 0, 100, 100), fill='white')
# img.save('test1.jpg')
# img = Image.open('test1.jpg')
# img.show()


# # lesson 2
# im1 = Image.open('red.jpg')
# im2 = Image.open('green.jpg')
#
# im2 = im2.resize((100, 100), Image.ANTIALIAS)
# im1.paste(im2)
# im1.save('fon_pillow_paste.jpg', quality=95)
#
# im1.close()
# im2.close()

# # lesson 3
# import numpy as np
#
# Nx = 3
# Ny = 3
# pSize = 10
#
# pR = Image.open('red.jpg')
# pG = Image.open('green.jpg')
# pB = Image.open('blue.jpg')
#
# pR = pR.resize((pSize, pSize), Image.ANTIALIAS)
# pG = pG.resize((pSize, pSize), Image.ANTIALIAS)
# pB = pB.resize((pSize, pSize), Image.ANTIALIAS)
#
# matrix = np.zeros(shape=(Nx, Ny))
#
# # for i in range(0, Nx):
# #     for j in range(0, Ny):
# #         print((i+j) % 2)
# #         if (i+j) % 2 == 0:
# #             matrix[i][j] = 1
# #         else:
# #             matrix[i][j] = 2
#
# for i in range(0, Nx):
#     matrix[0][i] = 1
#     matrix[1][i] = 2
#     matrix[2][i] = 3
#
# img = Image.new('RGB', (pSize*Nx, pSize*Ny), 'black')
# for i in range(0, Nx):
#     for j in range(0, Ny):
#         if matrix[i][j] == 1:
#             img.paste(pR, (i*pSize, j*pSize))
#         elif matrix[i][j] == 2:
#             img.paste(pG, (i*pSize, j*pSize))
#         elif matrix[i][j] == 3:
#             img.paste(pB, (i * pSize, j * pSize))
#         else:
#             pass
#
# img.show()
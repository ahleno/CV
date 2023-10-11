import numpy as np
import cv2

g_image = cv2.imread('./img/Lena_256g.bmp', cv2.IMREAD_GRAYSCALE)

roberts_x = np.array([[0, 0, -1],
                      [0, 1,  0],
                      [0, 0,  0]])
roberts_y = np.array([[-1, 0, 0],
                      [ 0, 1, 0],
                      [ 0, 0, 0]])

prewitt_x = np.array([[1, 0, -1],
                      [1, 0, -1],
                      [1, 0, -1]])
prewitt_y = np.array([[-1, -1, -1],
                      [ 0,  0, 0],
                      [ 1,  1, 1]])

r_imageX = cv2.convertScaleAbs(cv2.filter2D(g_image, -1, roberts_x))
r_imageY = cv2.convertScaleAbs(cv2.filter2D(g_image, -1, roberts_y))

p_imageX = cv2.convertScaleAbs(cv2.filter2D(g_image, -1, prewitt_x))
p_imageY = cv2.convertScaleAbs(cv2.filter2D(g_image, -1, prewitt_y))

cv2.imshow('Original image', g_image)
cv2.imshow('Roberts X direction image', r_imageX)
cv2.imshow('Roberts Y direction image', r_imageY)
cv2.imshow('Prewitt X direction image', p_imageX)
cv2.imshow('Prewitt Y direction image', p_imageY)

cv2.waitKey(0)
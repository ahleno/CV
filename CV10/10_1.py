import numpy as np
import cv2

g_image = cv2.imread('./img/fortlee_512c.bmp', cv2.IMREAD_GRAYSCALE)

ret, b_image = cv2.threshold(g_image, 128, 255, cv2.THRESH_BINARY)
b_image = g_image


morph_rect = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
morph_cros = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
morph_elip = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

di_image1 = cv2.dilate(b_image, morph_rect, iterations = 1)
di_image2 = cv2.dilate(b_image, morph_cros, iterations = 1)
di_image3 = cv2.dilate(b_image, morph_elip, iterations = 1)
di_image4 = cv2.dilate(b_image, morph_rect, iterations = 3)

cv2.imshow('Original image', g_image)
cv2.imshow('Binary  image', b_image)
cv2.imshow('Dilation image - rect iter 1', di_image1)
cv2.imshow('Dilation image - cross iter 1', di_image2)
cv2.imshow('Dilation image - ellipse iter 1', di_image3)
cv2.imshow('Dilation image - rect iter 4', di_image4)

cv2.waitKey(0) 
import cv2
import numpy as np

i_image = cv2.imread('./img/Lena_256c.bmp', cv2.IMREAD_GRAYSCALE)

s_mask1 = np.array([[-1, -1, -1],
                    [-1, 9, -1],
                    [-1, -1, -1]])

s_mask2 = np.array([[0, -1, 0],
                    [-1, 5, -1],
                    [0, -1, 0]])

s_image1 = cv2.filter2D(i_image, -1, s_mask1)
s_image2 = cv2.filter2D(i_image, -1, s_mask2)

b_image = cv2.GaussianBlur(i_image, (0, 0), 3)
us_image = np.clip(2.*i_image-b_image, 0, 255).astype(np.uint8)

cv2.imshow('Original image', i_image)
cv2.imshow('Sharpen image 1', s_image1)
cv2.imshow('Sharpen image 2', s_image2)
cv2.imshow('Unsharp image', us_image)

cv2.waitKey(0)
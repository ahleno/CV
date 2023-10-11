import cv2

g_image = cv2.imread('./img/CFA_512c.bmp', cv2.IMREAD_GRAYSCALE)

s_imageX = cv2.Sobel(g_image, cv2.CV_8U, 1, 0, ksize = 3)
s_imageY = cv2.Sobel(g_image, cv2.CV_8U, 0, 1, ksize = 3)
s_imageXY = cv2.Sobel(g_image, cv2.CV_8U, 1, 1, ksize = 3)

cv2.imshow('Original image', g_image)
cv2.imshow('Sobel X direction image', s_imageX)
cv2.imshow('Sobel Y direction image', s_imageY)
cv2.imshow('Sobel X-Y direction image', s_imageXY)

cv2.waitKey(0)

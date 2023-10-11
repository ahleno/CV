import cv2

g_image = cv2.imread('./img/CFA_512c.bmp', cv2.IMREAD_GRAYSCALE)

c_image1 = cv2.Canny(g_image, 10, 50)
c_image2 = cv2.Canny(g_image, 150, 300)

cv2.imshow('Original image', g_image)
cv2.imshow('Canny image 1', c_image1)
cv2.imshow('Canny image 2', c_image2)

cv2.waitKey(0)

import cv2

g_image = cv2.imread('./img/Lena_256g_noise.bmp', cv2.IMREAD_GRAYSCALE)

laplacian = cv2.Laplacian(g_image, cv2.CV_8U, ksize = 3)


cv2.imshow('Original image', g_image)

cv2.imshow('Laplacian image', laplacian)

cv2.waitKey(0)

import numpy as np
import cv2

g_image = cv2.imread('./img/fruit_512c.jpg', cv2.IMREAD_GRAYSCALE)
c_image = cv2.cvtColor(g_image, cv2.COLOR_GRAY2BGR)
cv2.imshow('Original image', c_image)

rows, cols = c_image.shape[:2] # channel 여부 무시

# pts1 좌표 표시
pts1 = np.float32([[200,200],[300,200],[200,300]])
cv2.circle(c_image, (200,200), 9, (255,0,0),-1)
cv2.circle(c_image, (300,200), 9, (0,255,0),-1)
cv2.circle(c_image, (200,300), 9, (0,0,255),-1)

pts2 = np.float32([[200,200],[350,200],[200,250]])
Mat1 = cv2.getAffineTransform(pts1, pts2)
r_image1 = cv2.warpAffine(c_image, Mat1, (cols, rows))

pts2 = np.float32([[200,200],[300,230],[260,300]])
Mat2 = cv2.getAffineTransform(pts1, pts2)
r_image2 = cv2.warpAffine(c_image, Mat2, (cols, rows))

pts2 = np.float32([[200,200],[100,170],[170,100]])
Mat3 = cv2.getAffineTransform(pts1, pts2)
r_image3 = cv2.warpAffine(c_image, Mat3, (cols, rows))

cv2.imshow('Original image', c_image)
cv2.imshow('Affine 1 image', r_image1)
cv2.imshow('Affine 2 image', r_image2)
cv2.imshow('Affine 3 image', r_image3)

cv2.waitKey(0)
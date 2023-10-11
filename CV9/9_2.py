import numpy as np
import cv2

c_image = cv2.imread('./img/vegie_512x256c.bmp', cv2.IMREAD_UNCHANGED)
cv2.imshow('Original image', c_image)

rows, cols = c_image.shape[:2] # channel 여부 무시
Mat = np.float32([ [1, 0, 30], # 이동 변환 행렬
                   [0, 1, 60] ])

t_image1 = cv2.warpAffine(c_image, Mat, (cols, rows))
t_image2 = cv2.warpAffine(c_image, Mat, (cols, rows),
                          borderMode=cv2.BORDER_CONSTANT,
                          borderValue=(255,255,255))
t_image3 = cv2.warpAffine(c_image, Mat, (cols, rows),
                          borderMode=cv2.BORDER_REPLICATE)
t_image4 = cv2.warpAffine(c_image, Mat, (cols, rows),
                          borderMode=cv2.BORDER_REFLECT)
t_image5 = cv2.warpAffine(c_image, Mat, (cols, rows),
                          borderMode=cv2.BORDER_WRAP)

cv2.imshow('Original image', c_image)
cv2.imshow('Translation image - default', t_image1)
cv2.imshow('Translation image - BORDER_CONSTANT', t_image2)
cv2.imshow('Translation image - BORDER_REPLICATE', t_image3)
cv2.imshow('Translation image - BORDER_REFLECT', t_image4)
cv2.imshow('Translation image - BORDER_WRAP', t_image5)

cv2.waitKey(0)
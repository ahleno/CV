import numpy as np
import cv2

image = cv2.imread('img/18-4-0.jpg', cv2.IMREAD_UNCHANGED)

<<<<<<< HEAD
=======


>>>>>>> 23d32b85909b6723242ecf2110ff1d11330be207
# 윈도우 생성
cv2.namedWindow("Image", cv2.WINDOW_NORMAL) 

# gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# cv2.imshow("Image", gray_img)
# cv2.waitKey()

### Bitplane MSB
mask = 0x01 << 0

(height, width, channel) = image.shape
    
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
### Masking
for y in range(height):
    for x in range(width):
        if gray_img[y, x] & mask > 0:
            gray_img[y, x] = 255
        else:
            gray_img[y, x] = 0


cv2.imshow("Image", gray_img)
cv2.resizeWindow("Image", 910, 512)

cv2.waitKey(0)
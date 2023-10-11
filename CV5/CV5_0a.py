import numpy as np
import cv2

org_image = cv2.imread('img/fruit_512c.jpg', cv2.IMREAD_UNCHANGED)
# Reference copy
cpy_image = org_image 

cpy_image[150:350, 150:350] = (255, 0, 0)

cv2.imshow("Origin Image", org_image)
cv2.imshow("Copy Image", cpy_image)

cv2.waitKey(0)
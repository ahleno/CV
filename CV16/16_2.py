import numpy as np
import cv2

c_image = cv2.imread('./img/fruit_512c.jpg', cv2.IMREAD_UNCHANGED)
g_image = cv2.cvtColor(c_image, cv2.COLOR_BGR2GRAY)
g_image = cv2.blur(g_image, (5,5))

cv2.imshow('Original image', c_image)

circles = cv2.HoughCircles(g_image, cv2.HOUGH_GRADIENT, 1, 30,
                           param1 = 250, param2 = 10,
                           minRadius = 30, maxRadius = 80)

for circle in circles[0]:
    cv2.circle(c_image, (int(circle[0]), int(circle[1])), 2, (255,0,0), 2)
    cv2.circle(c_image, (int(circle[0]), int(circle[1])), int(circle[2]), (0,0,255), 2)

cv2.imshow("Circle image", c_image)

cv2.waitKey(0)
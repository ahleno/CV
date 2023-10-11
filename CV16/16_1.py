import numpy as np
import cv2

c_image = cv2.imread('./img/fortlee_512c.bmp', cv2.IMREAD_UNCHANGED)
g_image = cv2.cvtColor(c_image, cv2.COLOR_BGR2GRAY)
g_image = cv2.blur(g_image, (5,5)) # 노이즈 제거
e_image = cv2.Canny(g_image, 50, 150, apertureSize=3) # Canny 엣지 검출

cv2.imshow('Original image', c_image)
cv2.imshow('Canny edge image', e_image)

lines = cv2.HoughLines(e_image, 1, np.pi/180, 100)

scale = c_image.shape[0] + c_image.shape[1]

for line in lines:
    rho, theta = line[0]

    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + scale*(-b))
    y1 = int(y0 + scale*(a))
    x2 = int(x0 - scale*(-b))
    y2 = int(y0 - scale*(a))

    cv2.line(c_image, (x1,y1), (x2,y2), (255,0,255), 1)

cv2.imshow("Line image", c_image)

cv2.waitKey(0)
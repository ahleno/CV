import numpy as np
import cv2

g_image = cv2.imread('./img/fruit_512c.jpg', cv2.IMREAD_GRAYSCALE)
c_image = cv2.cvtColor(g_image, cv2.COLOR_GRAY2BGR)
cv2.imshow('Original image', c_image)

rows, cols = c_image.shape[:2] # channel 여부 무시

# pts1 좌표 표시
pts1 = np.float32([[80,280],[220,220],[250,480],[60,420]])
cv2.circle(c_image, (80,280), 9, (255,0,0),-1)
cv2.circle(c_image, (220,220), 9, (0,255,0),-1)
cv2.circle(c_image, (250,480), 9, (0,0,255),-1)
cv2.circle(c_image, (60,420), 9, (0,255,255),-1)

# 평행선 표시
cv2.line(c_image, (0, 340), (511, 340), (255, 0, 0), 2)
cv2.line(c_image, (0, 380), (511, 380), (0, 0, 255), 2)

pts2 = np.float32([[10,10],[502,10],[502,502],[10,502]])
Mat1 = cv2.getPerspectiveTransform(pts1, pts2)

print('Perspective matrix')
print(Mat1)

r_image = cv2.warpPerspective(c_image, Mat1, (cols, rows))

cv2.imshow('Original image', c_image)
cv2.imshow('Perspective image', r_image)

cv2.waitKey(0)
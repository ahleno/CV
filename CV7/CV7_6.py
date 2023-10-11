# 히스토그램 스트레칭

import cv2

image = cv2.imread("img/lenna_256g_dark.bmp", cv2.IMREAD_GRAYSCALE)

hist = cv2.calcHist([image], [0], None, [256], [0, 256])

h_min = 255

for i in range(hist.size):
    if hist[i] > 0:
        h_min = i
        
        break

print(h_min)
print(image.min())
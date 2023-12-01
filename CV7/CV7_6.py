<<<<<<< HEAD
import cv2
from matplotlib import pyplot as plt

g_img = cv2.imread('./img/lena_256g.bmp', cv2.IMREAD_UNCHANGED)

# Stretching
n_img = cv2.normalize(g_img, None, 0, 255, cv2.NORM_MINMAX)

g_hist = cv2.calcHist([g_img], [0], None, [256], [0, 256])
n_hist = cv2.calcHist([n_img], [0], None, [256], [0, 256])

plt.title('Histogram')
plt.plot(g_hist, color='gray')
plt.plot(n_hist, color='blue')

cv2.imshow('Gray Image', g_img)
cv2.imshow('Stretch Image', n_img)
plt.show()

cv2.waitKey(0)
=======
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
>>>>>>> 23d32b85909b6723242ecf2110ff1d11330be207

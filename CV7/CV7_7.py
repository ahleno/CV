import cv2
from matplotlib import pyplot as plt

g_img = cv2.imread('./img/lena_256g.bmp', cv2.IMREAD_UNCHANGED)

# Equlization
n_img = cv2.equalizeHist(g_img)

g_hist = cv2.calcHist([g_img], [0], None, [256], [0, 256])
n_hist = cv2.calcHist([n_img], [0], None, [256], [0, 256])

plt.title('Histogram')S
plt.plot(g_hist, color='gray')
plt.plot(n_hist, color='blue')

cv2.imshow('Gray Image', g_img)
cv2.imshow('Equalization Image', n_img)
plt.show()

cv2.waitKey(0)
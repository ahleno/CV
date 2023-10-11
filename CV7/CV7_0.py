import cv2
from matplotlib import pyplot as plt

c_image = cv2.imread('img/lena_256c.bmp', cv2.IMREAD_UNCHANGED)

c_hist_B = cv2.calcHist([c_image], [0], None, [256], [0, 256])
c_hist_G = cv2.calcHist([c_image], [1], None, [256], [0, 256])
c_hist_R = cv2.calcHist([c_image], [2], None, [256], [0, 256])

plt.title('Histogram')
plt.plot(c_hist_B, color='b')
plt.plot(c_hist_G, color='g')
plt.plot(c_hist_R, color='r')

cv2.imshow('Color image', c_image)
plt.show()

cv2.waitKey(0)
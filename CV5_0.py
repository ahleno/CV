import numpy as np
import cv2

# 배열 객체 생성할 때
# np.ones/zeros(height, width, channel) 순서로 값 지정

cw_image = np.ones((256, 512, 3), np.uint8) * 255
cb_image = np.zeros((256, 512, 3), np.uint8)

cv2.imshow("Color white image", cw_image)
cv2.imshow("Color black image", cb_image)

gw_image = np.ones((256, 512, 1), dtype=np.uint8) * 255
gb_image = np.zeros((256, 512, 1), np.uint8)

# 위와 동일 코드
# gw_image = np.ones((256, 512), dtype=np.uint8) * 255
# gb_image = np.zeros((256, 512), np.uint8)

cv2.imshow("Gray white image", gw_image)
cv2.imshow("Gray black image", gb_image)

cv2.waitKey(0)
import numpy as np
import cv2

c_image = cv2.imread('./img/coins.bmp', cv2.IMREAD_UNCHANGED)
g_image = cv2.cvtColor(c_image, cv2.COLOR_BGR2GRAY)
g_image = cv2.blur(g_image, (7, 7))
ret, b_image = cv2.threshold(g_image, 224, 255,
                             cv2.THRESH_BINARY_INV)
l_image = np.zeros_like(c_image) # 레이블 영상 컬러 이미지 저장용

# 연결 컴포넌트 레이블링 수행
cnt, labels = cv2.connectedComponents(b_image)

print("Total objects = {}".format(cnt))

# 레이블 임의 색상 매핑W
for i in range(cnt):
    l_image[labels==i] = [int(j) for j in np.random.randint(0,255,3)]

# 화면 출력
cv2.imshow('Original Image', g_image)
cv2.imshow('Binary Image', b_image)
cv2.imshow('Label Image', labels.astype(np.uint8)*20)
cv2.imshow('Color Labeled Image', l_image)

cv2.waitKey(0)
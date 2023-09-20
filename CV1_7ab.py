import cv2

image = cv2.imread('img/fortlee_512c.bmp', cv2.IMREAD_UNCHANGED)

(hit, wth, dth) = image.shape

# image[y, x, bgr] = 255
# image[256, 253, 2] = 255
# image[256, 254, 2] = 255
# image[256, 255, 2] = 255
# image[256, 256, 2] = 255
# image[256, 257, 2] = 255

# 가로 파란 줄
y = int(hit / 2)
for i in range(0, wth):
    image[y, i, 0] = 255    
    image[y, i, 1] = 0    
    image[y, i, 2] = 0    

# 세로 빨간 줄
x = int(wth/2)
image[: , x] = (0, 0, 255)

# 영상을 출력
cv2.imshow("Image", image)
cv2.waitKey(0)

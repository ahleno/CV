import cv2

image = cv2.imread('img/fruit_512c.jpg', cv2.IMREAD_UNCHANGED)

# 윈도우 생성
cv2.namedWindow("Image", cv2.WINDOW_AUTOSIZE) 
# cv2.WINDOW_NORMAL : 윈도우 크기를 임의 조정 가능 

# 영상을 출력
cv2.imshow("Image", image)
cv2.waitKey(0)

# 윈도우 크기를 변경
cv2.resizeWindow("Image", 256, 256)
cv2.waitKey(0)

# 윈도우 위치를 (0,0) 위치로 이동
cv2.moveWindow("Image", 0, 0)
cv2.waitKey(0)

# 창을 닫음
cv2.destroyWindow("Image")
# cv2.destroyAllWindows()
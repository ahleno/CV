import cv2

c_image = cv2.imread('./img/fortlee_512c.bmp', cv2.IMREAD_UNCHANGED)

f_image0 = cv2.flip(c_image, 0)
f_image_p1 = cv2.flip(c_image, 1)
f_image_m1 = cv2.flip(c_image, -1)
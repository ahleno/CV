import cv2

g_img = cv2.imread('./img/vegie_512x256g.bmp', cv2.IMREAD_UNCHANGED)

cv2.imshow('Original Image', g_img)

ret, tb_image = cv2.threshold(g_img, 128, 255, cv2.THRESH_BINARY)
ret, bi_image = cv2.threshold(g_img, 128, 255, cv2.THRESH_BINARY_INV)
ret, tr_image = cv2.threshold(g_img, 128, 255, cv2.THRESH_TRUNC)
ret, tz_image = cv2.threshold(g_img, 128, 255, cv2.THRESH_TOZERO)
ret, os_image = cv2.threshold(g_img, 128, 255, cv2.THRESH_OTSU)

cv2.imshow('THRESH_BINARY Image', tb_image)
cv2.imshow('THRESH_BINARY_INV Image', bi_image)
cv2.imshow('THRESH_TRUNC Image', tr_image)
cv2.imshow('THRESH_TOZERO Image', tz_image)
cv2.imshow('THRESH_OTSU Image', os_image)

cv2.waitKey(0)
import cv2

c_image = cv2.imread('./img/vegie_512x256c.bmp', cv2.IMREAD_UNCHANGED)
cv2.imshow('Original image', c_image)

s_image = cv2.resize(c_image, (128, 64), interpolation=cv2.INTER_LINEAR)
cv2.imshow('32x64 image', s_image)

z_image1 = cv2.resize(s_image, (512, 256), interpolation=cv2.INTER_NEAREST)
z_image2 = cv2.resize(s_image, None, None, 4, 4, cv2.INTER_LINEAR)
z_image3 = cv2.resize(s_image, None, fx=4, fy=4, interpolation=cv2.INTER_CUBIC)
z_image4 = cv2.resize(s_image, None, fx=4, fy=4, interpolation=cv2.INTER_AREA)

cv2.imshow('Nearest neighbor intp image', z_image1)
cv2.imshow('Bilinear intp image', z_image2)
cv2.imshow('Cubic intp image', z_image3)
cv2.imshow('Area intp image', z_image4)

# d_image1 = z_image1 - z_image4
# d_image2 = z_image2 - z_image3
# n_image1 = cv2.normalize(d_image1, None, 0, 255, cv2.NORM_MINMAX)
# n_image2 = cv2.normalize(d_image2, None, 0, 255, cv2.NORM_MINMAX)
# cv2.imshow('NN - Area difference image', n_image1)
# cv2.imshow('Bilinear - Cubic difference image', n_image2)

cv2.waitKey(0)